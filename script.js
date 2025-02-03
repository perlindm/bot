// Инициализация Telegram Web App
const tg = window.Telegram.WebApp;

// Кнопка "Авиабилеты"
document.getElementById('flights').addEventListener('click', () => {
    tg.sendData('search_flights'); // Отправляем данные обратно в бота
});

// Кнопка "Отели"
document.getElementById('hotels').addEventListener('click', () => {
    tg.sendData('search_hotels');
});

// Кнопка "Экскурсии"
document.getElementById('tours').addEventListener('click', () => {
    tg.sendData('search_tours');
});
