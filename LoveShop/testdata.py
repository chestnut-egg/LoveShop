from LoveShop.crud.card_crud import *
from LoveShop.crud.user_crud import *
from LoveShop.crud.record_crud import add_record
import datetime


add_user('dandan','dandan','12345678')

add_card('包饺子','ql卡','一起包饺子','8')
add_card('包饺子','ql卡','一起包饺子','8')
add_card('包饺子','ql卡','一起包饺子','8')
add_card('包饺子','ql卡','一起包饺子','8')
add_card('包饺子','ql卡','一起包饺子','8')

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
add_record(1,now_time,'购买卡片',5,'交易完成')
add_record(1,now_time,'购买卡片',5,'交易完成')