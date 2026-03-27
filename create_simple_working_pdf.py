"""
Simple Working PDF Report for HealthGuard Analytics
"""

from fpdf import FPDF
from datetime import datetime
import os

class SimplePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
    
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 10)
            self.set_text_color(50, 50, 50)
            self.cell(0, 6, 'HealthGuard Analytics', 0, 1, 'L')
            self.set_draw_color(180, 180, 180)
            self.line(15, 18, 195, 18)
            self.set_y(25)
    
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-18)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 6, f'Page {self.page_no()}', 0, 0, 'C')

# Create PDF
pdf = SimplePDF()

# COVER PAGE
pdf.add_page()
pdf.set_fill_color(30, 55, 80)
pdf.rect(0, 0, 210, 297, 'F')

pdf.set_y(80)
pdf.set_font('Arial', 'B', 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 18, 'COVID-19', 0, 1, 'C')
pdf.set_font('Arial', 'B', 22)
pdf.cell(0, 14, 'Case Trend Analysis', 0, 1, 'C')
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 14, '& Recovery Insights', 0, 1, 'C')

pdf.set_y(160)
pdf.set_font('Arial', '', 11)
pdf.set_text_color(200, 200, 200)
pdf.cell(0, 8, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 6, datetime.now().strftime('%B %d, 2026'), 0, 1, 'C')

# PAGE 1 - EXECUTIVE SUMMARY
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, 'Executive Summary', 0, 1, 'L')
pdf.set_draw_color(30, 55, 80)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(8)

pdf.set_font('Arial', '', 11)
pdf.set_text_color(60, 60, 60)
summary = """This comprehensive analysis examines 5,000 patient cases from the early phase of the COVID-19 outbreak (January - March 2020). The study provides critical insights into demographic patterns, infection transmission dynamics, recovery timelines, and regional impact to support evidence-based public health decision-making."""
pdf.multi_cell(0, 6, summary)
pdf.ln(10)

# Key Stats
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Key Statistics', 0, 1, 'L')
pdf.ln(3)

stats = [
    ('Total Cases', '5,000'),
    ('Recovery Rate', '68.4%'),
    ('Recovered', '3,422'),
    ('Avg Recovery', '12.8 days'),
    ('Avg Age', '44.8 years'),
    ('Deceased', '559'),
    ('Active Cases', '1,019'),
    ('Primary Source', 'Contact (34.8%)')
]

for i, (label, value) in enumerate(stats):
    x = 20 + (i % 4) * 45
    y = pdf.get_y()
    pdf.set_fill_color(245, 248, 250)
    pdf.rect(x, y, 40, 28, 'FD')
    pdf.set_xy(x + 2, y + 3)
    pdf.set_font('Arial', '', 7)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(36, 4, label, 0, 1, 'C')
    pdf.set_xy(x + 2, y + 12)
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(30, 55, 80)
    pdf.cell(36, 6, value, 0, 1, 'C')
    if (i + 1) % 4 == 0:
        pdf.ln(32)

# PAGE 2 - DEMOGRAPHIC ANALYSIS
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '1. Demographic Analysis', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/demographic_analysis.png'):
    try:
        pdf.image('output/demographic_analysis.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 6, 'Figure 1: Gender, Age Distribution, and Top Countries', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Average Patient Age: 44.8 years')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Age Range: 1 to 90 years')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Most vulnerable: 46-60 years (31.3% of cases)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Age group 60+ accounts for 21.0% of cases')

# PAGE 3 - INFECTION PATTERNS
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '2. Infection Patterns', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/infection_patterns.png'):
    try:
        pdf.image('output/infection_patterns.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 6, 'Figure 2: Infection Sources and Contact Exposure', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Primary Source: Contact with confirmed case (34.8%)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Travel history: 25.0% of cases')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Community spread: 22.0% of cases')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Average contacts per patient: 5.0 individuals')

# PAGE 4 - RECOVERY TRENDS
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '3. Recovery Trends', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/recovery_trends.png'):
    try:
        pdf.image('output/recovery_trends.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 6, 'Figure 3: Recovery Time Distribution', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Recovery Rate: 68.4% (3,422 patients)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Average Recovery Time: 12.8 days')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Median Recovery Time: 12 days')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Older patients (60+) take 15.2 days vs 10.2 days for young')

# PAGE 5 - REGIONAL IMPACT
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '4. Regional Impact', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/regional_impact.png'):
    try:
        pdf.image('output/regional_impact.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 6, 'Figure 4: Top Affected Regions', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Most Affected: Maharashtra (348 cases, 7.0%)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Second: New York (347 cases)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Third: Sao Paulo (346 cases)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Outcomes: 68.4% recovered, 20.4% active, 11.2% deceased')

# PAGE 6 - FACTORS
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '5. Factors Influencing Recovery', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/recovery_factors.png'):
    try:
        pdf.image('output/recovery_factors.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 6, 'Figure 5: Age vs Recovery Time Correlation', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Findings:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Age Correlation: +0.42 (moderate positive)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Contact Number Correlation: +0.18')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Each year of age adds 0.12 days to recovery')

# PAGE 7 - REGRESSION
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, '6. Predictive Model', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(6)

if os.path.exists('output/regression_model.png'):
    try:
        pdf.image('output/regression_model.png', x=20, w=170)
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 6, 'Figure 6: Actual vs Predicted Recovery Time', 0, 1, 'C')
        pdf.ln(5)
    except:
        pass

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Model Performance:', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- R2 Score: 0.176 (explains 17.6% of variance)')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- RMSE: 4.8 days')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Age Coefficient: +0.12 days per year')

# PAGE 8 - RECOMMENDATIONS
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, 'Strategic Recommendations', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(8)

recs = [
    '1. SCREENING PRIORITIZATION - Focus on 45+ age group',
    '2. CONTACT TRACING - Expand capacity for high-contact individuals',
    '3. RESOURCE ALLOCATION - Concentrate on Maharashtra, New York, Sao Paulo',
    '4. AGE-SPECIFIC PROTOCOLS - Elderly need extended monitoring',
    '5. EARLY WARNING - Strengthen surveillance in high-risk regions'
]

pdf.set_font('Arial', '', 10)
for rec in recs:
    pdf.cell(8, 7, '', 0, 0)
    pdf.multi_cell(0, 6, rec)
    pdf.ln(2)

# PAGE 9 - CONCLUSION
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(30, 55, 80)
pdf.cell(0, 12, 'Conclusion', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(8)

conclusion = """This analysis provides actionable insights for public health decision-making during infectious disease outbreaks. Key findings include age as a significant recovery factor, contact tracing as a primary intervention, and targeted regional resource allocation."""
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, conclusion)

pdf.ln(12)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Report Summary', 0, 1, 'L')
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(5)

pdf.set_font('Arial', '', 10)
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Total Cases: 5,000')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Recovery Rate: 68.4%')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Average Recovery: 12.8 days')
pdf.cell(8, 6, '', 0, 0)
pdf.multi_cell(0, 5, '- Primary Source: Contact with confirmed case (34.8%)')

pdf.ln(8)
pdf.set_font('Arial', 'I', 9)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 5, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')

# Save PDF
pdf.output('HealthGuard_Perfect_Report.pdf')
print("\n" + "="*60)
print("PDF CREATED SUCCESSFULLY!")
print("="*60)
print("\nFile: HealthGuard_Perfect_Report.pdf")