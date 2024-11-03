from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        quote = get_quotes()
    return render_template("index.html", quote=quote)

def get_quotes():
    api_url = 'https://api.api-ninjas.com/v1/quotes?category=happiness'
    response = requests.get(api_url, headers={'X-Api-Key': 'duuMIJlXAhXtMBg489HdeQ==2rLLsZkCgpqBinQg'})
    if response.status_code == 200:
        data = response.json()  # Преобразование ответа в JSON
        if len(data) > 0:
            print(data[0])  # Вывод в консоль, чтобы убедиться в правильности структуры
            return data[0]  # возвращаем первую цитату из списка
    return None  # Если что-то пошло не так

if __name__ == '__main__':
    app.run(debug=True)