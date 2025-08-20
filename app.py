from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask import render_template, url_for


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'passwddev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32281149@localhost:5432/plannerdb'
login_manager = LoginManager(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True)