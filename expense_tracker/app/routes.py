from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Expense, Income
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        concept = request.form['concept']
        amount = float(request.form['amount'])
        installments = int(request.form['installments']) if request.form['installments'] else None
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form['due_date'] else None
        new_expense = Expense(date=date, concept=concept, amount=amount, installments=installments, due_date=due_date)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        concept = request.form['concept']
        amount = float(request.form['amount'])
        new_income = Income(date=date, concept=concept, amount=amount)
        db.session.add(new_income)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_income.html')

@app.route('/monthly_report')
def monthly_report():
    expenses = Expense.query.filter(db.extract('month', Expense.date) == datetime.now().month).all()
    incomes = Income.query.filter(db.extract('month', Income.date) == datetime.now().month).all()
    return render_template('report.html', expenses=expenses, incomes=incomes)
