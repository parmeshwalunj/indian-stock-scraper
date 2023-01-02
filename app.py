from flask import Flask
from stock_web_scraping import main_func

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Running main_func",main_func)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()