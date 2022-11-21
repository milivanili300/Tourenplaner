from flask import Flask
app = Flask("Rechner")




@app.route('/add/<zahl_0>/<zahl_1>')
def add():
    if request.method == "get":
        return render_template ("rechner.html")
    #msg = "Das Ergebnis ist" + str(int(zahl_0) + 3)+ "!"
    #msg = "Das Ergebnis ist {}!".format(int(zahl_0) + 3)
    #ergebnis= int(zahl_0) + int(zahl_1)
    #msg = f"Das Ergebnis ist {ergebnis}!"
    return "irgendwas ist falsch"


if __name__ == "__main__":
    app.run(debug=True, port=5005)
