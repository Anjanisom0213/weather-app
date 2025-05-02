from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('get_weather')
def handle_weather_request(city):
    print(f"🔎 Looking up weather for: {city}")
    response = requests.get(BASE_URL, params={
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    })

    print("🌐 API Request URL:", response.url)
    print("📦 Response Code:", response.status_code)
    print("📄 Response Body:", response.text)

    if response.status_code == 200:
        data = response.json()
        emit('weather_response', {
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'city': data['name']
        })
    else:
        emit('weather_response', {
            'error': 'City not found or API error.'
        })

if __name__ == '__main__':
    socketio.run(app, debug=True)
