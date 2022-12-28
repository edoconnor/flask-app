from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=d165339b5bc5a67a68ea36b2a7695185&units=imperial')

        json_object = r.json()

        temperature = int(json_object['main']['temp'])
        wind = int(json_object['wind']['speed'])
        condition = json_object['weather'][0]['main']

        return render_template('index.html', temperature=temperature, city_name=city_name, condition=condition, wind=wind)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
