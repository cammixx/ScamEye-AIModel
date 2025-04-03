from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Simulates a machine learning prediction for link risk.
    """
    try:
        data = request.get_json()
        url = data['url']

        # Replace this with your actual ML model prediction
        # For now, we'll simulate a random risk percentage
        import random
        risk_percent = random.randint(0, 100)

        return jsonify({'riskPercent': risk_percent})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')