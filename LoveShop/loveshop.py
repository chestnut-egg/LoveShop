from flask import Flask, render_template
from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from LoveShop.card_crud import card_line

app = Flask(__name__)
engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/dan", max_overflow=5)
app.config.from_object('dbmysql')



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/shop')
def shop():
    line = card_line()
    card_url = '/static/pic/card/'
    card_filetype = '.png'
    return render_template('shop.html',line = line,card_url=card_url,card_filetype=card_filetype)

@app.route('/card_info')
def card_info():
    return render_template('card_info.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
