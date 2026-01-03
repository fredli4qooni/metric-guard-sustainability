import pandas as pd
import numpy as np
import random
import os

np.random.seed(42)

def generate_dummy_data(num_rows=50):
    """
    Creating a dummy dataset for the GreenMetric UI simulation.
    Includes clean data and data with intentional errors.
    """
    
    data = []
    
    for i in range(1, num_rows + 1):
        univ_id = f"UNIV_{i:03d}"
        
        si_1_total_area = random.randint(100000, 5000000)
        
        si_2_forest = int(si_1_total_area * random.uniform(0.2, 0.4))
        
        si_3_planted = int(si_1_total_area * random.uniform(0.1, 0.2))
        
        populasi = random.randint(5000, 30000)
        ec_4_electricity = populasi * random.uniform(100, 500) 
        
        evidence_link = f"https://drive.google.com/file/d/{univ_id}"
        
        if i in [5, 15, 25]:
            si_2_forest = int(si_1_total_area * 1.5) 
            notes = "Logic Error: Forest > Total Area"
            
        elif i in [10, 20]:
            ec_4_electricity = ec_4_electricity * 1000
            notes = "Unit Error: Extreme Outlier (Watt?)"
            
        elif i == 30:
            ec_4_electricity = f"{int(ec_4_electricity)},00" 
            notes = "Format Error: Comma usage"
            
        elif i == 40:
            evidence_link = np.nan
            notes = "Compliance Error: Missing Evidence"
            
        else:
            notes = "Valid Data"

        row = {
            'University_ID': univ_id,
            'SI_1_Total_Area': si_1_total_area,
            'SI_2_Forest_Area': si_2_forest,
            'SI_3_Planted_Area': si_3_planted,
            'EC_4_Electricity_Usage': ec_4_electricity,
            'Evidence_Link': evidence_link,
            'Debug_Notes': notes
        }
        data.append(row)

    df = pd.DataFrame(data)
    
    return df

print("Generating Dummy Data...")
df_dummy = generate_dummy_data(50)

output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True) # Buat folder jika belum ada
filename = os.path.join(output_dir, "raw_greenmetric_data.csv")
df_dummy.to_csv(filename, index=False)

print(f"Success! File '{filename}' has been created with {len(df_dummy)} rows data.")
print("Check the file to see 'Logic Error' in line UNIV_005 and 'Unit Error' in UNIV_010.")