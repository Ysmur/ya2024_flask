from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Яндекс!"

@app.route('/index')
def index1():
    with open('templates/otbor.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')