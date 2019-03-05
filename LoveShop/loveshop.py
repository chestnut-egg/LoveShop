from flask import *
from sqlalchemy import create_engine
from werkzeug.utils import redirect

from LoveShop.crud.card_crud import *
from LoveShop.crud.user_crud import *
from LoveShop.crud.record_crud import *
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
        password = request.form.get('password')

        user = find_user_by_account(account)

        if (user['user_password'] == '-1'):
            return render_template('login.html', wrong = '用户名错误')
        else:
            if (user['user_password'] != password):
                return render_template('login.html', wrong = '密码错误')
            else:
                session['user_id'] = user['user_id']
                session['user_name'] = user['user_name']
                app.logger.info('user_name： '+user['user_name']+' 已经登陆')
                return redirect(url_for('record'))
    else:
        print('get')
        return render_template('login.html')



@app.route('/record')
def record():
    user_id = session['user_id']
    this_len = record_len(session['user_id'])
    this_record = find_record_by_user_id(user_id)
    return render_template('record.html',record=this_record,record_len=this_len)

@app.route('/shop')
def shop():
    this_len = card_len()
    img = img_card()
    return render_template('shop.html',card_len=this_len,img=img)

@app.route('/card_info')
def card_info():
    card_id = request.args.get("card_id")
    session['card_id'] = card_id
    card = show_cardinfo(card_id)
    img = img_card()
    return render_template('card_info.html',card=card,img=img)

@app.route('/buy_card',methods=['GET','POST'])
def buy_card():
    number = request.form.get('number')
    price = show_cardinfo(session['card_id'])['card_price']
    amount = int(price) * int(number)
    print(str(price) + '*' + str(number) + '=' + str(amount))
    return redirect(url_for('shop'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
