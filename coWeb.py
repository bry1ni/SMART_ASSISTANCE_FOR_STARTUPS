import joblib
from flask import Flask, request, jsonify


def predictSuccess(input_array):
    saved_model = joblib.load('businessRater.pkl')
    input_array.pop('category_code')
    successRate = saved_model.predict(input_array)
    return successRate


def estimateFund(success_rate):
    saved_model = joblib.load('fundingEstimer.pkl')
    predicted_funding_total_usd = saved_model.predict([[success_rate]])
    return predicted_funding_total_usd


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract startup_array_info from the request body
        startup_array_info = request.json.get('startup_array_info')

        # Call machine learning functions to process the data
        success_rate = predictSuccess(list(startup_array_info.values()))
        estimated_fund = estimateFund(success_rate)

        return jsonify({'success_rate': success_rate, 'estimated_fund': estimated_fund})

    else:
        # Handle GET requests
        return 'Send a POST request to this endpoint with startup_array_info.'


if __name__ == '__main__':
    app.run(debug=True, port=5500)
