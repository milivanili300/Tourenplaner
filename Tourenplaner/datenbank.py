import json
#Funktion welche das Auslesen der Touren ermöglicht
def auslesen(name, tour):
    with open("data.json", "r") as open_file:
        inhalt = json.load(open_file)
    return inhalt


# Funktion welche ermöglicht, neue Touren in das Json file abzuspeichern
def abspeichern( name, tour):
    current_content = auslesen(name, tour)
    current_content[name] = tour
    with open("data.json", "w", encoding="utf8") as open_file:
        json.dump(current_content, open_file, indent=4)
