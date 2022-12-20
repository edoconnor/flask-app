from flask import Flask
from flask import render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fruit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    food = db.Column(db.String(50))
    color = db.Column(db.String(20))

    def __repr__(self):
        return f"<Fruit {self.id}>"


@app.route("/")
def index():
    fruits = Fruit.query.order_by(Fruit.id.desc()).all()
    return render_template("index.html", fruits=fruits)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        name = request.form["name"]
        food = request.form["food"]
        color = request.form["color"]
        fruit = Fruit(name=name,
                      food=food,
                      color=color,
                      )

        db.session.add(fruit)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create.html")


@app.route('/edit/<int:fruit_id>/', methods=('GET', 'POST'))
def edit(fruit_id):
    fruit = Fruit.query.get_or_404(fruit_id)

    if request.method == "POST":
        name = request.form["name"]
        food = request.form["food"]
        color = request.form["color"]

        fruit.name = name
        fruit.food = food
        fruit.color = color

        db.session.add(fruit)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template('edit.html', fruit=fruit)


@app.route("/delete/<int:fruit_id>/", methods=['POST'])
def delete(fruit_id):
    fruit = Fruit.query.get_or_404(fruit_id)
    db.session.delete(fruit)
    db.session.commit()
    return redirect(url_for("index"))
