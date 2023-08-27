from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/your_route', methods=['POST'])
def your_route():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Check if the 'id' key exists in the JSON data
    if 'id' in data:
        # Get the value of 'id'
        id_value = data['id']

        # Perform any desired operations with the 'id' value
        # For this example, we'll simply return it as a response
        response_data = {'message': f'Received id: {id_value}'}

        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Missing or invalid "id" in the JSON data'}), 400

if __name__ == '__main__':
    app.run(debug=True)

# Make a POST request to the Flask route
flask_url = "http://localhost:5000/your_route"
response = requests.post(flask_url, json={"id": "x"})

# Check the response
if response.status_code == 200:
    print("POST request to Flask was successful")
    print("Response:", response.json())
else:
    print("POST request to Flask failed with status code:", response.status_code)
