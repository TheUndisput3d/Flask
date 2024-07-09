from flask import Flask, url_for, render_template, redirect, flash
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html", title='home')



@app.route('/signup', methods=["GET", "POST"])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    flash(f"Successfully Registered {form.username.data}")
    return redirect(url_for("home"))
  return render_template(
    "signup.html",
    title="Sign Up",
    form=form
  )

@app.route('/login', methods=["GET", "POST"])
def login():
  form = LoginForm()
  email = form.email.data
  pw = form.password.data
  if form.validate_on_submit():
    if email == "a@b.com" and pw == "12345":
      flash(f"Logged in Successfully!")
      return redirect(url_for("home"))
    else:
      flash(f"Incorrect email or password!")
  return render_template(
    "login.html",
    title="Login",
    form = form
  )

if __name__ == '__main__':
  app.run(debug=True)

