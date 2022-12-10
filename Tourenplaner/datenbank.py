
def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def touren_laden():
    #test2
    touren = auslesen()
    touren_liste = touren.split("\n")
    neue_liste = []
    for eintrag in touren_liste:
        aufgabe, deadline = eintrag.split(",")
        neue_liste.append([aufgabe, deadline])
    return neue_liste


def abspeichern(aufgabe, deadline):
    current_content = auslesen()
    new_content = current_content + f"\n{aufgabe},{deadline}"
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)
