### Mobilenet Image Classification Webapp

In dieser Webapp wird das ONNX-Modell von Mobilenet verwendet. Damit werden Bilder erkannt und klassifiziert.
Die Anwendung ist in Python 3 geschrieben und verwendet Flask als Web-Framework.

## Installation

Erstelle eine virtuelle Umgebung mit Python 3: python3 -m venv venv
Aktiviere die virtuelle Umgebung im Zielordner: source venv/Scripts/activate
Installiere die erforderlichen Pakete: pip install -r requirements.txt

## Verwendung

Starte die Webapp: python app.py
Im Terminal erscheint der Link für das Web, über diesen Link kannst du die Webapp lokal einsehen.
Klicke auf "Bild auswählen" und wähle ein Bild aus, das du klassifizieren möchtest.
Klicke auf "Klassifizieren" und überprüfe das Ergebnis. Die Klasse wird jeweils mit der Zahl der Klasse und der Bezeichnung ausgegeben. Alles Klassen findest du unter der Datei "classification_labels.txt"

## Modelle

Das ONNX-Modell Mobilenet, das für die Bilderkennung und Klassifizierung verwendet wird, ist unter folgendem Link abgelegt:
- https://github.com/onnx/models/tree/main/vision/classification/mobilenet

----------------------------------------------------------------------------------------------------------------------------------------------

03.04.2023
Simone Antonio Sommer 
ZHAW 
Modul: Model Doployment & Maintenance
Dozent: Adrian Moser