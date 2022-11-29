from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot


from todo.datenbank import abspeichern, auslesen

app = Flask("todo")


@app.route("/")
def start():
        todos = auslesen()
        todos_html = todos.replace("\n","<br>")
        todo_liste = todos.split("\n")
        neue_liste = []
        for eintrag in todo_liste:
            aufgabe, deadline = eintrag.split(",")
            neue_liste.append([aufgabe, deadline])
        return render_template("index.html", liste=neue_liste)


@app.route("/add", methods=["get", "post"])
def add_new_todo():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe:{aufgabe}")
        print(f"Request Form Deadline:{deadline}")
        abspeichern(aufgabe, deadline)
        return "funktioniert"


@app.route("/viz")
def grafik():
    fig = px.pie(labels=[1,2,3,4,5], values= [6,7,8,5,3])
    div = plot(fig, output_type="div" )

    return render_template("viz.html", barchart=div)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
