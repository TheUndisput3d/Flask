from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return '<h1>Welcome to the homepage</h1>'

@app.route('/about')
def about():
  return '<h1>Welcome to the about page'

@app.route('/welcome/<name>')
def welcome(name):
  return f'<h1>Welcome {name.title()}!</h1>'

@app.route('/addition/<int:num1>')
def addition(num1):
  return f'<h1>input is {num1}, output is {10 + num1}</h1>'

@app.route('/addition_two/<int:num1>/<int:num2>')
def addition_two(num1, num2):
  return f'<h1>{num1} + {num2} = {num1 + num2}</h1>'

  

if __name__ == '__main__':
  app.run(debug=True)



