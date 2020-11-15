from flask import Flask
from flask import Flask , render_template


app=Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    return render_template('user.html', name=name)
