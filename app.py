from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('phishing.pkl', 'rb') as file:
    model = pickle.load(file)


def extract_features(url):

    features = [
        url
    ]
    return features


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'error': 'Missing key "url" in request data'}), 400

    url = data['url']
    features = extract_features(url)

    # Make prediction
    y_predict = model.predict(features)

    if y_predict == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"

    return jsonify({'url': url, 'result': result})


if __name__ == '__main__':
    app.run(debug=True)
