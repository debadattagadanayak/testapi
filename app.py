from flask import Flask, jsonify

app = Flask(__name__)

# Cost center data
cost_centers = {
    "1001": {"description": "ULIS Business Team", "status": "ACTIVE"},
    "1002": {"description": "Finance Department", "status": "INACTIVE"},
    "1003": {"description": "HR Team", "status": "ACTIVE"}
}

# Define the root route
@app.route('/')
def home():
    return 'Welcome to the API! Use /validate/<cost_center_code> to validate cost center codes.'

# Handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content for favicon requests

# Endpoint to validate cost center codes
@app.route('/validate/<cost_center_code>')
def validate_cost_center(cost_center_code):
    cost_center = cost_centers.get(cost_center_code)
    if cost_center:
        return jsonify({
            "error": "0",
            "message": "Valid cost center",
            "costCenter": {
                "code": cost_center_code,
                "description": cost_center["description"],
                "status": cost_center["status"]
            }
        })
    else:
        return jsonify({
            "error": "1",
            "message": "Invalid cost center"
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
