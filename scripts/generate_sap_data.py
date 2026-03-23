import pandas as pd
import numpy as np

def generate_sap():
    projects = 50
    data = {
        'WBS_Element': [f'ZA-P{i:03}' for i in range(projects)],
        'Budget': np.random.randint(100000, 5000000, size=projects),
        'Actuals': np.random.randint(50000, 5500000, size=projects), # Some over budget
        'Commitments': np.random.randint(10000, 50000, size=projects)
    }
    df = pd.DataFrame(data)
    # Calculate Variance logic for the CSV
    df['Variance'] = df['Budget'] - (df['Actuals'] + df['Commitments'])
    df.to_csv('data/raw_sap_export.csv', index=False)
    print("✅ SAP Seed Data Created.")

if __name__ == "__main__":
    generate_sap()
