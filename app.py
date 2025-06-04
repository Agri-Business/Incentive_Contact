from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV data
df = pd.read_csv("DSM_Incentive.csv")
df.columns = df.columns.str.strip()

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    contact = request.args.get('Contact')

    if not contact:
        return jsonify({'error': 'Contact parameter is required'}), 400

    try:
        result = df[df['Contact'].astype(str) == str(contact)]

        if result.empty:
            return jsonify({'message': 'No data found for this contact'}), 404

        output = result.to_dict(orient='records')
        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
