const WebSocket = require('ws');

// Убедитесь, что URL соответствует вашему серверу
const socket = new WebSocket('ws://localhost:8000/ws/');

// Обработка сообщений от сервера
socket.on('message', (data) => {
    console.log('Message from server:', data);
});

// Обработка открытия соединения
socket.on('open', () => {
    console.log('WebSocket connection opened');
    // Отправка сообщения на сервер
    socket.send(JSON.stringify({ message: 'Hello Server!' }));
});

// Обработка закрытия соединения
socket.on('close', () => {
    console.log('WebSocket closed');
});

// Обработка ошибок
socket.on('error', (error) => {
    console.error('WebSocket Error:', error);
});
