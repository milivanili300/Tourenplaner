import json

from flask import Flask
from flask import render_template
from flask import request
from datenbank import abspeichern

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
        # Code, welcher die Daten mit Kategorisierung abgleicht.
        with open("data.json") as datei:
            vorschlag = json.load(datei)
        # leere Liste für die Touren welche mit der gesetzten Auswahl übereinstimmt, wird erstellt
        selection = []
        # gegenprüfung jeder Eingabe mit Json datei welche bestehende Touren beinhaltet.
        for key, value in vorschlag.items():
            if hoehenmeter == value["hoehenmeter"]:
                if dauer == value["dauer"]:
                    if tiefenmeter == value["tiefenmeter"]:
                        if schwierigkeit == value["schwierigkeit"]:
                            if gefahrenstufe == value["gefahrenstufe"]:
                                if erreichbarkeit == value["erreichbarkeit"]:
                                    # wenn die ausgewählten Eigenschaften mit den Touren übereinstimmen werden
                                    # sie in die Liste selection gespeichert
                                    selection.append(key)
                                    selection.append(value)
        return render_template("index.html", liste=selection)
        # Neue Seite wird geöffnet die nur die übereinstimmenden Touren anzeigt

    return render_template('kategorisierung.html')


# Code für Auswahl und Darstellung der Touren fertig, Touren die mit Dict. übereinstimmen werden dargestellt
# Code für die Erstellung einer neuen Tour fängt hier an.


@app.route("/add", methods=["GET", "POST"])
def add_new_tour():
    if request.method == "POST":
        # Eigentlich wie bei der Tour aussuchen, können die Eigenschaften der Tour angegeben werden.
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
        # durch die in datenbank.py definierte Funktion, wird die Tour und der Name in Json mit den restlichen Touren
        # abgespeichert.
        abspeichern(name, tour)
    # neue_tour.html wird nach jedem abspeichern wieder geöffnet, damit weitere Touren eingeben werden können.
    return render_template("neue_tour.html")


if __name__ == "__main__":
    app.run(debug=True, port=5550)
