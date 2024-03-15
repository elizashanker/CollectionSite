from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def missia():
    news = {
        "title": "Сегодня хорошая погода",
        "content": "Невероятно, сегодня хорошая погода"
    }
    return render_template("text.html", title="Yes", news=news)

if __name__ == '__main__':
    app.run(port=5050, host="127.0.0.1")