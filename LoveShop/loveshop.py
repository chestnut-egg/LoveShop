from flask import Flask, render_template, request
from sqlalchemy import create_engine
from LoveShop.crud.card_crud import card_line, show_cardinfo
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
from LoveShop.img_config import img_card

app = Flask(__name__)
engine = create_engine(SQLALCHEMY_DATABASE_URI, max_overflow=100)
app.config.from_object('dbmysql')



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    account = request.form.get('account')
    password = request.form.get('password')



    return render_template('record.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/shop')
def shop():
    line = card_line()
    img = img_card()
    return render_template('shop.html',line = line,img=img)

@app.route('/card_info')
def card_info():
    card_id = request.args.get("card_id")
    #print(card_id)

    card = show_cardinfo(card_id)

    img = img_card()

    return render_template('card_info.html',card=card,img=img)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
