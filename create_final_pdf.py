"""
Simple PDF Report Creator - Fixed Version
"""

from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'COVID-19 Early Case Trend Analysis & Recovery Insights', 0, 1, 'C')
        self.ln(8)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)
    
    def add_text(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 6, text)
        self.ln(2)
    
    def add_bullet(self, text):
        self.set_font('Arial', '', 10)
        self.cell(8, 6, '-', 0, 0)
        self.multi_cell(0, 6, text)

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'COVID-19 Case Analysis Report', 0, 1, 'C')
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%B %d, 2026")}', 0, 1, 'C')
pdf.ln(8)

# Executive Summary
pdf.section_title('EXECUTIVE SUMMARY')
summary = """HealthGuard Analytics Pvt. Ltd. conducted a comprehensive analysis of 
infectious disease case data to support public health decision-making. This report 
presents findings from 5,000 patient cases during the early phase of the outbreak 
(January 2020 - March 2020)."""
pdf.add_text(summary)

# Key Findings
pdf.section_title('KEY FINDINGS')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '1. DEMOGRAPHIC PATTERNS (Who is getting infected?)', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.add_bullet('Average Patient Age: 44.8 years')
pdf.add_bullet('Age Range: 1 to 90 years')
pdf.add_bullet('Most vulnerable age group: 45+ years')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '2. INFECTION PATTERNS (How are infections spreading?)', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.add_bullet('Primary Infection Source: Contact with confirmed case (34.8%)')
pdf.add_bullet('Average Contacts per Patient: 5.0 individuals')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '3. RECOVERY TRENDS (What are the recovery patterns?)', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.add_bullet('Overall Recovery Rate: 68.4% (3,422 patients)')
pdf.add_bullet('Average Recovery Time: 12.8 days')
pdf.add_bullet('Median Recovery Time: 12 days')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '4. REGIONAL IMPACT (Which regions are most affected?)', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.add_bullet('Most Affected Region: Maharashtra (348 cases - 7.0%)')
pdf.add_bullet('Second: New York (347 cases - 6.9%)')
pdf.add_bullet('Third: Sao Paulo (346 cases - 6.9%)')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '5. PATIENT OUTCOMES', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.add_bullet('Released (Recovered): 3,422 patients (68.4%)')
pdf.add_bullet('Isolated (Active): 1,019 patients (20.4%)')
pdf.add_bullet('Deceased: 559 patients (11.2%)')

# Recommendations
pdf.add_page()
pdf.section_title('RECOMMENDATIONS')

recommendations = [
    "SCREENING PRIORITIZATION: Focus screening efforts on the 45+ age group, as they represent a significant portion of cases.",
    "CONTACT TRACING: Implement aggressive contact tracing for individuals with high contact numbers (more than 10 contacts).",
    "RESOURCE ALLOCATION: Direct healthcare resources to the most affected regions: Maharashtra, New York, and Sao Paulo.",
    "TREATMENT PROTOCOLS: Develop age-specific treatment protocols, especially for elderly patients.",
    "EARLY WARNING SYSTEMS: Strengthen surveillance in regions showing rapid case growth for early intervention."
]

for i, rec in enumerate(recommendations, 1):
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 7, f"{i}. {rec.split(':')[0]}:", 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, rec.split(':', 1)[1].strip())
    pdf.ln(2)

# Visualizations
pdf.add_page()
pdf.section_title('VISUALIZATION OUTPUTS')

pdf.set_font('Arial', '', 10)
pdf.add_text('The following visualizations have been generated as part of this analysis:')
pdf.ln(5)

# Add images
charts = [
    'demographic_analysis.png',
    'infection_patterns.png', 
    'recovery_trends.png',
    'regional_impact.png',
    'recovery_factors.png',
    'regression_model.png'
]

for i, chart in enumerate(charts, 1):
    img_path = f'output/{chart}'
    if os.path.exists(img_path):
        try:
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(0, 8, f"Figure {i}: {chart.replace('_', ' ').replace('.png', '')}", 0, 1)
            pdf.image(img_path, x=20, w=170)
            pdf.ln(5)
        except Exception as e:
            pdf.set_font('Arial', '', 10)
            pdf.add_text(f"Image {chart} could not be loaded: {str(e)}")
            pdf.ln(2)
    else:
        pdf.set_font('Arial', '', 10)
        pdf.add_text(f"Image not found: {chart}")
        pdf.ln(2)

# Technical Details
pdf.add_page()
pdf.section_title('TECHNICAL DETAILS')

tech_text = """
Analysis Tools:
- Programming Language: Python 3.x
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- Statistical Methods: Descriptive statistics, Correlation analysis, Linear Regression

Dataset Information:
- Total Records: 5,000 patient cases
- Time Period: January 2020 - March 2020
- Key Attributes: Demographics, infection details, timelines, outcomes

Model Performance:
- Linear Regression Model trained on age and contact number features
- Model evaluates factors influencing recovery time
"""
pdf.add_text(tech_text)

# Conclusion
pdf.section_title('CONCLUSION')

conclusion_text = """This analysis successfully provides actionable insights for public health 
decision-making during the early phase of an infectious disease outbreak. The identified 
patterns in demographics, transmission, and recovery can help authorities implement 
targeted interventions and optimize resource allocation.

The complete analysis code, dataset, and visualizations are available for review and 
further analysis.

For any questions or additional analysis requirements, please contact the HealthGuard 
Analytics team.
"""
pdf.add_text(conclusion_text)

# Save PDF
try:
    pdf.output('HealthGuard_Project_Report.pdf')
    print("\n" + "="*60)
    print("✅ PDF REPORT CREATED SUCCESSFULLY!")
    print("="*60)
    print("\n📄 File: HealthGuard_Project_Report.pdf")
    print("📁 Location: C:\\Users\\ASUS\\healthguard_project")
    print("\n💡 To open, type: start HealthGuard_Project_Report.pdf")
except Exception as e:
    print(f"\n❌ Error creating PDF: {e}")
    print("\nTrying alternative method...")
    
    # Alternative: Create without special formatting
    pdf2 = FPDF()
    pdf2.add_page()
    pdf2.set_font('Arial', '', 12)
    pdf2.cell(0, 10, 'HealthGuard Analytics - COVID-19 Report', 0, 1, 'C')
    pdf2.cell(0, 10, f'Generated: {datetime.now().strftime("%B %d, 2026")}', 0, 1, 'C')
    pdf2.ln(10)
    pdf2.multi_cell(0, 6, 'Key Findings:')
    pdf2.multi_cell(0, 6, '- Average Age: 44.8 years')
    pdf2.multi_cell(0, 6, '- Recovery Rate: 68.4%')
    pdf2.multi_cell(0, 6, '- Average Recovery Time: 12.8 days')
    pdf2.multi_cell(0, 6, '- Most Affected Region: Maharashtra (348 cases)')
    pdf2.output('HealthGuard_Project_Report.pdf')
    print("✅ Simple PDF created: HealthGuard_Project_Report.pdf")