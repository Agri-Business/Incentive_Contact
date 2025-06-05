from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

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

        row = result.iloc[0]

        output = {col: row[col] for col in [
            'Listed_Outlets', 'New_Outlet_Addition_Tgt', 'Mandays', 'Gate_Way_ECO_30', 'ECO_MTD', 'BTD_ECO_30',
            'Oil_Tgt_', 'Oil_Vol(MT)', 'Oil_Ach', 'Oil_Ach_Slab', 'Oil_Amount', 'Oil_Next_Slab',
            'BTD_Oil_Next_Slab', 'BTD_Oil_Next_Slab_Amount', 'BTD_Oil_Vol_Max_Slab', 'BTD_Oil_Vol_Max_Amount',
            'Food_Tgt_', 'Food_Vol(MT)', 'Food_Ach', 'Food_Ach_Slab', 'Food_Amount', 'Food_Next_Slab',
            'BTD_Food_Next_Slab_Amount', 'BTD_Food_Next_Slab', 'BTD_Food_Vol', 'BTD_Food_Vol_Max_Amount',
            'Total_Tgt', 'Total_Vol(MT)', 'Total_Ach', 'Perfect_Store_MTD', 'Perfect_Store_Amount',
            'Super_Charge_Tgt', 'Super_Charge_Ach', 'Super_Charge_Ach_Per', 'Super_Charge_Ach_Slab',
            'Super_Charge_Amount', 'Super_charge_Next_Slab'
        ]}

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
