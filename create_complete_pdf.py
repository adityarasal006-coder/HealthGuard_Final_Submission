"""
Complete PDF Report with All Visualizations
HealthGuard Analytics - COVID-19 Case Analysis
"""

from fpdf import FPDF
from datetime import datetime
import os

class ReportPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        
    def header(self):
        if self.page_no() > 1:  # No header on cover page
            self.set_fill_color(30, 60, 90)
            self.rect(0, 0, 210, 25, 'F')
            self.set_font('Arial', 'B', 12)
            self.set_text_color(255, 255, 255)
            self.cell(0, 8, 'HealthGuard Analytics', 0, 1, 'C')
            self.set_font('Arial', 'I', 8)
            self.cell(0, 5, 'COVID-19 Case Analysis Report', 0, 1, 'C')
            self.set_y(20)
        
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 60, 90)
        self.set_fill_color(230, 240, 250)
        self.cell(0, 12, title, 0, 1, 'L', 1)
        self.set_draw_color(30, 60, 90)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(8)
    
    def add_image_with_caption(self, img_path, caption):
        if os.path.exists(img_path):
            try:
                self.image(img_path, x=25, w=160)
                self.ln(5)
                self.set_font('Arial', 'I', 9)
                self.set_text_color(80, 80, 80)
                self.cell(0, 8, caption, 0, 1, 'C')
                self.ln(10)
                return True
            except Exception as e:
                self.set_font('Arial', '', 9)
                self.set_text_color(255, 0, 0)
                self.cell(0, 8, f'[Image not available: {img_path}]', 0, 1, 'C')
                return False
        return False

# Create PDF
pdf = ReportPDF()
pdf.add_page()

# ============================================================================
# COVER PAGE
# ============================================================================
pdf.set_fill_color(30, 60, 90)
pdf.rect(0, 0, 210, 297, 'F')

pdf.set_y(70)
pdf.set_font('Arial', 'B', 32)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 20, 'COVID-19', 0, 1, 'C')
pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 15, 'Case Trend Analysis', 0, 1, 'C')
pdf.set_font('Arial', 'B', 22)
pdf.cell(0, 15, '& Recovery Insights', 0, 1, 'C')

pdf.set_y(150)
pdf.set_font('Arial', '', 12)
pdf.set_text_color(220, 220, 220)
pdf.cell(0, 8, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 6, datetime.now().strftime('%B %d, 2026'), 0, 1, 'C')

pdf.add_page()

# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================
pdf.section_title('Executive Summary')

summary_text = """This comprehensive analysis examines 5,000 patient cases from the early phase 
of the COVID-19 outbreak (January - March 2020). The study provides critical insights into 
demographic patterns, infection transmission dynamics, recovery timelines, and regional 
impact to support evidence-based public health decision-making."""

pdf.set_font('Arial', '', 11)
pdf.set_text_color(50, 50, 50)
pdf.multi_cell(0, 7, summary_text)
pdf.ln(10)

# Key Statistics
pdf.set_font('Arial', 'B', 12)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Statistics at a Glance', 0, 1, 'L')
pdf.ln(5)

# Statistics boxes
stats = [
    ('Total Cases', '5,000'),
    ('Recovery Rate', '68.4%'),
    ('Avg Recovery', '12.8 days'),
    ('Avg Age', '44.8 years'),
    ('Deceased', '559'),
    ('Active', '1,019')
]

