from flask import Flask
from flask_cors import CORS
from transformers import pipeline
import os

app = Flask(__name__)
CORS(app) 

summarizer = pipeline("summarization")

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
