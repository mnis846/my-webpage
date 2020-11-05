from flask import Flask

app = Flask(__name__)


@app.route('/david')
def hello():
    return "hello, david !"


@app.route('/')
def start():
    return "manish"


@app.route('/<string:name>')
def input(name):
    return f" hello,  {name}"


if __name__ == '__main__':
    app.run(debug=TRUE)
