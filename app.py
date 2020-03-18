from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "{}".format(os.environ["DATABASE_URI"])

# force update again
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


# db.session.add(User(username="Flask", email="example@example.com"))
# db.session.commit()

@app.route("/")
def index():
    return "this is the homepage"

@app.route("/users")
def users():
    users = User.query.all()
    return render_template('index.html', users=users)
