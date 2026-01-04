import pandas as pd
import numpy as np
import os

def generate_dashboard_data():
    """
    This function aims to:
    1. Retrieve existing university data.
    2. Calculate/Simulate final SCORES for 6 UI GreenMetric categories.
    3. Perform UNPIVOT (Melt) data so it can be read by Tableau Radar Chart.
    """
    
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, '..', 'data', 'clean_stage_1.csv')
    output_path = os.path.join(base_dir, '..', 'data', 'dashboard_ready_data.csv')
    
    print(f"Reading data from: {input_path}")
    df = pd.read_csv(input_path)
    
    np.random.seed(123)
    
    df_scores = df[['University_ID']].copy()
    
    df_scores['Setting & Infra (SI)'] = np.random.randint(800, 1500, size=len(df))
    
    df_scores['Energy (EC)'] = np.random.randint(1000, 2100, size=len(df))
    
    df_scores['Waste (WS)'] = np.random.randint(800, 1800, size=len(df))
    
    df_scores['Water (WR)'] = np.random.randint(500, 1000, size=len(df))
    
    df_scores['Transportation (TR)'] = np.random.randint(800, 1800, size=len(df))
    
    df_scores['Education (ED)'] = np.random.randint(900, 1800, size=len(df))
    
    df_scores['Total_Score'] = df_scores.sum(axis=1, numeric_only=True)
    
    df_scores['National_Rank'] = df_scores['Total_Score'].rank(ascending=False).astype(int)
    
    print("\n[PREVIEW] Score Data (Wide Format):")
    print(df_scores.head(3))
    
    radar_columns = [
        'Setting & Infra (SI)', 'Energy (EC)', 'Waste (WS)', 
        'Water (WR)', 'Transportation (TR)', 'Education (ED)'
    ]
    
    df_long = df_scores.melt(
        id_vars=['University_ID', 'Total_Score', 'National_Rank'],
        value_vars=radar_columns,
        var_name='Category',
        value_name='Score'
    )
    
    max_scores = {
        'Setting & Infra (SI)': 1500,
        'Energy (EC)': 2100,
        'Waste (WS)': 1800,
        'Water (WR)': 1000,
        'Transportation (TR)': 1800,
        'Education (ED)': 1800
    }
    
    df_long['Max_Score'] = df_long['Category'].map(max_scores)
    
    print("\n[PREVIEW] Tableau-Ready Data (Long Format):")
    print(df_long.head(6))
    
    df_long.to_csv(output_path, index=False)
    print(f"\n[SUCCESS] Dashboard file ready at: {output_path}")

if __name__ == "__main__":
    generate_dashboard_data()