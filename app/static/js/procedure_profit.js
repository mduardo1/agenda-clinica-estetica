const costInput = document.querySelector("#cost");
const priceInput = document.querySelector("#price");
const profitOutput = document.querySelector("#profitOutput");

function formatCurrency(value) {
    return new Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL",
    }).format(value);
}

function updateProfit() {
    const cost = Number(costInput.value || 0);
    const price = Number(priceInput.value || 0);
    profitOutput.textContent = `Lucro: ${formatCurrency(price - cost)}`;
}

if (costInput && priceInput && profitOutput) {
    costInput.addEventListener("input", updateProfit);
    priceInput.addEventListener("input", updateProfit);
    updateProfit();
}
