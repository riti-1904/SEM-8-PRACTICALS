import pandas as pd
import os

# Paths
input_path = "data/sample_data.csv"
output_path = "output/transformed_data.csv"

def extract():
    print("Extracting data...")
    df = pd.read_csv(input_path)
    return df

def transform(df):
    print("Transforming data...")
    df = df.dropna(subset=['Salary'])  # Remove rows with missing Salary
    df['Department'].fillna('Unknown', inplace=True)
    df['Salary'] = df['Salary'].astype(float)
    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])
    df['Experience_Years'] = pd.Timestamp('2025-01-01').year - df['Joining_Date'].dt.year
    return df

def load(df):
    print("Loading data...")
    os.makedirs("output", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data loaded into {output_path}")

def run_etl():
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

if __name__ == "__main__":
    run_etl()
