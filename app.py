from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("final_lead_conversion_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = pd.DataFrame([request.json])
    prediction = model.predict(input_data)[0]
    return jsonify({"lead_conversion_prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
