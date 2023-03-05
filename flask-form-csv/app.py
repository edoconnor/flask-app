from flask import render_template, redirect, url_for, request 
from flask import Flask
import csv
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit-form', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    with open('responses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([first_name, last_name, email])

    return redirect(url_for("table"))

@app.route('/table')
def table():
    rows = []
    with open('responses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            rows.append(row)
    return render_template('table.html', headers=headers, rows=rows)    

if __name__ == '__main__':
    if not os.path.exists('responses.csv'):
        with open('responses.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['First Name', 'Last Name', 'Email'])
    app.run()