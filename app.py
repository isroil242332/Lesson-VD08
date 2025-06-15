from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.api-ninjas.com/v1/quotes"
API_KEY = "+o31Gl5oYGS1ufsRAjhvig==pNF1A1b0mfaZ1MJk"  # Вставьте сюда ваш API ключ с api-ninjas.com

def get_random_quote():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            quote = data[0]['quote']
            author = data[0]['author']
            return quote, author
    return "Не удалось получить цитату.", ""

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

@app.route('/new_quote')
def new_quote():
    quote, author = get_random_quote()
    return {'quote': quote, 'author': author}

if __name__ == "__main__":
    app.run(debug=True)