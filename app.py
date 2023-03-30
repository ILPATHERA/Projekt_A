from flask import Flask, render_template, request, jsonify
import onnxruntime
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    
    # Load the image and resize it
    image = Image.open(request.files['image'])
    image = image.resize((224, 224))

    # Convert the image to a numpy array
    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.transpose(image_array, (2, 0, 1))
    image_array = np.expand_dims(image_array, axis=0)

    # Load the ONNX model and run inference
    session = onnxruntime.InferenceSession('mobilenetv2-7.onnx')
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    output = session.run([output_name], {input_name: image_array})

    # Get the predicted class and print the output
    predicted_class = np.argmax(output)

    with open('classification_labels.txt', 'r') as f:
        class_names = [line.strip() for line in f.readlines()]

    predicted_class = class_names[predicted_class]    

    #print('Predicted class:', predicted_class)
    return jsonify({'prediction': predicted_class})

@app.route("/", methods=['GET'])
def indexPage():
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def classify():
    # Call predict function to get the prediction
    predicted_class = predict().get_json()['prediction']
    return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
