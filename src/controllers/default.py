from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from src import app, lm
from src.models.forms import LoginForm
from src.models.tables import User


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid Login.")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return redirect("index")


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
