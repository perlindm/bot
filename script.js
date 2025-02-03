// script.js

// Обработчик для кнопок
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', () => {
        const action = button.id;

        switch (action) {
            case 'flights':
                window.open('https://www.skyscanner.com', '_blank');
                break;
            case 'hotels':
                window.open('https://www.booking.com', '_blank');
                break;
            case 'tours':
                window.open('https://www.getyourguide.com', '_blank');
                break;
            default:
                console.error('Неизвестное действие');
        }
    });
});

// Обработчик для формы поиска авиабилетов
document.getElementById('flight-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const origin = document.getElementById('origin').value.toUpperCase();
    const destination = document.getElementById('destination').value.toUpperCase();
    const date = document.getElementById('date').value;

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "<p>Загрузка...</p>";

    try {
        const response = await fetch(`http://localhost:5000/search-flights?origin=${origin}&destination=${destination}&date=${date}`);
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Не удалось получить данные");
        }
        const data = await response.json();

        if (data && data.flights) {
            let flightsHtml = "<h3>Результаты поиска:</h3><ul>";
            data.flights.forEach(flight => {
                flightsHtml += `<li>${flight.airline} - $${flight.price}</li>`;
            });
            flightsHtml += "</ul>";
            resultDiv.innerHTML = flightsHtml;
        } else {
            resultDiv.innerHTML = `<p>${data.error || "Билеты не найдены."}</p>`;
        }
    } catch (error) {
        console.error("Ошибка:", error);
        resultDiv.innerHTML = `<p>Произошла ошибка: ${error.message}</p>`;
    }
});