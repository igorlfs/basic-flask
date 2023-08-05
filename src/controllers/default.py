from flask import render_template

from src import app, db
from src.models.forms import LoginForm
from src.models.tables import User


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
    else:
        print(form.errors)
    return render_template("login.html", form=form)


# @app.route("/teste")
# def teste():
#     r = User.query.filter_by(password="1234").first()
#     print(r.username)
#     # i = User("jojo", "1234", "Julia", "email")
#     # db.session.add(i)
#     # db.session.commit()
#     return "Ok"


# @app.route("/test", defaults={"name": None}, methods=["GET"])
# @app.route("/test/<name>")
# def test(name):
#     if name:
#         return f"Hello, {name}"
#     else:
#         return "Hello, user!"
