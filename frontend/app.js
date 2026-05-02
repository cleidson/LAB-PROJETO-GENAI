const API_BASE_URL = "http://localhost:8000/api/prompts";

const form = document.getElementById("prompt-form");
const promptIdField = document.getElementById("prompt-id");
const feedback = document.getElementById("feedback");
const promptList = document.getElementById("prompt-list");
const template = document.getElementById("prompt-card-template");
const formTitle = document.getElementById("form-title");

document.getElementById("refresh-list").addEventListener("click", loadPrompts);
document.getElementById("cancel-edit").addEventListener("click", resetForm);
form.addEventListener("submit", handleSubmit);

function collectPayload() {
    return {
        title: document.getElementById("title").value.trim(),
        description: document.getElementById("description").value.trim() || null,
        persona: document.getElementById("persona").value.trim() || null,
        context: document.getElementById("context").value.trim() || null,
        instructions: document.getElementById("instructions").value.trim(),
        expected_output: document.getElementById("expected_output").value.trim(),
        tags: document.getElementById("tags").value
            .split(",")
            .map((tag) => tag.trim())
            .filter(Boolean),
        status: document.getElementById("status").value
    };
}

async function handleSubmit(event) {
    event.preventDefault();

    const payload = collectPayload();
    const promptId = promptIdField.value;
    const method = promptId ? "PUT" : "POST";
    const url = promptId ? `${API_BASE_URL}/${promptId}` : API_BASE_URL;

    const response = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        const error = await response.json();
        showFeedback(error.detail || "Nao foi possivel salvar o prompt.", true);
        return;
    }

    showFeedback(promptId ? "Prompt atualizado com sucesso." : "Prompt criado com sucesso.");
    resetForm();
    await loadPrompts();
}

async function loadPrompts() {
    promptList.innerHTML = "<p>Carregando prompts...</p>";
    const response = await fetch(API_BASE_URL);
    const prompts = await response.json();

    promptList.innerHTML = "";

    if (!prompts.length) {
        promptList.innerHTML = "<p>Nenhum prompt cadastrado ainda.</p>";
        return;
    }

    prompts.forEach((prompt) => {
        const node = template.content.cloneNode(true);
        const card = node.querySelector(".prompt-card");

        node.querySelector(".prompt-title").textContent = prompt.title;
        node.querySelector(".prompt-meta").textContent = `Versao ${prompt.version} • ${prompt.status}`;
        node.querySelector(".badge").textContent = prompt.status;
        node.querySelector(".prompt-description").textContent = prompt.description || "Sem descricao.";

        const tagList = node.querySelector(".tag-list");
        if (prompt.tags.length) {
            prompt.tags.forEach((tag) => {
                const span = document.createElement("span");
                span.className = "tag";
                span.textContent = tag;
                tagList.appendChild(span);
            });
        } else {
            const span = document.createElement("span");
            span.className = "tag";
            span.textContent = "sem-tags";
            tagList.appendChild(span);
        }

        const resultBox = node.querySelector(".result-box");
        resultBox.textContent = "Use os botoes abaixo para analisar ou priorizar.";

        card.querySelector('[data-action="edit"]').addEventListener("click", () => populateForm(prompt));
        card.querySelector('[data-action="delete"]').addEventListener("click", () => deletePrompt(prompt.id));
        card.querySelector('[data-action="analyze"]').addEventListener("click", async () => {
            const result = await postAction(`${API_BASE_URL}/${prompt.id}/analyze`);
            if (!result) return;
            resultBox.innerHTML = `<strong>Analise:</strong> ${result.classification} (${result.score}/100)<br>${formatSuggestions(result.suggestions)}`;
        });
        card.querySelector('[data-action="priority"]').addEventListener("click", async () => {
            const result = await postAction(`${API_BASE_URL}/${prompt.id}/priority`);
            if (!result) return;
            resultBox.innerHTML = `<strong>Prioridade:</strong> ${result.priority}<br>${result.reason}<br><em>${result.recommended_action}</em>`;
        });

        promptList.appendChild(node);
    });
}

function populateForm(prompt) {
    formTitle.textContent = "Editar prompt";
    promptIdField.value = prompt.id;
    document.getElementById("title").value = prompt.title;
    document.getElementById("description").value = prompt.description || "";
    document.getElementById("persona").value = prompt.persona || "";
    document.getElementById("context").value = prompt.context || "";
    document.getElementById("instructions").value = prompt.instructions;
    document.getElementById("expected_output").value = prompt.expected_output;
    document.getElementById("tags").value = prompt.tags.join(", ");
    document.getElementById("status").value = prompt.status;
}

function resetForm() {
    form.reset();
    promptIdField.value = "";
    formTitle.textContent = "Novo prompt";
}

async function deletePrompt(promptId) {
    const response = await fetch(`${API_BASE_URL}/${promptId}`, { method: "DELETE" });

    if (!response.ok) {
        showFeedback("Nao foi possivel excluir o prompt.", true);
        return;
    }

    showFeedback("Prompt excluido com sucesso.");
    await loadPrompts();
}

async function postAction(url) {
    const response = await fetch(url, { method: "POST" });

    if (!response.ok) {
        const error = await response.json();
        showFeedback(error.detail || "Falha na operacao.", true);
        return null;
    }

    return response.json();
}

function formatSuggestions(suggestions) {
    if (!suggestions.length) {
        return "Sem sugestoes de melhoria.";
    }
    return suggestions.map((item) => `- ${item}`).join("<br>");
}

function showFeedback(message, isError = false) {
    feedback.textContent = message;
    feedback.style.color = isError ? "#dc2626" : "#166534";
}

loadPrompts();
