from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<html><body style="background-color: green; color: white; font-size: 50px; text-align: center;">zarga zarga</body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
