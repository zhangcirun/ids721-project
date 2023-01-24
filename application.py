from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "hello world !!"

@application.route('/text')
def some_text():
    return "some text.."

if __name__ == "__main__":
    application.run()