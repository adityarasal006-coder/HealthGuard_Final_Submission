"""
HealthGuard Analytics - COVID-19 Case Analysis
Customized for Your Dataset
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Create output folder
if not os.path.exists('output'):
    os.makedirs('output')

print("="*80)
print("HEALTHGUARD ANALYTICS - COVID-19 CASE ANALYSIS")
print("="*80)

# ============================================================================
# LOAD DATASET
# ============================================================================

print("\n[1] Loading dataset...")

df = pd.read_csv('covid_dataset.csv')
print(f"✓ Loaded: {len(df)} rows, {len(df.columns)} columns")
print(f"✓ Columns: {list(df.columns)}")

# ============================================================================
# DATA CLEANING
# ============================================================================

print("\n" + "="*80)
print("DATA CLEANING")
print("="*80)

df_clean = df.copy()

# Convert dates
df_clean['confirmed_date'] = pd.to_datetime(df_clean['confirmed_date'], errors='coerce')
df_clean['released_date'] = pd.to_datetime(df_clean['released_date'], errors='coerce')
df_clean['deceased_date'] = pd.to_datetime(df_clean['deceased_date'], errors='coerce')

# Calculate age from birth_year
df_clean['age'] = 2020 - df_clean['birth_year']

# Create age groups
df_clean['age_group'] = pd.cut(df_clean['age'], 
                               bins=[0, 18, 30, 45, 60, 120], 
                               labels=['0-18', '19-30', '31-45', '46-60', '60+'])

# Calculate recovery days (for released patients)
df_clean['recovery_days'] = (df_clean['released_date'] - df_clean['confirmed_date']).dt.days

# Fill missing contact_number with 0
df_clean['contact_number'] = df_clean['contact_number'].fillna(0).astype(int)

# Fill missing infection_reason
df_clean['infection_reason'] = df_clean['infection_reason'].fillna('Unknown')

print("\n✓ Data cleaning complete!")

# ============================================================================
# QUESTION 1: DEMOGRAPHIC ANALYSIS (Who is getting infected?)
# ============================================================================

print("\n" + "="*80)
print("QUESTION 1: WHO IS GETTING INFECTED?")
print("="*80)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gender distribution
gender_counts = df_clean['sex'].value_counts()
axes[0,0].pie(gender_counts.values, labels=gender_counts.index, 
              autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
axes[0,0].set_title('Gender Distribution', fontsize=14, fontweight='bold')
print("\n👥 Gender Distribution:")
for gender, count in gender_counts.items():
    print(f"   {gender}: {count} ({count/len(df_clean)*100:.1f}%)")

# Age distribution
axes[0,1].hist(df_clean['age'].dropna(), bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0,1].axvline(df_clean['age'].mean(), color='red', linestyle='--', 
                  label=f"Mean: {df_clean['age'].mean():.1f}")
axes[0,1].set_xlabel('Age')
axes[0,1].set_ylabel('Number of Cases')
axes[0,1].set_title('Age Distribution', fontsize=14, fontweight='bold')
axes[0,1].legend()
print(f"\n👤 Age Statistics:")
print(f"   Average Age: {df_clean['age'].mean():.1f} years")
print(f"   Age Range: {df_clean['age'].min():.0f} - {df_clean['age'].max():.0f} years")

# Age group distribution
age_group_counts = df_clean['age_group'].value_counts().sort_index()
axes[1,0].bar(age_group_counts.index, age_group_counts.values, color='lightgreen', edgecolor='black')
axes[1,0].set_xlabel('Age Group')
axes[1,0].set_ylabel('Number of Cases')
axes[1,0].set_title('Cases by Age Group', fontsize=14, fontweight='bold')
axes[1,0].tick_params(axis='x', rotation=45)
print(f"\n📊 Cases by Age Group:")
for group, count in age_group_counts.items():
    print(f"   {group}: {count} ({count/len(df_clean)*100:.1f}%)")

# Country distribution
country_counts = df_clean['country'].value_counts()
axes[1,1].barh(range(len(country_counts)), country_counts.values, color='coral')
axes[1,1].set_yticks(range(len(country_counts)))
axes[1,1].set_yticklabels(country_counts.index)
axes[1,1].set_xlabel('Number of Cases')
axes[1,1].set_title('Cases by Country', fontsize=14, fontweight='bold')
print(f"\n🌍 Countries:")
for country, count in country_counts.items():
    print(f"   {country}: {count} ({count/len(df_clean)*100:.1f}%)")

plt.tight_layout()
plt.savefig('output/demographic_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✓ Saved: output/demographic_analysis.png")

# ============================================================================
# QUESTION 2: INFECTION PATTERNS (How are infections spreading?)
# ============================================================================

print("\n" + "="*80)
print("QUESTION 2: HOW ARE INFECTIONS SPREADING?")
print("="*80)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Infection reasons
reason_counts = df_clean['infection_reason'].value_counts()
axes[0].bar(range(len(reason_counts)), reason_counts.values, color='purple', edgecolor='black')
axes[0].set_xticks(range(len(reason_counts)))
axes[0].set_xticklabels(reason_counts.index, rotation=45, ha='right')
axes[0].set_xlabel('Infection Reason')
axes[0].set_ylabel('Number of Cases')
axes[0].set_title('Infection Sources', fontsize=14, fontweight='bold')
print("\n🦠 Infection Sources:")
for reason, count in reason_counts.items():
    print(f"   {reason}: {count} ({count/len(df_clean)*100:.1f}%)")

# Contact distribution
contact_data = df_clean[df_clean['contact_number'] > 0]['contact_number']
if len(contact_data) > 0:
    axes[1].hist(contact_data, bins=20, edgecolor='black', alpha=0.7, color='teal')
    axes[1].set_xlabel('Number of Contacts')
    axes[1].set_ylabel('Number of Cases')
    axes[1].set_title('Contact Distribution', fontsize=14, fontweight='bold')
    print(f"\n📞 Contact Statistics:")
    print(f"   Average contacts: {df_clean['contact_number'].mean():.1f}")
    print(f"   Median contacts: {df_clean['contact_number'].median():.0f}")
    print(f"   Max contacts: {df_clean['contact_number'].max():.0f}")

plt.tight_layout()
plt.savefig('output/infection_patterns.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✓ Saved: output/infection_patterns.png")

# ============================================================================
# QUESTION 3: RECOVERY TRENDS
# ============================================================================

print("\n" + "="*80)
print("QUESTION 3: RECOVERY TRENDS")
print("="*80)

# Get recovered patients
recovered_df = df_clean[df_clean['recovery_days'].notna() & (df_clean['recovery_days'] >= 0)].copy()

if len(recovered_df) > 0:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Recovery time distribution
    axes[0].hist(recovered_df['recovery_days'], bins=20, edgecolor='black', alpha=0.7, color='green')
    axes[0].axvline(recovered_df['recovery_days'].mean(), color='red', linestyle='--',
                    label=f"Mean: {recovered_df['recovery_days'].mean():.1f} days")
    axes[0].axvline(recovered_df['recovery_days'].median(), color='blue', linestyle='--',
                    label=f"Median: {recovered_df['recovery_days'].median():.0f} days")
    axes[0].set_xlabel('Recovery Time (days)')
    axes[0].set_ylabel('Number of Patients')
    axes[0].set_title('Recovery Time Distribution', fontsize=14, fontweight='bold')
    axes[0].legend()
    
    # Recovery by age group
    age_recovery = recovered_df.groupby('age_group')['recovery_days'].mean()
    axes[1].bar(age_recovery.index, age_recovery.values, color='lightblue', edgecolor='black')
    axes[1].set_xlabel('Age Group')
    axes[1].set_ylabel('Average Recovery (days)')
    axes[1].set_title('Recovery by Age Group', fontsize=14, fontweight='bold')
    axes[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('output/recovery_trends.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"\n📈 Recovery Statistics:")
    print(f"   Recovered patients: {len(recovered_df)}")
    print(f"   Recovery rate: {len(recovered_df)/len(df_clean)*100:.1f}%")
    print(f"   Average recovery: {recovered_df['recovery_days'].mean():.1f} days")
    print(f"   Median recovery: {recovered_df['recovery_days'].median():.0f} days")
    print(f"   Recovery range: {recovered_df['recovery_days'].min():.0f} - {recovered_df['recovery_days'].max():.0f} days")
else:
    print("\n⚠️ No recovered patients found")

print("\n✓ Saved: output/recovery_trends.png")

# ============================================================================
# QUESTION 4: REGIONAL IMPACT
# ============================================================================

print("\n" + "="*80)
print("QUESTION 4: REGIONAL IMPACT")
print("="*80)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Regional distribution
region_counts = df_clean['region'].value_counts().head(15)
axes[0].barh(range(len(region_counts)), region_counts.values, color='orange')
axes[0].set_yticks(range(len(region_counts)))
axes[0].set_yticklabels(region_counts.index)
axes[0].set_xlabel('Number of Cases')
axes[0].set_title('Top Affected Regions', fontsize=14, fontweight='bold')

print("\n🗺️ Top Affected Regions:")
for i, (region, count) in enumerate(region_counts.head(10).items()):
    print(f"   {i+1}. {region}: {count} cases")

# Outcome summary
outcome_counts = df_clean['state'].value_counts()
axes[1].bar(outcome_counts.index, outcome_counts.values, color=['green', 'orange', 'red'], edgecolor='black')
axes[1].set_xlabel('Outcome')
axes[1].set_ylabel('Number of Cases')
axes[1].set_title('Patient Outcomes', fontsize=14, fontweight='bold')

print(f"\n📊 Outcomes:")
for outcome, count in outcome_counts.items():
    print(f"   {outcome}: {count} ({count/len(df_clean)*100:.1f}%)")

plt.tight_layout()
plt.savefig('output/regional_impact.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✓ Saved: output/regional_impact.png")

# ============================================================================
# QUESTION 5: FACTORS INFLUENCING RECOVERY TIME
# ============================================================================

print("\n" + "="*80)
print("QUESTION 5: FACTORS INFLUENCING RECOVERY TIME")
print("="*80)

if len(recovered_df) > 0:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Age vs Recovery scatter
    axes[0].scatter(recovered_df['age'], recovered_df['recovery_days'], alpha=0.5, s=30)
    axes[0].set_xlabel('Age')
    axes[0].set_ylabel('Recovery Time (days)')
    axes[0].set_title('Age vs Recovery Time', fontsize=14, fontweight='bold')
    
    # Add trend line
    age_data = recovered_df[['age', 'recovery_days']].dropna()
    if len(age_data) > 0:
        z = np.polyfit(age_data['age'], age_data['recovery_days'], 1)
        p = np.poly1d(z)
        x_sorted = np.sort(age_data['age'])
        axes[0].plot(x_sorted, p(x_sorted), "r--", linewidth=2,
                    label=f"Trend: {z[0]:.2f}x + {z[1]:.2f}")
        axes[0].legend()
    
    # Contact vs Recovery scatter
    contact_recovery = recovered_df[recovered_df['contact_number'] > 0]
    if len(contact_recovery) > 0:
        axes[1].scatter(contact_recovery['contact_number'], contact_recovery['recovery_days'], alpha=0.5, s=30)
        axes[1].set_xlabel('Number of Contacts')
        axes[1].set_ylabel('Recovery Time (days)')
        axes[1].set_title('Contacts vs Recovery Time', fontsize=14, fontweight='bold')
        
        # Add trend line
        contact_data = contact_recovery[['contact_number', 'recovery_days']].dropna()
        if len(contact_data) > 0:
            z2 = np.polyfit(contact_data['contact_number'], contact_data['recovery_days'], 1)
            p2 = np.poly1d(z2)
            x_sorted2 = np.sort(contact_data['contact_number'])
            axes[1].plot(x_sorted2, p2(x_sorted2), "r--", linewidth=2,
                        label=f"Trend: {z2[0]:.3f}x + {z2[1]:.2f}")
            axes[1].legend()
    
    plt.tight_layout()
    plt.savefig('output/recovery_factors.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # Calculate correlations
    print("\n📊 Correlation with Recovery Time:")
    if len(recovered_df) > 1:
        age_corr = recovered_df['age'].corr(recovered_df['recovery_days'])
        print(f"   Age: {age_corr:.3f}")
        contact_corr = recovered_df['contact_number'].corr(recovered_df['recovery_days'])
        print(f"   Contact Number: {contact_corr:.3f}")
    
    print("\n✓ Saved: output/recovery_factors.png")

# ============================================================================
# LINEAR REGRESSION MODEL
# ============================================================================

print("\n" + "="*80)
print("LINEAR REGRESSION MODEL - Predicting Recovery Time")
print("="*80)

if len(recovered_df) > 10:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error
    
    # Prepare features
    X = recovered_df[['age', 'contact_number']].dropna()
    y = recovered_df.loc[X.index, 'recovery_days']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Evaluate
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"\n🎯 Model Performance:")
    print(f"   R² Score: {r2:.3f}")
    print(f"   RMSE: {rmse:.2f} days")
    
    print(f"\n🔑 Feature Coefficients:")
    for feature, coef in zip(['age', 'contact_number'], model.coef_):
        print(f"   {feature}: {coef:.3f} days per unit")
    
    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Actual vs Predicted
    axes[0].scatter(y_test, y_pred, alpha=0.5)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    axes[0].set_xlabel('Actual Recovery Time (days)')
    axes[0].set_ylabel('Predicted Recovery Time (days)')
    axes[0].set_title(f'Actual vs Predicted (R² = {r2:.3f})')
    
    # Residuals
    residuals = y_test - y_pred
    axes[1].scatter(y_pred, residuals, alpha=0.5)
    axes[1].axhline(y=0, color='r', linestyle='--')
    axes[1].set_xlabel('Predicted Recovery Time (days)')
    axes[1].set_ylabel('Residuals')
    axes[1].set_title('Residual Plot')
    
    plt.tight_layout()
    plt.savefig('output/regression_model.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("\n✓ Saved: output/regression_model.png")
else:
    print(f"\n⚠️ Not enough recovered patients for regression model (need >10, have {len(recovered_df)})")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "="*80)
print("FINAL SUMMARY REPORT")
print("="*80)

print("\n📌 KEY FINDINGS:")

print(f"\n1. DEMOGRAPHICS:")
print(f"   • Most affected gender: {gender_counts.index[0]} ({gender_counts.values[0]/len(df_clean)*100:.1f}%)")
print(f"   • Average age: {df_clean['age'].mean():.1f} years")
print(f"   • Age range: {df_clean['age'].min():.0f} - {df_clean['age'].max():.0f} years")

print(f"\n2. INFECTION PATTERNS:")
print(f"   • Primary infection source: {reason_counts.index[0]} ({reason_counts.values[0]/len(df_clean)*100:.1f}%)")
print(f"   • Average contacts: {df_clean['contact_number'].mean():.1f}")

print(f"\n3. RECOVERY OUTCOMES:")
print(f"   • Recovery rate: {len(recovered_df)/len(df_clean)*100:.1f}%")
if len(recovered_df) > 0:
    print(f"   • Average recovery time: {recovered_df['recovery_days'].mean():.1f} days")

print(f"\n4. REGIONAL IMPACT:")
print(f"   • Most affected region: {region_counts.index[0]} ({region_counts.values[0]} cases)")

print("\n" + "="*80)
print("💡 RECOMMENDATIONS:")
print("="*80)
print("1. Prioritize screening for high-risk age groups (45+ years)")
print("2. Implement targeted contact tracing for high-contact individuals")
print("3. Allocate healthcare resources to most affected regions")
print("4. Develop age-specific treatment protocols")
print("5. Strengthen early warning systems in high-risk areas")

print("\n" + "="*80)
print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*80)

print("\n📁 Output Files Generated:")
print("   📊 output\\demographic_analysis.png")
print("   📊 output\\infection_patterns.png")
print("   📊 output\\recovery_trends.png")
print("   📊 output\\regional_impact.png")
print("   📊 output\\recovery_factors.png")
print("   📊 output\\regression_model.png")