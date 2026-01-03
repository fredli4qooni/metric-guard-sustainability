import pandas as pd
import numpy as np
import os

def load_and_clean_data(filepath):
    """
    Function to load raw data and perform standard format cleaning.
    Focus: Addressing decimal comma (European/Indonesian) vs. decimal point (US/Python) issues.
    """
    
    print(f"--- 1. Loading Data from {filepath} ---")
    df = pd.read_csv(filepath)
    
    print("\n[INFO] Initial Data Type:")
    print(df.dtypes)
    
    print("\n--- 2. Cleaning Process Started ---")
    
    numeric_cols = ['SI_1_Total_Area', 'SI_2_Forest_Area', 'SI_3_Planted_Area', 'EC_4_Electricity_Usage']
    
    for col in numeric_cols:
        if df[col].dtype == 'object':
            print(f"[FIX]  Clearing column formatting: {col}")
            
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
            
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    print("\n[INFO] Data Types After Cleaning:")
    print(df.dtypes)
    
    check_univ_30 = df[df['University_ID'] == 'UNIV_030']['EC_4_Electricity_Usage'].values[0]
    print(f"\n[VERIFICATION] The EC_4 value for UNIV_030 is now: {check_univ_30} (Type: {type(check_univ_30)})")
    
    return df

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, '..', 'data', 'raw_greenmetric_data.csv')
    output_path = os.path.join(base_dir, '..', 'data', 'clean_stage_1.csv')

    df_clean = load_and_clean_data(data_path)
    
    df_clean.to_csv(output_path, index=False)