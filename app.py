from flask import Flask, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("DSM_Incentive.csv")
data.columns = data.columns.str.strip()

@app.route('/salesman', methods=['GET'])
def get_salesman_by_contact():
    contact = request.args.get('contact')
    if not contact:
        return "Contact parameter is missing."

    record = data[data['contact'].astype(str) == str(contact)]
    if record.empty:
        return "No data found for this contact."

    row = record.iloc[0]

    # Only extract columns I to AV (columns 8 to 47)
    output_lines = []
    output_lines.append('Salesman Name: ' + str(row['Salesman Name']) if pd.notnull(row['Salesman Name']) else 'Salesman Name: NA')
    output_lines.append('contact: ' + str(row['contact']) if pd.notnull(row['contact']) else 'contact: NA')
    output_lines.append('HO-DSM Type: ' + str(row['HO-DSM Type']) if pd.notnull(row['HO-DSM Type']) else 'HO-DSM Type: NA')
    output_lines.append('Listed Outlet: ' + str(row['Listed Outlet']) if pd.notnull(row['Listed Outlet']) else 'Listed Outlet: NA')
    output_lines.append('New_Outlet_Addition_Tgt: ' + str(row['New_Outlet_Addition_Tgt']) if pd.notnull(row['New_Outlet_Addition_Tgt']) else 'New_Outlet_Addition_Tgt: NA')
    output_lines.append('ECO Target: ' + str(row['ECO Target']) if pd.notnull(row['ECO Target']) else 'ECO Target: NA')
    output_lines.append('ECO_MTD: ' + str(row['ECO_MTD']) if pd.notnull(row['ECO_MTD']) else 'ECO_MTD: NA')
    output_lines.append('ECO_BTD: ' + str(row['ECO_BTD']) if pd.notnull(row['ECO_BTD']) else 'ECO_BTD: NA')
    output_lines.append('Oil_Tgt: ' + str(row['Oil_Tgt']) if pd.notnull(row['Oil_Tgt']) else 'Oil_Tgt: NA')
    output_lines.append('Oil_Vol_MT: ' + str(row['Oil_Vol_MT']) if pd.notnull(row['Oil_Vol_MT']) else 'Oil_Vol_MT: NA')
    output_lines.append('Oil_Ach_Per: ' + str(row['Oil_Ach_Per']) if pd.notnull(row['Oil_Ach_Per']) else 'Oil_Ach_Per: NA')
    output_lines.append('Oil_Ach_Per_Slab: ' + str(row['Oil_Ach_Per_Slab']) if pd.notnull(row['Oil_Ach_Per_Slab']) else 'Oil_Ach_Per_Slab: NA')
    output_lines.append('Oil_Ach_Amount: ' + str(row['Oil_Ach_Amount']) if pd.notnull(row['Oil_Ach_Amount']) else 'Oil_Ach_Amount: NA')
    output_lines.append('Oil_Vol_BTD: ' + str(row['Oil_Vol_BTD']) if pd.notnull(row['Oil_Vol_BTD']) else 'Oil_Vol_BTD: NA')
    output_lines.append('Food_Tgt: ' + str(row['Food_Tgt']) if pd.notnull(row['Food_Tgt']) else 'Food_Tgt: NA')
    output_lines.append('Food_Vol_MT: ' + str(row['Food_Vol_MT']) if pd.notnull(row['Food_Vol_MT']) else 'Food_Vol_MT: NA')
    output_lines.append('Food_Ach_Per: ' + str(row['Food_Ach_Per']) if pd.notnull(row['Food_Ach_Per']) else 'Food_Ach_Per: NA')
    output_lines.append('Food_Ach_Per_Slab: ' + str(row['Food_Ach_Per_Slab']) if pd.notnull(row['Food_Ach_Per_Slab']) else 'Food_Ach_Per_Slab: NA')
    output_lines.append('Food_Ach_Amount: ' + str(row['Food_Ach_Amount']) if pd.notnull(row['Food_Ach_Amount']) else 'Food_Ach_Amount: NA')
    output_lines.append('Food_Vol_BTD: ' + str(row['Food_Vol_BTD']) if pd.notnull(row['Food_Vol_BTD']) else 'Food_Vol_BTD: NA')
    output_lines.append('Total_Vol_MT: ' + str(row['Total_Vol_MT']) if pd.notnull(row['Total_Vol_MT']) else 'Total_Vol_MT: NA')
    output_lines.append('Perfect_Store: ' + str(row['Perfect_Store']) if pd.notnull(row['Perfect_Store']) else 'Perfect_Store: NA')
    output_lines.append('Perfect_Store_Amount: ' + str(row['Perfect_Store_Amount']) if pd.notnull(row['Perfect_Store_Amount']) else 'Perfect_Store_Amount: NA')
    output_lines.append('Perfect_Store_Criteria: ' + str(row['Perfect_Store_Criteria']) if pd.notnull(row['Perfect_Store_Criteria']) else 'Perfect_Store_Criteria: NA')
    output_lines.append('Super_Charge_Product: ' + str(row['Super_Charge_Product']) if pd.notnull(row['Super_Charge_Product']) else 'Super_Charge_Product: NA')
    output_lines.append('Super_Charge_Product_PDO: ' + str(row['Super_Charge_Product_PDO']) if pd.notnull(row['Super_Charge_Product_PDO']) else 'Super_Charge_Product_PDO: NA')
    output_lines.append('Super_Charge_No_of_Product: ' + str(row['Super_Charge_No_of_Product']) if pd.notnull(row['Super_Charge_No_of_Product']) else 'Super_Charge_No_of_Product: NA')
    output_lines.append('Super_Charge_Tgt: ' + str(row['Super_Charge_Tgt']) if pd.notnull(row['Super_Charge_Tgt']) else 'Super_Charge_Tgt: NA')
    output_lines.append('Super_Charge_Ach: ' + str(row['Super_Charge_Ach']) if pd.notnull(row['Super_Charge_Ach']) else 'Super_Charge_Ach: NA')
    output_lines.append('Super_Charge_Ach_Per: ' + str(row['Super_Charge_Ach_Per']) if pd.notnull(row['Super_Charge_Ach_Per']) else 'Super_Charge_Ach_Per: NA')
    output_lines.append('Super_Charge_Ach_Per_Slab: ' + str(row['Super_Charge_Ach_Per_Slab']) if pd.notnull(row['Super_Charge_Ach_Per_Slab']) else 'Super_Charge_Ach_Per_Slab: NA')
    output_lines.append('Super_Charge_Ach_Amount: ' + str(row['Super_Charge_Ach_Amount']) if pd.notnull(row['Super_Charge_Ach_Amount']) else 'Super_Charge_Ach_Amount: NA')
    output_lines.append('Super_Charge_BTD: ' + str(row['Super_Charge_BTD']) if pd.notnull(row['Super_Charge_BTD']) else 'Super_Charge_BTD: NA')
    output_lines.append('Manday: ' + str(row['Manday']) if pd.notnull(row['Manday']) else 'Manday: NA')
    output_lines.append('ASE Name: ' + str(row['ASE Name']) if pd.notnull(row['ASE Name']) else 'ASE Name: NA')
    output_lines.append('ASE Emp Code: ' + str(row['ASE Emp Code']) if pd.notnull(row['ASE Emp Code']) else 'ASE Emp Code: NA')
    output_lines.append('ASM Name: ' + str(row['ASM Name']) if pd.notnull(row['ASM Name']) else 'ASM Name: NA')
    output_lines.append('ASM Emp Code: ' + str(row['ASM Emp Code']) if pd.notnull(row['ASM Emp Code']) else 'ASM Emp Code: NA')
    output_lines.append('RSM Name: ' + str(row['RSM Name']) if pd.notnull(row['RSM Name']) else 'RSM Name: NA')
    output_lines.append('RSM Emp Code: ' + str(row['RSM Emp Code']) if pd.notnull(row['RSM Emp Code']) else 'RSM Emp Code: NA')

    response_text = "\n".join(output_lines)
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
