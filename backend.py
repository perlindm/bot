from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API-ключи и URL
RAPIDAPI_KEY = "e91259e43cmsh14a3ed98ee053eep16dd00jsn7a94eccb4420"
BASE_URL = "https://skyscanner89.p.rapidapi.com/flights/one-way/list"

# Функция для получения данных о ценах
@app.route('/search-flights', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')  # Город отправления (например, LON)
    destination = request.args.get('destination')  # Город назначения (например, NYC)
    date = request.args.get('date')  # Дата вылета (например, 2023-12-01)

    # Параметры запроса
    querystring = {
        "origin": origin,
        "destination": destination,
        "date": date,
        "adults": "1",  # Количество взрослых пассажиров
        "currency": "USD"  # Валюта
    }

    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "skyscanner89.p.rapidapi.com"
    }

    # Отправляем запрос к Skyscanner API
    response = requests.get(BASE_URL, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Не удалось получить данные"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)

    import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/search-flights', methods=['GET'])
def search_flights():
    try:
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        date = request.args.get('date')

        logging.debug(f"Параметры запроса: origin={origin}, destination={destination}, date={date}")

        querystring = {
            "origin": origin,
            "destination": destination,
            "date": date,
            "adults": "1",
            "currency": "USD"
        }

        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "skyscanner89.p.rapidapi.com"
        }

        response = requests.get(BASE_URL, headers=headers, params=querystring)
        logging.debug(f"Ответ от Skyscanner API: {response.status_code}, {response.text}")

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            logging.error(f"Ошибка Skyscanner API: {response.status_code}, {response.text}")
            return jsonify({"error": "Не удалось получить данные"}), response.status_code
    except Exception as e:
        logging.error(f"Произошла ошибка: {str(e)}")
        return jsonify({"error": "Внутренняя ошибка сервера"}), 500
    @app.route('/search-flights', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date = request.args.get('date')

    # Проверка параметров
    if not origin or not destination or not date:
        return jsonify({"error": "Необходимо указать origin, destination и date"}), 400

    try:
        # Проверка формата даты
        from datetime import datetime
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Неверный формат даты. Используйте YYYY-MM-DD"}), 400

    querystring = {
        "origin": origin,
        "destination": destination,
        "date": date,
        "adults": "1",
        "currency": "USD"
    }

    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "skyscanner89.p.rapidapi.com"
    }

    response = requests.get(BASE_URL, headers=headers, params=querystring)
    data = response.json()

    if response.status_code == 200 and "flights" in data:
        return jsonify(data)
    else:
        logging.error(f"Ошибка Skyscanner API: {response.status_code}, {data}")
        return jsonify({"error": data.get("message", "Не удалось получить данные")}), response.status_code
    import os

# Замените строку с RAPIDAPI_KEY
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")