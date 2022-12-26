import flask
from flask import render_template, request, redirect, url_for
from wtforms import Form, StringField, validators
import pandas as pd
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    data = pd.read_csv("data.csv")
    data = data.rename(columns={'sales ': 'sales'})
    labels = data.month.values.tolist()
    values = data.sales.values.tolist()

    return render_template("index.html", labels=labels[-5:], values=values[-5:])


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == "GET":
        return render_template('create.html')

    if request.method == "POST":
        month = request.form['month']
        sales = request.form['sales']

        field_names = [request.form['month'], request.form['sales']]

        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(field_names)

        return redirect(url_for("index"))


# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         month = request.form['month']
#         sales = request.form['sales']

#         if not month:
#             flash('Month is required!')
#         elif not sales:
#             flash('Sales is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO XXXX (month, sales) VALUES (?, ?)',
#                          (month, sales))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))

#     return render_template('create.html')
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
