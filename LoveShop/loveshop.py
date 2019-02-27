from flask import Flask, render_template, request, session
from sqlalchemy import create_engine
from LoveShop.crud.card_crud import card_line, show_cardinfo
from LoveShop.crud.user_crud import find_user_by_account
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
from LoveShop.img_config import img_card

app = Flask(__name__)
engine = create_engine(SQLALCHEMY_DATABASE_URI, max_overflow=100)
app.config.from_object('dbmysql')
app.config['SECRET_KEY'] = '123456'


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account = request.form.get('account')
        print(account)
        password = request.form.get('password')
        print(password)


        user = find_user_by_account(account)

        if (user['user_password'] == '-1'):
            return render_template('login.html', wrong = '用户名错误')
        else:
            if (user['user_password'] != password):
                return render_template('login.html', wrong = '密码错误')
            else:
                session['user_id'] = user['user_id']
                session['user_name'] = user['user_name']
                return render_template('record.html', user_name = session['user_name'])
    else:
        print('get')
        return render_template('login.html')



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
    card = show_cardinfo(card_id)
    img = img_card()
    return render_template('card_info.html',card=card,img=img)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
