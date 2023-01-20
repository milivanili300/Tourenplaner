Problembeschreibung/Motivation
Die Motivation für dieses Projekt war es, ein Projekt zu kreieren welches möglich macht, meine Programmierkenntnisse zu verbessern und gleichzeitig ein Programm zu schreiben welches ich gerne zum Nutzen hätte. Das Projekt löst in dem Sinn also weniger ein Problem, sondern mehr ein persönliches Bedürfnis. Es soll eine Art Katalog oder Sammelstelle für potenzielle Skitourenroute sein. Das Ziel ist, dass eine Auswahl von Routen definiert und nach verschiedenen Aspekten kategorisiert werden. Diese sind Dauer, Höhenmeter, Tiefenmeter, technische Schwierigkeit, Gefahrenstufe und ob die Tour mit der ÖV erreichbar ist oder nicht. Das Projekt ermöglicht es somit den Nutzenden, einzugeben, welche Art von Skitour gemacht werden will, also wie lange sie Zeit haben und welche Art von Route sie machen möchten. Danach kann ihnen das Programm alle möglichen Routen vorschlagen. 


Betrieb
Damit das Programm funktioniert braucht es ausser Flask keine zusätzlichen Pakete. Zur Ausführung der Anwendung muss somit nichts beachtet werden, ausser, dass das erwähnte Paket welches benötigt wird installiert ist. 
  
Zum richtigen Ausführen der Anwendung muss die mit main.py betitelte Date ausgeführt werden. Diese wird den Tourenplaner richtig starten. 

Benutzung
Wie bereits in der Problembeschreibung erwähnt, kann zur Benutzung der Anwendung Kriterien angewählt werden, welche wiederum mit der existierenden Datenbank in Form eines Json abgespeichert ist, abgeglichen werden. Sofern eine übereinstimmende Tour existiert, wird diese angezeigt. Falls dies nicht der Fall sein soll, kann die Anwenderin oder der Anwender es unendliche Male erneut versuchen oder hat auch die Möglichkeit eigene Touren hinzuzufügen. Der genaue Ablauf wird im nächsten Abschnitt erläutert.  

Architektur
<img src="C:\Users\milen\OneDrive\Desktop\FHGR\DBM_HS22\Prog2\pro2_projekt\Tourenplaner\images\Ablaufdiagramm_Tourenplaner.png"/>

Ungelöste/unbearbeitete Probleme
Nicht gelöst werden konnte, dass die Touren schön formatiert und nicht als Dictionary dargestellt werden. Ebenfalls wäre es das Ziel gewesen, dass wenn keine Tour gefunden wurde, die Seite keine_Tour.html aufgestartet wird. Von da aus war das Ziel wiederum auf die Startseite oder auf eigene Tour erstellen navigiert werden könnte. Dies ist im Moment nicht der Fall. 
Obwohl ich sehr zufrieden bin mit dem Programm, sehe ich viele Verbesserungs- und Ausbaumöglichkeiten. Verbesserungspotential wäre beispielsweise die Implementierung der Route in Form einer Karte und einen Button, den man setzen kann, sobald die Tour auch gemacht wurde. Dazu wäre es naheliegend eine weitere Seite zu erstellen auf welcher eine Grafik ist. Auf dieser könnte man sehen, wie viele Touren bereits erledigt wurden und wie viel Höhen und Tiefenmeter insgesamt absolviert wurden. Zusätzlich würde ich gerne das Design noch verbessern damit die Anwendung auch einfacher zu bedienen ist für den User.
