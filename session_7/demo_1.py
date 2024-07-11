from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def home():
  response = make_response("<h1>Welcome to the homepage!</h1>")
  return response

@app.route("/set_cookie")
def set_cookie():
  response = make_response("<h1>Welcome to the set_cookie page!</h1>")
  response.set_cookie("cookie_name", "cookie_value") 
  return response

@app.route("/get_cookie")
def get_cookie():
  value = request.cookies.get("cookie_name")
  response = make_response(f"<h1>The value of the cookie is <i>{value}</i>.<h1>")
  return response


if __name__ == "__main__":
  app.run(debug=True)

