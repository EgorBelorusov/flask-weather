from unittest import result

from flask import Flask, request, render_template
import requests


app = Flask(__name__) # создание приложения





def get_weather(name_city: str):

    try:
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": name_city, "count": 1},
            timeout=5
        )

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return "Город не найден"

        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]


        # Шаг 2: получить погоду по этим координатам
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]},
            timeout=5
        )
        weather_data = weather_response.json()

        temp = weather_data["current"]["temperature_2m"]
        wind = weather_data["current"]["wind_speed_10m"]
        return f"В городе {name_city}: температура {temp} градусов, ветер {wind} м/сек"

    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"











@app.route("/") # ждет запрос с адресом /, чтобы вызвать функцию ниже
def home():
    return render_template("index.html") # возвращает и отображает на странице

@app.route("/about")
def about():
    return "Это страница 'О нас'"


@app.route("/hello/<name>") # Всё, что стоит в адресе на месте <name>, Flask передаёт в функцию одноимённым аргументом. Открыв /hello/Егор, вы получите name = "Егор"
def hello(name):
    return f"Привет, {name}!"


@app.route("/square/<int:n>") # получение числа конвертером int:, иначе строка
def square(n):
    return f"Квадрат {n} равен {n * n}"


CITYS = ["Tomsk", "Seversk", "Novosibirsk"]
@app.route("/weather")
def weather():
    city = request.args.get("city") # этот метод извлекает из адреса URL указанный параметр после ?
    result = None

    if city:
        result = get_weather(city)
    return render_template("weather.html", city=city, result=result, citys = CITYS) # рендерит weather.html и передает переменную city внутрь шаблона


@app.route("/api/ping")
def ping():
    return {"status": "ok"} # Flask превращает ваш словарь в JSON-текст и ставит заголовок Content-Type: application/json


@app.route("/add/summ")
def summ():
    a = request.args.get("one", type=int)
    b = request.args.get("two", type=int)

    if a is None or b is None:
        return {"error": "нужны числа"}, 400
    else:
        return {"sum": a + b}


if __name__ == "__main__":
    app.run(debug=True)





















