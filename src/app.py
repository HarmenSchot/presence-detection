from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the API endpoint
@app.route('/api/v1/presence-detection', methods=['GET'])
def presence_detection():
    # Extracting query parameters
    user = request.args.get('user', default=None, type=str)
    date = request.args.get('date', default=None, type=str)
    hour = request.args.get('hour', default=None, type=int)
    
    # Here, integrate your prediction logic and return the appropriate response
    # For now, let's return the received parameters as a placeholder
    response = {
        "user": user,
        "date": date,
        "hour": hour,
        "prediction": "Prediction logic will be here"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Running the server in debug mode
