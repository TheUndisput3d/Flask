import time
from flask import Flask, redirect, url_for, render_template

from employees import employees_data

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='home')

@app.route('/about')
def about():
  return render_template('about.html', title='about')

@app.route('/employees')
def employees():
  return render_template(
    'employees.html',
    title='employees',
    emps=employees_data
    )

@app.route('/employees/managers')
def managers():
  return render_template(
    'managers.html',
    title='managers',
    emps=employees_data
    )

@app.route('/evaluate/<int:num>')
def evaluate(num):
  return render_template('evaluate.html', title='evaluate', number=num)



if __name__ == '__main__':
  app.run(debug=True)