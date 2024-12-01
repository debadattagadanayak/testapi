from flask import Flask, request, jsonify

app = Flask(__name__)

cost_centers = {
    "1001": {"description": "ULIS Business Team", "status": "ACTIVE"},
    "1002": {"description": "Finance Department", "status": "INACTIVE"},
    "1003": {"description": "HR Team", "status": "ACTIVE"}
}

@app.route('/validate-costcenter', methods=['GET'])
def validate_costcenter():
    cost_center_code = request.args.get('costCenterCode')
    if not cost_center_code:
        return jsonify({"error": "1", "message": "Missing costCenterCode parameter"}), 400

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
        return jsonify({"error": "1", "message": "Invalid cost center code"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
