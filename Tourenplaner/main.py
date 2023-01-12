from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot

from datenbank import abspeichern, auslesen

app = Flask("Tourenplaner")


@app.route("/", methods=["GET", "POST"])
def start():
    selection = None;

    if request.method == "POST":
        selection = {};
        touren = auslesen()
        dauer = request.form.get("dauer")
        hoehenmeter = request.form.get("hoehenmeter");
        tiefenmeter = request.form.get("tiefenmeter");
        schwierigkeit = request.form.get("schwierigkeit");
        erreichbarkeit = request.form.get("erreichbarkeit");
        gefahrenstufe = request.form.get("gefahrenstufe");

        for key, value in touren.items():
            if value["hoehenmeter"] == hoehenmeter:
                if value["dauer"] == dauer:
                    if value["tiefenmeter"] == tiefenmeter:
                        if value["schwierigkeit"] == schwierigkeit:
                            if value["gefahrenstufe"] == gefahrenstufe:
                                if value["erreichbarkeit"] == erreichbarkeit:
                                    selection[key] = {
                                        "dauer": dauer,
                                        "tiefenmeter": tiefenmeter,
                                        "hoehenmeter": hoehenmeter,
                                        "schwierigkeit": schwierigkeit,
                                        "gefahrenstufe": gefahrenstufe,
                                        "erreichbarkeit": erreichbarkeit
                                    }
    return render_template('kategorisierung.html', selection=selection)

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


@app.route("/overview")
def grafik():
    return "nope"


if __name__ == "__main__":
    app.run(debug=True, port=5550)
