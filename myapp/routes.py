from flask import Flask, request, jsonify, Blueprint
import requests

main = Blueprint('main', __name__)

@main.route('/attendance', methods=['POST'])
def your_route():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Check if the 'id' key exists in the JSON data
    if 'id' in data:
        # Get the value of 'id'
        id_value = data['id']

        # Form the URL for the external API with the 'id' value
        external_api_url = f'http://goldberg.pythonanywhere.com/api/attendances/record/2?id={id_value}'

        # Send a POST request to the external API without a request body
        response = requests.post(external_api_url)

        if response.status_code == 200:
            return jsonify({'message': f'Successfully recorded attendance for id: {id_value}'}), 200
        else:
            return jsonify({'error': f'Failed to record attendance for id: {id_value}'}), 500
    else:
        return jsonify({'error': 'Missing or invalid "id" in the JSON data'}), 400
