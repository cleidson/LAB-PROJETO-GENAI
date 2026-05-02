import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from app.infrastructure.database import get_engine


@pytest.fixture()
def client(tmp_path):
    db_file = tmp_path / "test_prompthub.db"
    os.environ["DATABASE_URL"] = f"sqlite:///{db_file.as_posix()}"
    get_engine.cache_clear()

    from app.api.main import app

    SQLModel.metadata.create_all(get_engine())

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    get_engine.cache_clear()
    os.environ.pop("DATABASE_URL", None)


def create_prompt_payload():
    return {
        "title": "Gerador de rubrica academica",
        "description": "Ajuda a montar criterios de avaliacao.",
        "persona": "Professor universitario",
        "context": "Disciplina de IA aplicada em pos-graduacao.",
        "instructions": "Crie uma rubrica objetiva com niveis de desempenho e nao use jargoes desnecessarios.",
        "expected_output": "Tabela com criterio, peso e descricao.",
        "tags": ["avaliacao", "educacao"],
        "status": "Active",
    }


def test_should_create_valid_prompt(client):
    response = client.post("/api/prompts", json=create_prompt_payload())

    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == "Gerador de rubrica academica"
    assert payload["version"] == 1


def test_should_return_error_when_creating_prompt_without_title(client):
    invalid_payload = create_prompt_payload()
    invalid_payload["title"] = "   "

    response = client.post("/api/prompts", json=invalid_payload)

    assert response.status_code == 422


def test_should_list_prompts(client):
    client.post("/api/prompts", json=create_prompt_payload())

    response = client.get("/api/prompts")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_should_get_existing_prompt_by_id(client):
    created = client.post("/api/prompts", json=create_prompt_payload()).json()

    response = client.get(f"/api/prompts/{created['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_should_return_not_found_for_missing_prompt(client):
    response = client.get("/api/prompts/not-found")

    assert response.status_code == 404


def test_should_update_prompt_and_increment_version(client):
    created = client.post("/api/prompts", json=create_prompt_payload()).json()

    response = client.put(
        f"/api/prompts/{created['id']}",
        json={"description": "Descricao revisada", "tags": ["avaliacao", "qualidade"]},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["version"] == 2
    assert payload["description"] == "Descricao revisada"


def test_should_delete_prompt(client):
    created = client.post("/api/prompts", json=create_prompt_payload()).json()

    delete_response = client.delete(f"/api/prompts/{created['id']}")
    get_response = client.get(f"/api/prompts/{created['id']}")

    assert delete_response.status_code == 200
    assert get_response.status_code == 404


def test_should_analyze_prompt_and_return_score(client):
    created = client.post("/api/prompts", json=create_prompt_payload()).json()

    response = client.post(f"/api/prompts/{created['id']}/analyze")

    assert response.status_code == 200
    payload = response.json()
    assert 0 <= payload["score"] <= 100
    assert payload["classification"] in {"Poor", "Basic", "Good", "Excellent"}


def test_should_calculate_prompt_priority(client):
    created = client.post("/api/prompts", json=create_prompt_payload()).json()

    response = client.post(f"/api/prompts/{created['id']}/priority")

    assert response.status_code == 200
    payload = response.json()
    assert payload["priority"] in {"Low", "Medium", "High", "Critical"}
    assert "recommended_action" in payload
