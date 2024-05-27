from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Expense, Income  # Asegúrate de que 'Income' esté definido en models.py
from datetime import datetime

@app.route('/')
def index():
    expenses = Expense.query.all()
    incomes = Income.query.all()
    return render_template('index.html', expenses=expenses, incomes=incomes)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        new_expense = Expense(description=description, amount=amount, date=datetime.strptime(date, '%Y-%m-%d'))
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        new_income = Income(description=description, amount=amount, date=datetime.strptime(date, '%Y-%m-%d'))
        db.session.add(new_income)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_income.html')
