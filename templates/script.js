async function summarizeText() {
    const inputText = document.getElementById('inputText').value;
    const outputSummary = document.getElementById('outputSummary');

    if (!inputText.trim()) {
        outputSummary.innerText = 'Please enter some text to summarize.';
        return;
    }

    outputSummary.innerText = 'Summarizing...';

    const endpoint = 'http://127.0.0.1:8000/summarize';

    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    });

    if (response.ok) {
        const data = await response.json();
        if (data.summary){
            outputSummary.innerText = data.summary;
        }
        else if (data.message){
            outputSummary.innerText = data.message;
        }
    } else {
        outputSummary.innerText = 'Error: Could not summarize the text. Please try again.';
    }
}
