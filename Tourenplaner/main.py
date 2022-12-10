from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot

from datenbank import abspeichern, auslesen, touren_laden

app = Flask("Tourenplaner")



@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        a = request.form.getlist('a')
        return "1" if len(a) == 1 else "0"
    return render_template('kategorisierung.html')

@app.route("/add", methods=["GET", "POST"])
def add_new_tour():
    if request.method == "GET":
        return render_template("neue_tour.html", seitentitel="Todo Eingabe")

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe: {aufgabe}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(aufgabe, deadline)
        return "hät funktioniert"


@app.route("/overview")
def grafik():
    return "nope"
    """
    todos = todos_laden()
    deadlines = {}
    for todo in todos:
        if todo[1] not in deadlines:
            deadlines[todo[1]] = 1
        else:
            deadlines[todo[1]] += 1

    x = deadlines.keys()
    y = deadlines.values()
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    return render_template("overview.html", barchart=div, seitentitel="Tourenübersicht")
    """

if __name__ == "__main__":
    app.run(debug=True, port=5550)
