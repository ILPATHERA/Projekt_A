
#Importe
from flask import Flask, render_template, request, jsonify
import onnxruntime
import numpy as np
from PIL import Image
from io import BytesIO

#Flask App erstellen
app = Flask(__name__)

#Endpoint für Prediction
@app.route('/predict', methods=['POST'])
def predict():
    
    #Bild laden und formatieren
    image = Image.open(request.files['image'])
    image = image.resize((224, 224))

    #Bild zu Numpy array umwandeln
    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.transpose(image_array, (2, 0, 1))
    image_array = np.expand_dims(image_array, axis=0)

    #ONNX-Modell laden und Prediction durchführen
    session = onnxruntime.InferenceSession('mobilenetv2-7.onnx')
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    output = session.run([output_name], {input_name: image_array})

    #Prediction aus classification_labels.txt auslesen und ausgeben
    predicted_class = np.argmax(output)
    with open('classification_labels.txt', 'r') as f:
        class_names = [line.strip() for line in f.readlines()]

    #Ausgabe formatieren
    predicted_class = class_names[predicted_class].rstrip(',')
    #print('Predicted class:', predicted_class)
    
    #als JSON ausgeben
    return jsonify({'prediction': predicted_class})

@app.route("/", methods=['GET'])
def indexPage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
