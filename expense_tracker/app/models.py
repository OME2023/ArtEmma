from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    concept = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    installments = db.Column(db.Integer, nullable=True)
    due_date = db.Column(db.Date, nullable=True)

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    concept = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
