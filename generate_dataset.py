"""
Generate sample COVID-19 dataset for HealthGuard Analytics project
Fixed version - probabilities sum to 1
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of records
n_records = 5000

# Generate dates (Jan 2020 - March 2020)
start_date = datetime(2020, 1, 15)
end_date = datetime(2020, 3, 31)

# Create dataset
data = {
    'patient_id': [f'P{str(i).zfill(5)}' for i in range(1, n_records + 1)],
    
    # Demographics
    'sex': np.random.choice(['Male', 'Female'], n_records, p=[0.52, 0.48]),
    'birth_year': np.random.choice(range(1930, 2020), n_records),
    'country': np.random.choice(['India', 'USA', 'UK', 'Brazil', 'Italy', 'France', 'Spain', 'Germany'], 
                                 n_records, p=[0.35, 0.20, 0.10, 0.08, 0.07, 0.07, 0.07, 0.06]),
    'region': np.random.choice([
        'Maharashtra', 'Delhi', 'Gujarat', 'Tamil Nadu', 'Karnataka', 
        'Uttar Pradesh', 'West Bengal', 'Rajasthan', 'New York', 'California',
        'Texas', 'Florida', 'London', 'Manchester', 'Sao Paulo'
    ], n_records),
    
    # Infection details - FIXED: probabilities sum to 1
    'infection_reason': np.random.choice([
        'Travel history', 'Contact with confirmed case', 'Community spread',
        'Healthcare worker', 'Mass gathering', 'Family cluster'
    ], n_records, p=[0.25, 0.35, 0.25, 0.05, 0.05, 0.05]),  # Sum = 1.0
    
    # Infection order - FIXED: probabilities sum to 1
    'infection_order': np.random.choice(range(1, 15), n_records, 
                                         p=[0.35, 0.25, 0.15, 0.08, 0.05, 0.03, 0.02, 0.01, 
                                            0.01, 0.01, 0.01, 0.01, 0.01, 0.01]),  # Sum = 1.0
    
    'infected_by': np.random.choice([np.nan] + [f'P{str(i).zfill(5)}' for i in range(1, 100)], 
                                     n_records, p=[0.6] + [0.4/99]*99),
    
    'contact_number': np.random.poisson(5, n_records),
    
    # Outcome status
    'state': np.random.choice(['released', 'isolated', 'deceased'], n_records, p=[0.75, 0.20, 0.05]),
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate dates with realistic patterns
confirmed_dates = []
released_dates = []
deceased_dates = []

for i in range(n_records):
    # Confirmation date (earlier in the outbreak)
    conf_offset = np.random.exponential(20)
    conf_date = start_date + timedelta(days=int(conf_offset))
    conf_date = min(conf_date, end_date)
    confirmed_dates.append(conf_date)
    
    # Recovery/Deceased dates based on outcome
    if df.loc[i, 'state'] == 'released':
        # Recovery takes 5-25 days
        recovery_days = int(np.random.normal(14, 5))
        recovery_days = max(5, min(30, recovery_days))
        rel_date = conf_date + timedelta(days=recovery_days)
        released_dates.append(rel_date)
        deceased_dates.append(pd.NaT)
    elif df.loc[i, 'state'] == 'deceased':
        # Death occurs 3-20 days after confirmation
        death_days = int(np.random.normal(10, 4))
        death_days = max(3, min(20, death_days))
        dec_date = conf_date + timedelta(days=death_days)
        deceased_dates.append(dec_date)
        released_dates.append(pd.NaT)
    else:  # isolated (still active)
        released_dates.append(pd.NaT)
        deceased_dates.append(pd.NaT)

df['confirmed_date'] = confirmed_dates
df['released_date'] = released_dates
df['deceased_date'] = deceased_dates

# Add realistic age patterns
ages = []
for i in range(n_records):
    age = 2020 - df.loc[i, 'birth_year']
    ages.append(age)
df['age'] = ages

# Adjust outcomes based on age (realistic pattern)
for i in range(n_records):
    age = df.loc[i, 'age']
    if age > 60:
        # Older patients have higher mortality
        if df.loc[i, 'state'] == 'released' and np.random.random() < 0.2:
            df.loc[i, 'state'] = 'deceased'
            df.loc[i, 'released_date'] = pd.NaT
            death_days = int(np.random.normal(8, 3))
            death_days = max(3, min(20, death_days))
            df.loc[i, 'deceased_date'] = df.loc[i, 'confirmed_date'] + timedelta(days=death_days)
    elif age < 18:
        # Children recover faster
        if df.loc[i, 'state'] == 'released' and df.loc[i, 'released_date'] is not pd.NaT:
            # Reduce recovery time
            current_recovery = (df.loc[i, 'released_date'] - df.loc[i, 'confirmed_date']).days
            if current_recovery > 10:
                new_recovery = max(5, current_recovery - 5)
                df.loc[i, 'released_date'] = df.loc[i, 'confirmed_date'] + timedelta(days=new_recovery)

# Clean up dates - convert to proper format
df['confirmed_date'] = pd.to_datetime(df['confirmed_date']).dt.date
df['released_date'] = df['released_date'].apply(lambda x: x.date() if pd.notna(x) else pd.NaT)
df['deceased_date'] = df['deceased_date'].apply(lambda x: x.date() if pd.notna(x) else pd.NaT)

# Save to CSV
df.to_csv('covid_dataset.csv', index=False)
print("="*60)
print("✅ DATASET GENERATED SUCCESSFULLY!")
print("="*60)
print(f"\n📊 Dataset Statistics:")
print(f"   Total records: {len(df):,}")
print(f"   Columns: {len(df.columns)}")
print(f"\n📋 Column Names:")
for col in df.columns:
    print(f"   • {col}")
print(f"\n📈 Sample Data (first 5 rows):")
print(df.head())
print(f"\n📊 Data Types:")
print(df.dtypes)
print(f"\n🔍 Missing Values:")
print(df.isnull().sum())
print(f"\n💾 File saved as: covid_dataset.csv")
print("="*60)