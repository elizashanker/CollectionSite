from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def missia():
    news = {
            "title": "Сегодня хорошая погода",
            "content": "Невероятно, сегодня хорошая погода"
        }
    return render_template('index.html')


@app.route("/index")
def deviz():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1", debug=True)
