"""
Data Preprocessing Module
Handles data cleaning, transformation, and preparation
"""

import pandas as pd
import numpy as np
from typing import Tuple

class DataPreprocessor:
    """Class for handling data preprocessing tasks"""
    
    def __init__(self):
        self.processed_data = None
        
    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Load dataset from CSV file
        
        Parameters:
        -----------
        filepath : str
            Path to CSV file
            
        Returns:
        --------
        pd.DataFrame
            Loaded dataframe
        """
        try:
            df = pd.read_csv(filepath)
            print(f"✅ Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
            return df
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the dataset by handling missing values and outliers
        
        Parameters:
        -----------
        df : pd.DataFrame
            Raw dataframe
            
        Returns:
        --------
        pd.DataFrame
            Cleaned dataframe
        """
        df_clean = df.copy()
        
        # Handle missing values
        if 'Income' in df_clean.columns:
            df_clean['Income'] = df_clean['Income'].fillna(df_clean['Income'].median())
        
        # Convert date columns
        date_cols = [col for col in df_clean.columns 
                    if 'date' in col.lower() or 'dt' in col.lower()]
        
        for col in date_cols:
            try:
                df_clean[col] = pd.to_datetime(df_clean[col], dayfirst=True)
            except:
                pass
        
        print(f"✅ Data cleaned: {df_clean.isnull().sum().sum()} missing values remaining")
        return df_clean
    
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create new features for analysis
        
        Parameters:
        -----------
        df : pd.DataFrame
            Cleaned dataframe
            
        Returns:
        --------
        pd.DataFrame
            Dataframe with new features
        """
        df_features = df.copy()
        
        # Create total spending feature
        spending_cols = [col for col in df_features.columns if 'Mnt' in col]
        if spending_cols:
            df_features['Total_Spending'] = df_features[spending_cols].sum(axis=1)
        
        # Create total purchases feature
        purchase_cols = [col for col in df_features.columns if 'Num' in col and 'Purchases' in col]
        if purchase_cols:
            df_features['Total_Purchases'] = df_features[purchase_cols].sum(axis=1)
        
        # Create engagement score
        if 'Total_Spending' in df_features.columns and 'Total_Purchases' in df_features.columns:
            df_features['Engagement_Score'] = (
                df_features['Total_Spending'] * df_features['Total_Purchases']
            ) / 1000
        
        print(f"✅ Features created: {len(df_features.columns)} total columns")
        return df_features

# Example usage
if __name__ == "__main__":
    print("🧹 Data Preprocessing Module")
    print("-" * 40)
    
    # Initialize preprocessor
    preprocessor = DataPreprocessor()
    
    # Test functions
    print("\nModule loaded successfully!")
    print("Available methods:")
    print("1. load_data(filepath) - Load CSV file")
    print("2. clean_data(df) - Clean missing values")
    print("3. create_features(df) - Create new features")