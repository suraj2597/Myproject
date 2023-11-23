from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=["POST", "GET"])
def get_weatherdata():
    if request.method == 'POST':
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': request.form.get("city"),
            'appid': request.form.get('appid'),
            'units': request.form.get('units')
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            city = data.get('name', 'Unknown')
            return f"data : {data}, city: {city}"
        else:
            error_message = data.get('message', 'Unknown error')
            return f"Error: {error_message}"
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
