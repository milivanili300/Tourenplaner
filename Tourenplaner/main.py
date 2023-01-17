import json

from flask import Flask
from flask import render_template
from flask import request

import plotly.express as px
from plotly.offline import plot

from datenbank import abspeichern, auslesen

app = Flask("Tourenplaner")


# Erstellung der Startseite, bei welcher Touren gefiltert werden können
@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        dauer = request.form["dauer"]
        hoehenmeter = request.form["hoehenmeter"]
        tiefenmeter = request.form["tiefenmeter"]
        schwierigkeit = request.form["schwierigkeit"]
        erreichbarkeit = request.form["erreichbarkeit"]
        gefahrenstufe = request.form["gefahrenstufe"]
        # Code, welcher die Daten aus Json abruft
        # gegenprüfen von eingabe und daten in json
        # leere Liste für die Touren welche mit den gesetzten Radios übereinstimmen wird erstellt
        with open("data.json") as datei:
            vorschlag = json.load(datei)
        selection = []
        for key, value in vorschlag.items():
            if hoehenmeter == value["hoehenmeter"]:
                if dauer == value["dauer"]:
                    if tiefenmeter == value["tiefenmeter"]:
                        if schwierigkeit == value["schwierigkeit"]:
                            if gefahrenstufe == value["gefahrenstufe"]:
                                if erreichbarkeit == value["erreichbarkeit"]:
                                    # wenn die ausgewählten Eigenschaften mit den Touren übereinstimmen werden
                                    # sie in die Liste auswahl gespeichert
                                    selection.append(key)
                                    selection.append(value)
                                    print(selection)

        return render_template("index.html", selection=selection)
        # Neue Seite wird geöffnet die nur die gewollten Touren anzeigt

    return render_template('kategorisierung.html')
# Code für Auswahl und Darstellung der Touren fertig, Touren die mit Dict. übereinstimmen werden dargestellt
# Code für die Erstellung einer neuen Tour fängt hier an.


@app.route("/add", methods=["GET", "POST"])
def add_new_tour():
    if request.method == "POST":
        name = request.form["Name der Tour"]
        gefahrenstufe = request.form['gefahrenstufe']
        oev = request.form['erreichbarkeit']
        hoehenmeter = request.form['hoehenmeter']
        tiefenmeter = request.form['tiefenmeter']
        dauer = request.form['dauer']
        schwierigkeit = request.form['schwierigkeit']
        # Code welcher vorgibt, wie Eingaben in Data als Dict. abgespeichert werden soll.
        tour = {
            'gefahrenstufe': gefahrenstufe,
            'erreichbarkeit': oev,
            'hoehenmeter': hoehenmeter,
            'tiefenmeter': tiefenmeter,
            'dauer': dauer,
            'schwierigkeit': schwierigkeit,
        }
        abspeichern(name, tour)

    return render_template("neue_tour.html")


# @app.route("/overview", methods=['GET'])
# def overview():
# with open("data.json", "r") as file:
#   data = json.load(file)
#  print(data)
# return render_template("overview.html", seitentitel="Overview", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5550)
