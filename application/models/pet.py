from . import db
from datetime import datetime

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Integer)  # 宠物类型
    city = db.Column(db.String(32))
    postTime = db.Column(db.String(32))
    link = db.Column(db.String(256))
    status = db.Column(db.Integer,default=0) # 0,待收养;1,已收养

    def __init__(self,kind,city,link,postTime=None,status=0):
        self.kind = kind
        self.city = city
        self.link = link
        if postTime:
            postTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.postTime = postTime
        self.status = status






