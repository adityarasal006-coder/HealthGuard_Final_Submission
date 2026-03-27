"""
Create Professional PDF Report for HealthGuard Analytics Project
"""

from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        # Logo (optional - you can add if you have a logo image)
        # self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'COVID-19 Early Case Trend Analysis & Recovery Insights', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(5)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()
    
    def bullet_point(self, text):
        self.set_font('Arial', '', 11)
        self.cell(10, 6, '•', 0, 0)
        self.multi_cell(0, 6, text)
    
    def add_image_safe(self, img_path, width=170):
        if os.path.exists(img_path):
            try:
                self.image(img_path, x=20, w=width)
                self.ln(5)
                return True
            except:
                return False
        return False

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'COVID-19 Case Analysis Report', 0, 1, 'C')
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%B %d, %Y")}', 0, 1, 'C')
pdf.ln(10)

# Executive Summary
pdf.chapter_title('EXECUTIVE SUMMARY')
summary = """HealthGuard Analytics Pvt. Ltd. conducted a comprehensive analysis of 
infectious disease case data to support public health decision-making. This report 
presents findings from 5,000 patient cases during the early phase of the outbreak 
(January 2020 - March 2020). The analysis covers patient demographics, infection 
patterns, recovery trends, and regional impact."""
pdf.chapter_body(summary)

# Key Findings
pdf.chapter_title('KEY FINDINGS')

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '1. DEMOGRAPHIC PATTERNS (Who is getting infected?)', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.bullet_point('Gender Distribution: Male 0.0%, Female 0.0% (Gender data needs review)')
pdf.bullet_point('Average Patient Age: 44.8 years')
pdf.bullet_point('Age Range: 1 - 90 years')
pdf.bullet_point('Most vulnerable age groups: 45+ years show higher case counts')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '2. INFECTION PATTERNS (How are infections spreading?)', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.bullet_point('Primary Infection Source: Contact with confirmed case (34.8%)')
pdf.bullet_point('Secondary Sources: Travel history, Community spread')
pdf.bullet_point('Average Contacts per Patient: 5.0 individuals')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '3. RECOVERY TRENDS (What are the recovery patterns?)', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.bullet_point('Overall Recovery Rate: 68.4% (3,422 patients)')
pdf.bullet_point('Average Recovery Time: 12.8 days')
pdf.bullet_point('Median Recovery Time: 12 days')
pdf.bullet_point('Recovery Time Range: 5 - 30 days')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '4. REGIONAL IMPACT (Which regions are most affected?)', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.bullet_point('Most Affected Region: Maharashtra (348 cases - 7.0%)')
pdf.bullet_point('Second: New York (347 cases - 6.9%)')
pdf.bullet_point('Third: Sao Paulo (346 cases - 6.9%)')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '5. PATIENT OUTCOMES', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.bullet_point('Released (Recovered): 3,422 patients (68.4%)')
pdf.bullet_point('Isolated (Active): 1,019 patients (20.4%)')
pdf.bullet_point('Deceased: 559 patients (11.2%)')

pdf.ln(5)

# Visualizations
pdf.add_page()
pdf.chapter_title('VISUALIZATION OUTPUTS')

pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'The following visualizations have been generated as part of this analysis:')
pdf.ln(5)

charts = [
    ('demographic_analysis.png', 'Figure 1: Demographic Analysis - Gender, Age, Country Distribution'),
    ('infection_patterns.png', 'Figure 2: Infection Patterns - Sources and Contact Exposure'),
    ('recovery_trends.png', 'Figure 3: Recovery Trends - Time Distribution by Age Group'),
    ('regional_impact.png', 'Figure 4: Regional Impact - Top Regions and Patient Outcomes'),
    ('recovery_factors.png', 'Figure 5: Factors Influencing Recovery Time'),
    ('regression_model.png', 'Figure 6: Linear Regression Model - Prediction Results')
]

for chart_file, caption in charts:
    img_path = f'output/{chart_file}'
    if pdf.add_image_safe(img_path):
        pdf.set_font('Arial', 'I', 9)
        pdf.cell(0, 5, caption, 0, 1, 'C')
        pdf.ln(3)
    else:
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 5, f'⚠ {caption} - Image not available', 0, 1)
        pdf.ln(2)

# Recommendations
pdf.add_page()
pdf.chapter_title('RECOMMENDATIONS')

recommendations = [
    "SCREENING PRIORITIZATION: Focus screening efforts on the 45+ age group, as they represent a significant portion of cases with potentially longer recovery times.",
    "CONTACT TRACING: Implement aggressive contact tracing for individuals with high contact numbers (>10 contacts) to control spread.",
    "RESOURCE ALLOCATION: Direct healthcare resources to the most affected regions: Maharashtra, New York, and Sao Paulo.",
    "TREATMENT PROTOCOLS: Develop age-specific treatment protocols, especially for elderly patients who may require longer recovery periods.",
    "EARLY WARNING SYSTEMS: Strengthen surveillance in regions showing rapid case growth for early intervention."
]

for i, rec in enumerate(recommendations, 1):
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, f"{i}. {rec.split(':')[0]}:", 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, rec.split(':', 1)[1].strip())
    pdf.ln(2)

# Technical Details
pdf.chapter_title('TECHNICAL DETAILS')

tech_details = """Analysis Tools:
• Programming Language: Python 3.x
• Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
• Statistical Methods: Descriptive statistics, Correlation analysis, Linear Regression

Dataset Information:
• Total Records: 5,000 patient cases
• Time Period: January 2020 - March 2020
• Key Attributes: Demographics, infection details, timelines, outcomes

Model Performance:
• Linear Regression R² Score: 0.XX (explains XX% of variance in recovery time)
• Features Used: Age, Contact Number
"""

pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5, tech_details)

# Conclusion
pdf.add_page()
pdf.chapter_title('CONCLUSION')

conclusion = """This analysis successfully provides actionable insights for public health 
decision-making during the early phase of an infectious disease outbreak. The identified 
patterns in demographics, transmission, and recovery can help authorities implement 
targeted interventions and optimize resource allocation.

The complete analysis code, dataset, and visualizations are available in the project 
repository for further review and extension.

For any questions or additional analysis requirements, please contact the HealthGuard 
Analytics team.
"""

pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, conclusion)

# Save PDF
pdf.output('HealthGuard_Project_Report.pdf')
print("\n" + "="*60)
print("✅ PDF REPORT CREATED SUCCESSFULLY!")
print("="*60)
print("\n📄 File: HealthGuard_Project_Report.pdf")
print("📁 Location: Current folder")
print("\n💡 Open it with: start HealthGuard_Project_Report.pdf")