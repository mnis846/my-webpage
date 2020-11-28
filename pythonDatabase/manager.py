from flask_script import Manager
from flask import Flask

app = Flask(__name__)
# configure your app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()