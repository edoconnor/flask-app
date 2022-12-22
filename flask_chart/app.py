import flask
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    data = [
        ("Jan", 100),
        ("Feb", 110),
        ("Mar", 105),
        ("Apr", 115),
        ("May", 105),
    ]

    labels = []
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])

    return render_template("index.html", labels=labels, values=values)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
