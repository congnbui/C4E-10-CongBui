from flask import Flask, render_template

app = Flask(__name__)


@app.route('/aboutme')
def index():
    return render_template("hwss13-html.html")


if __name__ == '__main__':
    app.run()