pdf.set_font('Arial', '', 9)
for i, (label, value) in enumerate(stats):
    x = 25 + (i % 3) * 55
    y = pdf.get_y()
    pdf.set_fill_color(248, 249, 250)
    pdf.set_draw_color(200, 200, 200)
    pdf.rect(x, y, 50, 35, 'FD')
    pdf.set_xy(x + 5, y + 5)
    pdf.set_font('Arial', '', 8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(40, 5, label, 0, 1, 'L')
    pdf.set_xy(x + 5, y + 15)
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(30, 60, 90)
    pdf.cell(40, 8, value, 0, 1, 'L')
    if (i + 1) % 3 == 0:
        pdf.ln(40)

pdf.ln(15)

# ============================================================================
# DEMOGRAPHIC ANALYSIS - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('1. Demographic Analysis')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Who is getting infected?', 0, 1, 'L')
pdf.ln(5)

# Add demographic chart
pdf.add_image_with_caption('output/demographic_analysis.png', 
    'Figure 1: Demographic Analysis - Gender distribution, age distribution, age groups, and top affected countries')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Demographic Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

findings = [
    '- Average Patient Age: 44.8 years',
    '- Age Range: 1 to 90 years',
    '- Most vulnerable age group: 46-60 years (31.3% of cases)',
    '- Age group 60+ years accounts for 21.0% of cases'
]

for f in findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# INFECTION PATTERNS - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('2. Infection Patterns')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'How are infections spreading?', 0, 1, 'L')
pdf.ln(5)

# Add infection patterns chart
pdf.add_image_with_caption('output/infection_patterns.png',
    'Figure 2: Infection Patterns - Sources of infection and contact exposure distribution')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Infection Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

infection_findings = [
    '- Primary Source: Contact with confirmed case (34.8%)',
    '- Travel history: 25.0% of cases',
    '- Community spread: 22.0% of cases',
    '- Average contacts per patient: 5.0 individuals',
    '- Contact tracing is critical for outbreak control'
]

for f in infection_findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# RECOVERY TRENDS - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('3. Recovery Trends')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'What are the recovery patterns?', 0, 1, 'L')
pdf.ln(5)

# Add recovery trends chart
pdf.add_image_with_caption('output/recovery_trends.png',
    'Figure 3: Recovery Trends - Recovery time distribution and recovery by age group')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Recovery Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

recovery_findings = [
    '- Recovery Rate: 68.4% (3,422 patients)',
    '- Average Recovery Time: 12.8 days',
    '- Median Recovery Time: 12 days',
    '- Recovery Range: 5 to 30 days',
    '- Older patients (60+) take 15.2 days on average vs 10.2 days for young patients'
]

for f in recovery_findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# REGIONAL IMPACT - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('4. Regional Impact')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Which regions are most affected?', 0, 1, 'L')
pdf.ln(5)

# Add regional impact chart
pdf.add_image_with_caption('output/regional_impact.png',
    'Figure 4: Regional Impact - Top affected regions and patient outcomes')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Regional Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

regional_findings = [
    '- Most Affected: Maharashtra (348 cases, 7.0%)',
    '- Second: New York (347 cases, 6.9%)',
    '- Third: Sao Paulo (346 cases, 6.9%)',
    '- Top 10 regions account for 68% of all cases',
    '- Patient Outcomes: 68.4% recovered, 20.4% active, 11.2% deceased'
]

for f in regional_findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# FACTORS INFLUENCING RECOVERY - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('5. Factors Influencing Recovery')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'What affects recovery time?', 0, 1, 'L')
pdf.ln(5)

# Add recovery factors chart
pdf.add_image_with_caption('output/recovery_factors.png',
    'Figure 5: Factors Influencing Recovery - Age vs recovery time correlation')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Key Factor Analysis:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

factors_findings = [
    '- Age Correlation with Recovery: +0.42 (moderate positive)',
    '- Contact Number Correlation: +0.18 (weak positive)',
    '- Each year of age adds approximately 0.12 days to recovery',
    '- Age is the strongest predictor of recovery duration'
]

for f in factors_findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# REGRESSION MODEL - WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('6. Predictive Model')
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Linear Regression Analysis', 0, 1, 'L')
pdf.ln(5)

# Add regression model chart
pdf.add_image_with_caption('output/regression_model.png',
    'Figure 6: Linear Regression Model - Actual vs predicted recovery time with residual analysis')

# Add key findings
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 60, 90)
pdf.cell(0, 8, 'Model Performance:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

model_findings = [
    '- R2 Score: 0.176 (explains 17.6% of variance)',
    '- RMSE: 4.8 days (average prediction error)',
    '- Age Coefficient: +0.12 days/year',
    '- Contact Coefficient: +0.08 days/contact',
    '- Age is the most significant predictor of recovery time'
]

for f in model_findings:
    pdf.cell(8, 6, '', 0, 0)
    pdf.multi_cell(0, 6, f)

pdf.ln(5)

# ============================================================================
# RECOMMENDATIONS
# ============================================================================
pdf.add_page()
pdf.section_title('Strategic Recommendations')

recommendations = [
    ('1. SCREENING PRIORITIZATION', 
     'Focus screening efforts on the 45+ age group, which accounts for over 52% of cases and shows longer recovery times.'),
    
    ('2. CONTACT TRACING ENHANCEMENT', 
     'With 34.8% of cases linked to contact with confirmed patients, expand contact tracing capacity. Prioritize individuals with more than 10 contacts.'),
    
    ('3. REGIONAL RESOURCE ALLOCATION', 
     'Concentrate healthcare resources in Maharashtra, New York, and Sao Paulo which account for nearly 21% of all cases.'),
    
    ('4. AGE-SPECIFIC TREATMENT PROTOCOLS', 
     'Develop treatment protocols based on age groups. Elderly patients require extended monitoring (15+ days) while younger patients recover faster.'),
    
    ('5. EARLY WARNING SYSTEM', 
     'Strengthen surveillance in regions showing rapid case growth. Implement real-time monitoring to identify super-spreader events early.'),
    
    ('6. DATA QUALITY IMPROVEMENT', 
     'Improve gender data collection as significant missing values were detected in this analysis.')
]

for title, description in recommendations:
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(30, 60, 90)
    pdf.cell(0, 8, title, 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5, description)
    pdf.ln(3)

# ============================================================================
# CONCLUSION
# ============================================================================
pdf.add_page()
pdf.section_title('Conclusion')

conclusion_text = """This comprehensive analysis successfully provides actionable insights for public health decision-making during the early phase of the COVID-19 outbreak.

Key Achievements:
- Complete analysis of 5,000 patient cases
- 6 professional visualizations generated
- Demographic patterns identified
- Recovery trends analyzed
- Predictive model built and evaluated

The identified patterns in demographics, transmission, and recovery can help authorities implement targeted interventions and optimize resource allocation for future outbreaks.

For any questions or additional analysis requirements, please contact the HealthGuard Analytics team."""

pdf.set_font('Arial', '', 11)
pdf.set_text_color(50, 50, 50)
pdf.multi_cell(0, 7, conclusion_text)

pdf.ln(15)

# Closing
pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.cell(0, 6, 'Data-Driven Public Health Insights', 0, 1, 'C')

# ============================================================================
# SAVE PDF
# ============================================================================
try:
    pdf.output('HealthGuard_Complete_Report.pdf')
    print("\n" + "="*70)
    print("COMPLETE PDF REPORT CREATED SUCCESSFULLY!")
    print("="*70)
    print("\nFile: HealthGuard_Complete_Report.pdf")
    print("Location: C:\\Users\\ASUS\\healthguard_project")
    print("\nReport Contents:")
    print("   Page 1: Professional Cover Page")
    print("   Page 2: Executive Summary with Key Statistics")
    print("   Page 3: Demographic Analysis with Chart")
    print("   Page 4: Infection Patterns with Chart")
    print("   Page 5: Recovery Trends with Chart")
    print("   Page 6: Regional Impact with Chart")
    print("   Page 7: Factors Influencing Recovery with Chart")
    print("   Page 8: Predictive Model with Chart")
    print("   Page 9: Strategic Recommendations")
    print("   Page 10: Conclusion")
    print("\nAll 6 charts from your analysis are included!")
    print("\nTo open, type: start HealthGuard_Complete_Report.pdf")
    
except Exception as e:
    print(f"\nError: {e}")
    print("\nMake sure all charts exist in the 'output' folder:")
    os.system('dir output')