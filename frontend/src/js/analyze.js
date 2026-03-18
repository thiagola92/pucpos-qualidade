
async function onAnalyzeRequested() {
    let url = urlField.value;
    let response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "url": url,
        })
    })

    if (!response.ok) {
        console.log(response)
        urlField.removeAttribute("aria-invalid")
        resultText.textContent = "Falha na comunicação com o server."
        return
    }

    content = await response.json();

    if (content["is_legit"] == true) {
        urlField.setAttribute("aria-invalid", "false");
        resultText.textContent = "Parece legitimo"
    } else {
        urlField.setAttribute("aria-invalid", "true");
        resultText.textContent = "Parece phishing"
    }
}

function onWindowLoad() {
    analyzeButton.addEventListener("click", onAnalyzeRequested);
}

window.onload = onWindowLoad