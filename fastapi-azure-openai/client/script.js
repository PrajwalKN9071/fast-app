document.getElementById('chatbot-toggle').addEventListener('click', function() {
    document.getElementById('chatbot').style.display = 'flex';
    this.style.display = 'none';
});

document.getElementById('minimize-btn').addEventListener('click', function() {
    document.getElementById('chatbot').style.display = 'none';
    document.getElementById('chatbot-toggle').style.display = 'block';
});

document.getElementById('send-btn').addEventListener('click', async function() {
    const input = document.getElementById('chatbot-input');
    const message = input.value;
    if (message.trim() === '') return;

    const messagesDiv = document.getElementById('chatbot-messages');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = `You: ${message}`;
    messagesDiv.appendChild(userMessageDiv);

    input.value = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/generate-text/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);  // Log the response to see its structure

        const botMessageDiv = document.createElement('div');
        if (data.choices && data.choices.length > 0) {
            botMessageDiv.textContent = `Bot: ${data.choices[0].message.content}`;
        } else {
            botMessageDiv.textContent = `Bot: No response received`;
        }
        messagesDiv.appendChild(botMessageDiv);
    } catch (error) {
        console.error('Error:', error);
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.textContent = `Error: ${error.message}`;
        messagesDiv.appendChild(errorMessageDiv);
    }
});
