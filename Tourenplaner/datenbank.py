import json
def auslesen():
    with open("data.json", "r") as open_file:
        inhalt = json.load(open_file)
    return inhalt



def abspeichern( name, tour):
    current_content = auslesen()
    current_content[name] = tour
    with open("data.json", "w", encoding="utf8") as open_file:
        json.dump(current_content, open_file, indent=4)
