from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('helloworld.txt') as f:
        lines =f.readlines()
    return str(lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)