from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For', 'None')
    return f'X-Forwarded-For: {x_forwarded_for}\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


