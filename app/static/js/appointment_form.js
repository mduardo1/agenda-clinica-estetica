const clientSelect = document.querySelector("#client_id");
const procedureSelect = document.querySelector("#procedure_id");
const clientInfo = document.querySelector("#clientInfo");
const procedureInfo = document.querySelector("#procedureInfo");

function selectedOption(select) {
    return select.options[select.selectedIndex];
}

function updateClientInfo() {
    const option = selectedOption(clientSelect);
    if (!option || !option.value) {
        clientInfo.textContent = "Nome e WhatsApp aparecem aqui.";
        return;
    }

    clientInfo.textContent = `${option.dataset.name} | WhatsApp: ${option.dataset.whatsapp}`;
}

function updateProcedureInfo() {
    const option = selectedOption(procedureSelect);
    if (!option || !option.value) {
        procedureInfo.textContent = "Nome, custo, valor e lucro aparecem aqui.";
        return;
    }

    procedureInfo.textContent = [
        option.dataset.name,
        `Custo: ${option.dataset.cost}`,
        `Valor: ${option.dataset.price}`,
        `Lucro: ${option.dataset.profit}`,
    ].join(" | ");
}

if (clientSelect && procedureSelect) {
    clientSelect.addEventListener("change", updateClientInfo);
    procedureSelect.addEventListener("change", updateProcedureInfo);
}
