from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from models import db
from models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]

        email = request.form["email"]

        password = request.form["password"]

        confirm = request.form["confirm"]

        age = request.form["age"]

        gender = request.form["gender"]

        blood = request.form["blood"]

        phone = request.form["phone"]

        emergency = request.form["emergency"]

        if password != confirm:

            flash("Passwords do not match", "danger")

            return redirect(url_for("auth.register"))

        existing = User.query.filter_by(email=email).first()

        if existing:

            flash("Email already exists", "warning")

            return redirect(url_for("auth.register"))

        hashed = generate_password_hash(password)

        user = User(

            fullname=fullname,

            email=email,

            password=hashed,

            age=age,

            gender=gender,

            blood_group=blood,

            phone=phone,

            emergency_contact=emergency

        )

        db.session.add(user)

        db.session.commit()

        flash("Registration Successful", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful", "success")

            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged Out Successfully", "success")

    return redirect(url_for("main.home"))