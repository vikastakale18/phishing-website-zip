from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get("url", "")

    # Dummy logic (replace with actual ML model if needed)
    if "login" in url or "bank" in url:
        result = "phishing"
    else:
        result = "legitimate"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
