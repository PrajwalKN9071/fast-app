document.getElementById('chatbot-toggle').addEventListener('click', function() {
    const chatbot = document.getElementById('chatbot');
    chatbot.style.display = chatbot.style.display === 'none' ? 'flex' : 'none';
});

document.getElementById('minimize-btn').addEventListener('click', function() {
    document.getElementById('chatbot').style.display = 'none';
});
