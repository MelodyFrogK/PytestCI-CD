from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def some_function():
    return "Hello, World!"

class SomeClass:
    def method(self):
        return "Method called"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
