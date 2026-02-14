from flask import Flask, render_template, request
import numpy as np
import pickle
import json

app = Flask(__name__)

# ================= LOAD MODELS =================

with open('KNN.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('Navis.pkl', 'rb') as f:
    nb_model = pickle.load(f)

# ================= LOAD METRICS =================

with open('train_knn.json') as f:
    train_knn = json.load(f)

with open('test_knn.json') as f:
    test_knn = json.load(f)

with open('train_Navia.json') as f:
    train_nb = json.load(f)

with open('test_Navia.json') as f:
    test_nb = json.load(f)

# ================= FLOWER LABELS =================

flower_names = {
    0: "Iris Setosa",
    1: "Iris Versicolor",
    2: "Iris Virginica"
}

# ================= HOME ROUTE =================

@app.route('/')
def home():
    return render_template("index.html")

# ================= PREDICT ROUTE =================

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get form values
        values = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]

        model_type = request.form['modelType']
        features = np.array([values])

        # Select model
        if model_type == "KNN":
            prediction = knn_model.predict(features)[0]
            train_data = train_knn
            test_data = test_knn
        else:
            prediction = nb_model.predict(features)[0]
            train_data = train_nb
            test_data = test_nb

        flower = flower_names[int(prediction)]

        return render_template(
            "index.html",
            prediction_text=flower,
            train_accuracy=train_data.get("Accuracy_Score"),
            test_accuracy=test_data.get("Accuracy_Score"),
            train_report=train_data.get("Classification_report"),
            test_report=test_data.get("Classification_report"),
            train_cm=train_data.get("Confusion_matrix"),
            test_cm=test_data.get("Confusion_matrix")
        )

    except Exception as e:
        return render_template("index.html", prediction_text="Error occurred")

# ================= RUN APP =================

if __name__ == "__main__":
    app.run(debug=True)
