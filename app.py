from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# this only turns off flask sqlalchemy modification tracker,
# not the sqlalchemy modification tracker
app.secret_key = 'davekhim'
# secret key MUST not be published.
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # database가 없을 경우,해당 파일을 config에서 정의한 경로와 유형의 것으로 만들어줌


jwt = JWT(app, authenticate, identity)
# JWT creates an endpont called /auth
# authenticate 함수에 보내서, JW token을 발급해줌
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
# 'http://127.0.0.1:5000/item/<name>'
api.add_resource(ItemList, '/items')
# 'http://127.0.0.1:5000/items'
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
