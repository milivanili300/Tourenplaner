from flask import Flask
from flask import render_template

import random

app = Flask("Hello World")


@app.route('/hello_all')
def hello_world():
    auswahl = ["Limena", "Anna", "Sabrina", "Hannah"]
    ausgewaehlter_name = random.choice(auswahl)
    return render_template('hello_all.html', alle_namen=auswahl)


@app.route('/hallo')
def hallo_welt():
    return 'Hallo, Welt!>'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
