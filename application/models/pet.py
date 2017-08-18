from . import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Integer)  # 宠物类型
    city = db.Column(db.String(32))
    postTime = db.Column(db.String(32))
    link = db.Colunm(db.String(256))

    def __init__(self,kind,city,postTime,link):
        self.kind = kind
        self.city = city
        self.postTime = postTime
        self.link = link






