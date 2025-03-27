import os
from flask import Flask

app = Flask(__name__)
name = os.environ.get('YOUR_NAME', 'friend')

@app.route('/')
def hello():
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
