from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # database가 없을 경우,해당 파일을 config에서 정의한 경로와 유형의 것으로 만들어줌
