import pandas as pd

def clean_superstore(data_path, output_path):
    """Load and clean the Superstore dataset."""
    df = pd.read_csv(data_path)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert data types
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # Create derived columns
    df['Profit Margin'] = df['Profit'] / df['Sales']
    df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    df = clean_superstore("data/superstore.csv", "outputs/cleaned_superstore.csv")
    print(f"Cleaned data shape: {df.shape}")