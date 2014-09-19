from flask import Flask, render_template
from data import read_attendance_data, sort_data, find_facts

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data")
def data():
    data = read_attendance_data()

    return render_template("data.html", d={"data": data})


@app.route("/facts")
def facts():
    data = read_attendance_data()

    facts = find_facts(data)

    x = facts['max']
    y = facts['min']
    z = facts['max_percent']
    a = facts['min_percent']

    return render_template("facts.html", x=x, y=y, z=z, a=a)


@app.route("/data/<order>")
def data_order(order="attendance-desc"):
    data = read_attendance_data()

    if order:
        data = sort_data(data, order)

    return render_template("data.html", d={"data": data})


if __name__ == "__main__":
    app.debug = True
    app.run()