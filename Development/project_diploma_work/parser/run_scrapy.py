from flask import Flask

app = Flask(__name__)

@app.route('/run_scrapy', methods=['GET'])
def run_scrapy():
    mas = []
    for i in range(0,10,1):
        mas[i] = "ха"
    return mas

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
