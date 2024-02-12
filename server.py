from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<marker>')
def list_prof(marker):
    with open("static/resource/prof.txt", encoding='utf-8') as f:
        data = f.readlines()
    return render_template('list_prof.html', marker=marker, data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')