import pandas as pd
import numpy as np
from datetime import datetime

# Load data
df = pd.read_csv('covid_dataset.csv')

# Clean data
df['confirmed_date'] = pd.to_datetime(df['confirmed_date'], errors='coerce')
df['released_date'] = pd.to_datetime(df['released_date'], errors='coerce')
df['age'] = 2020 - df['birth_year']
df['recovery_days'] = (df['released_date'] - df['confirmed_date']).dt.days
recovered = df[df['recovery_days'].notna()]

# Calculate metrics
gender_counts = df['sex'].value_counts()
male_pct = gender_counts.get('male', 0)/len(df)*100
female_pct = gender_counts.get('female', 0)/len(df)*100

avg_age = df['age'].mean()
age_min = df['age'].min()
age_max = df['age'].max()

infection_sources = df['infection_reason'].value_counts()
top_source = infection_sources.index[0] if len(infection_sources) > 0 else 'N/A'
top_source_pct = infection_sources.values[0]/len(df)*100 if len(infection_sources) > 0 else 0

avg_contacts = df['contact_number'].mean()

recovery_rate = len(recovered)/len(df)*100 if len(recovered) > 0 else 0
avg_recovery = recovered['recovery_days'].mean() if len(recovered) > 0 else 0
median_recovery = recovered['recovery_days'].median() if len(recovered) > 0 else 0

regions = df['region'].value_counts()
outcomes = df['state'].value_counts()

# Print report
print('\n' + '='*80)
print('HEALTHGUARD ANALYTICS - PROJECT REPORT')
print('='*80)
print(f'Generated: {datetime.now().strftime("%B %d, %Y")}')
print('='*80)

print('\n📊 KEY METRICS SUMMARY')
print('-'*60)

print(f'\n1. DEMOGRAPHICS:')
print(f'   • Gender: Male {male_pct:.1f}%, Female {female_pct:.1f}%')
print(f'   • Average Age: {avg_age:.1f} years')
print(f'   • Age Range: {age_min:.0f} - {age_max:.0f} years')

print(f'\n2. INFECTION PATTERNS:')
print(f'   • Primary Source: {top_source} ({top_source_pct:.1f}%)')
print(f'   • Average Contacts: {avg_contacts:.1f}')

print(f'\n3. RECOVERY OUTCOMES:')
print(f'   • Recovery Rate: {recovery_rate:.1f}%')
print(f'   • Average Recovery Time: {avg_recovery:.1f} days')
print(f'   • Median Recovery Time: {median_recovery:.0f} days')

print(f'\n4. PATIENT OUTCOMES:')
for outcome, count in outcomes.items():
    print(f'   • {outcome}: {count} ({count/len(df)*100:.1f}%)')

print(f'\n5. TOP AFFECTED REGIONS:')
for i, (region, count) in enumerate(regions.head(5).items()):
    print(f'   {i+1}. {region}: {count} cases')

print('\n' + '='*80)
print('✅ Report generated successfully!')
print('='*80)

# Also save to file
with open('project_report.txt', 'w') as f:
    f.write('HEALTHGUARD ANALYTICS - PROJECT REPORT\n')
    f.write('='*60 + '\n\n')
    f.write(f'Generated: {datetime.now().strftime("%B %d, %Y")}\n\n')
    f.write('KEY METRICS:\n')
    f.write(f'- Gender: Male {male_pct:.1f}%, Female {female_pct:.1f}%\n')
    f.write(f'- Average Age: {avg_age:.1f} years\n')
    f.write(f'- Age Range: {age_min:.0f} - {age_max:.0f}\n')
    f.write(f'- Primary Infection Source: {top_source} ({top_source_pct:.1f}%)\n')
    f.write(f'- Average Contacts: {avg_contacts:.1f}\n')
    f.write(f'- Recovery Rate: {recovery_rate:.1f}%\n')
    f.write(f'- Average Recovery Time: {avg_recovery:.1f} days\n')
    f.write(f'- Most Affected Region: {regions.index[0]}\n')

print('\n✅ Report also saved to: project_report.txt')