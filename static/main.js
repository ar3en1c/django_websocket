const socket = new WebSocket('ws://localhost:8000/ws/chat/');

socket.onopen = function (e) {
    console.log("Connection established!");
};

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    const messages = document.getElementById('messages');
    const li = document.createElement('li');
    li.textContent = data.message;
    messages.appendChild(li);
};

function sendMessage() {
    const input = document.getElementById("messageInput");
    socket.send(input.value);
    input.value = '';
}