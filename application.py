from flask import Flask
from flask import render_template
from flask import request
from flask.ext.runner import Runner

app = Flask(__name__)
runner = Runner(app)

@app.route('/')
def hello_world():
    return render_template('chat.html')


if __name__ == '__main__':
    runner.run()