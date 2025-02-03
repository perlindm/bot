// Инициализация Telegram Web App
const tg = window.Telegram.WebApp;

// Функция для открытия ссылок через Telegram
function openLink(url) {
    tg.openLink(url); // Открывает ссылку через Telegram
}

// Кнопка "Авиабилеты"
document.getElementById('flights').addEventListener('click', () => {
    openLink('https://www.skyscanner.com');
});

// Кнопка "Отели"
document.getElementById('hotels').addEventListener('click', () => {
    openLink('https://www.booking.com');
});

// Кнопка "Экскурсии"
document.getElementById('tours').addEventListener('click', () => {
    openLink('https://www.getyourguide.com');
});
