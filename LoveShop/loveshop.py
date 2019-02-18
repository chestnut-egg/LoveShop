from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/card_info')
def card_info():
    return render_template('card_info.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
