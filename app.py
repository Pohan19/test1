from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    return jsonify({'message': 'Welcome to the API!'}), 200

if __name__ == '__main__':
    app.run(debug=True)