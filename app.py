from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load data when the app starts
data = pd.read_csv("DSM_Incentive.csv")

@app.route('/salesman', methods=['GET'])
def get_salesman_by_contact():
    contact = request.args.get('contact')
    if not contact:
        return jsonify({'error': 'Missing required parameter: contact'}), 400

    # Search using 'Contact' column
    record = data[data['Contact'].astype(str) == str(contact)]

    if record.empty:
        return jsonify({'error': 'Contact not found'}), 404

    row = record.iloc[0]

    def safe_cast(value, cast_type):
        return cast_type(value) if pd.notnull(value) else None

    response = {
        'Contact': str(row['Contact']),
        'Salesman Code': str(row['Salesman Code']),
        'Listed_Outlets': safe_cast(row['Listed_Outlets'], int),
        'New_Outlet_Addition_Tgt': safe_cast(row['New_Outlet_Addition_Tgt'], int),
        'Mandays': safe_cast(row['Mandays'], int),
        'Gate_Way_ECO_30': safe_cast(row['Gate_Way_ECO_30'], str),
        'ECO_MTD': safe_cast(row['ECO_MTD'], str),
        'BTD_ECO_30': safe_cast(row['BTD_ECO_30'], int),
        'Oil_Tgt_': safe_cast(row['Oil_Tgt_'], int),
        'Oil_Vol(MT)': safe_cast(row['Oil_Vol(MT)'], str),
        'Oil_Ach': safe_cast(row['Oil_Ach'], str),
        'Oil_Ach_Slab': safe_cast(row['Oil_Ach_Slab'], str),
        'Oil_Amount': safe_cast(row['Oil_Amount'], int),
        'Oil_Next_Slab': safe_cast(row['Oil_Next_Slab'], str),
        'BTD_Oil_Next_Slab': safe_cast(row['BTD_Oil_Next_Slab'], int),
        'BTD_Oil_Next_Slab_Amount': safe_cast(row['BTD_Oil_Next_Slab_Amount'], int),
        'BTD_Oil_Vol_Max_Slab': safe_cast(row['BTD_Oil_Vol_Max_Slab'], int),
        'BTD_Oil_Vol_Max_Amount': safe_cast(row['BTD_Oil_Vol_Max_Amount'], int),
        'Food_Tgt_': safe_cast(row['Food_Tgt_'], int),
        'Food_Vol(MT)': safe_cast(row['Food_Vol(MT)'], str),
        'Food_Ach': safe_cast(row['Food_Ach'], str),
        'Food_Ach_Slab': safe_cast(row['Food_Ach_Slab'], str),
        'Food_Amount': safe_cast(row['Food_Amount'], int),
        'Food_Next_Slab': safe_cast(row['Food_Next_Slab'], str),
        'BTD_Food_Next_Slab_Amount': safe_cast(row['BTD_Food_Next_Slab_Amount'], int),
        'BTD_Food_Next_Slab': safe_cast(row['BTD_Food_Next_Slab'], int),
        'BTD_Food_Vol': safe_cast(row['BTD_Food_Vol'], int),
        'BTD_Food_Vol_Max_Amount': safe_cast(row['BTD_Food_Vol_Max_Amount'], int),
        'Total_Tgt': safe_cast(row['Total_Tgt'], int),
        'Total_Vol(MT)': safe_cast(row['Total_Vol(MT)'], str),
        'Total_Ach': safe_cast(row['Total_Ach'], str),
        'Perfect_Store_MTD': safe_cast(row['Perfect_Store_MTD'], str),
        'Perfect_Store_Amount': safe_cast(row['Perfect_Store_Amount'], int),
        'Super_Charge_Tgt': safe_cast(row['Super_Charge_Tgt'], int),
        'Super_Charge_Ach': safe_cast(row['Super_Charge_Ach'], str),
        'Super_Charge_Ach_Per': safe_cast(row['Super_Charge_Ach_Per'], str),
        'Super_Charge_Ach_Slab': safe_cast(row['Super_Charge_Ach_Slab'], str),
        'Super_Charge_Amount': safe_cast(row['Super_Charge_Amount'], int),
        'Super_charge_Next_Slab': safe_cast(row['Super_charge_Next_Slab'], str),
        'BTD_Super_Charge_Next_Slab': safe_cast(row['BTD_Super_Charge_Next_Slab'], int)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
