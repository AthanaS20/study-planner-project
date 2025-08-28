from app.routes import app
from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, logout_user, login_required
from .models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Logged in Successfully!", 'sucess')
            return redirect(url_for(dashboard))
        else:
            flash("Invalid Username or Password", 'danger') 
            return render_template("login.html") 
  

    return render_template("login.html")
