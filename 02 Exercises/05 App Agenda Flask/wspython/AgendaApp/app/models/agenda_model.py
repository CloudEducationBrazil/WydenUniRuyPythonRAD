from app import db

class Agenda(db.Model):
    __tablename__ = "agenda"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    realizada = db.Column(db.Boolean, default=False)
