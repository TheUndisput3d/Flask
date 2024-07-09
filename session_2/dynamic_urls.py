from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Welcome to the homepage.</h1>'

@app.route('/welcome/<name>')
def Welcome(name):
  return f'<h1>Hey, {name.title()}. Welcome to the homepage.</h1>'


if __name__ == '__main__':
  app.run(debug=True)