from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET"])
def home():
    return open("index.html").read()

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["review"]
    result = classifier(text)[0]["label"]
    html = open("index.html").read()
    return html.replace("{{result}}", result)

if __name__ == "__main__":
    app.run(debug=True)