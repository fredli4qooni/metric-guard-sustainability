import pandas as pd
import numpy as np
import os

from clean_data import load_and_clean_data

def run_validation_engine(df):
    """
    The core of MetricGuard. This function performs a series of logical and statistical checks
    on the cleaned data.
    """
    
    print("\n--- 3. Running Validation Logic ---")
    
    validation_flags = []
    
    for index, row in df.iterrows():
        total_green_area = row['SI_2_Forest_Area'] + row['SI_3_Planted_Area']
        
        if total_green_area > row['SI_1_Total_Area']:
            validation_flags.append({
                'University_ID': row['University_ID'],
                'Error_Type': 'Logic Error',
                'Message': f"Total Green Area ({total_green_area} m2) exceeds Total Campus Area ({row['SI_1_Total_Area']} m2)",
                'Priority': 'High'
            })
    
    mean_ec = df['EC_4_Electricity_Usage'].mean()
    std_ec = df['EC_4_Electricity_Usage'].std()
    
    print(f"[STATS] Electricity Average: {mean_ec:.2f} | Std Dev: {std_ec:.2f}")
    
    df['Z_Score_EC'] = (df['EC_4_Electricity_Usage'] - mean_ec) / std_ec
    
    outliers = df[np.abs(df['Z_Score_EC']) > 3]
    
    for index, row in outliers.iterrows():
        validation_flags.append({
            'University_ID': row['University_ID'],
            'Error_Type': 'Unit Error (Outlier)',
            'Message': f"Electricity usage is statistically improbable (Z-Score: {row['Z_Score_EC']:.2f}). Check for Watt vs kWh error.",
            'Priority': 'Critical'
        })
    
    missing_evidence = df[df['Evidence_Link'].isnull()]
    
    for index, row in missing_evidence.iterrows():
        validation_flags.append({
            'University_ID': row['University_ID'],
            'Error_Type': 'Compliance Error',
            'Message': "Evidence Link is missing.",
            'Priority': 'Medium'
        })

    df_flags = pd.DataFrame(validation_flags)
    
    return df_flags

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, '..', 'data', 'raw_greenmetric_data.csv')
    
    output_dir = os.path.join(base_dir, '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "Final_Validation_Report.xlsx")

    print(f"Reading data from: {input_path}")
    df_clean = load_and_clean_data(input_path)
    
    df_report = run_validation_engine(df_clean)
    
    if not df_report.empty:
        print(df_report[['University_ID', 'Error_Type', 'Message']].to_string(index=False))
        
        df_report.to_excel(report_path, index=False)
        print(f"\n[SUCCESS] report detail save as: {report_path}")