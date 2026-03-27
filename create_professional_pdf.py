"""
Professional PDF Report Generator for HealthGuard Analytics
Advanced Styling with Colors, Tables, and Modern Design
"""

from fpdf import FPDF
from datetime import datetime
import os

class ProfessionalPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        
    def header(self):
        # Gradient effect with colored background
        self.set_fill_color(30, 60, 90)  # Dark blue header
        self.rect(0, 0, 210, 35, 'F')
        
        # Company Logo Text
        self.set_font('Arial', 'B', 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 20, 'HealthGuard Analytics', 0, 1, 'C')
        
        self.set_font('Arial', 'I', 10)
        self.set_text_color(200, 200, 200)
        self.cell(0, 5, 'Data-Driven Public Health Insights', 0, 1, 'C')
        
        # Decorative line
        self.set_draw_color(100, 150, 200)
        self.line(20, 35, 190, 35)
        
        self.set_y(40)
        
    def footer(self):
        self.set_y(-20)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Confidential Report - Page ' + str(self.page_no()), 0, 0, 'C')
        
        # Add date
        self.set_y(-20)
        self.set_x(150)
        self.cell(0, 10, datetime.now().strftime('%B %d, 2026'), 0, 0, 'R')
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 60, 90)
        self.set_fill_color(230, 240, 250)
        self.cell(0, 12, title, 0, 1, 'L', 1)
        self.set_draw_color(30, 60, 90)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(5)
    
    def subsection_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(50, 80, 110)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(2)
    
    def add_stat_card(self, title, value, description='', x=None):
        if x is None:
            x = self.get_x()
        y = self.get_y()
        
        # Card background
        self.set_fill_color(248, 249, 250)
        self.set_draw_color(220, 220, 220)
        self.rect(x, y, 85, 45, 'FD')
        
        # Title
        self.set_font('Arial', '', 9)
        self.set_text_color(100, 100, 100)
        self.set_xy(x + 5, y + 5)
        self.cell(75, 5, title, 0, 1, 'L')
        
        # Value
        self.set_font('Arial', 'B', 18)
        self.set_text_color(30, 60, 90)
        self.set_xy(x + 5, y + 12)
        self.cell(75, 10, value, 0, 1, 'L')
        
        # Description
        self.set_font('Arial', '', 7)
        self.set_text_color(150, 150, 150)
        self.set_xy(x + 5, y + 28)
        self.cell(75, 5, description, 0, 1, 'L')
        
        return y + 50
    
    def add_table(self, headers, data):
        self.set_font('Arial', 'B', 9)
        self.set_fill_color(30, 60, 90)
        self.set_text_color(255, 255, 255)
        
        # Table header
        col_width = 180 / len(headers)
        for header in headers:
            self.cell(col_width, 8, header, 1, 0, 'C', 1)
        self.ln()
        
        # Table data
        self.set_font('Arial', '', 9)
        self.set_text_color(0, 0, 0)
        fill = False
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_width, 7, str(item), 'LR', 0, 'L', fill)
            self.ln()
            fill = not fill
        
        # Bottom line
        self.cell(col_width * len(headers), 0, '', 'T')
        self.ln()
    
    def add_insight_box(self, text):
        self.set_fill_color(255, 245, 225)
        self.set_draw_color(255, 200, 100)
        self.rect(self.get_x(), self.get_y(), 170, 20, 'FD')
        
        self.set_font('Arial', 'I', 9)
        self.set_text_color(100, 80, 40)
        self.set_xy(self.get_x() + 5, self.get_y() + 3)
        self.multi_cell(160, 5, text)
        
        self.set_y(self.get_y() + 15)
        self.ln(5)

# Create PDF
pdf = ProfessionalPDF()
pdf.add_page()

# ============================================================================
# COVER PAGE
# ============================================================================

# Cover Page Design
pdf.set_fill_color(30, 60, 90)
pdf.rect(0, 0, 210, 297, 'F')

# Main Title
pdf.set_y(80)
pdf.set_font('Arial', 'B', 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 20, 'COVID-19', 0, 1, 'C')
pdf.set_font('Arial', 'B', 24)
pdf.cell(0, 15, 'Early Case Trend Analysis', 0, 1, 'C')
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'and Recovery Insights', 0, 1, 'C')

# Subtitle
pdf.set_y(140)
pdf.set_font('Arial', '', 12)
pdf.set_text_color(200, 200, 200)
pdf.cell(0, 8, 'A Data-Driven Report for Public Health Authorities', 0, 1, 'C')

# Company and Date
pdf.set_y(200)
pdf.set_font('Arial', '', 10)
pdf.cell(0, 6, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.cell(0, 6, datetime.now().strftime('%B %d, 2026'), 0, 1, 'C')

pdf.add_page()

# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================

pdf.section_title('Executive Summary')
pdf.set_font('Arial', '', 11)
pdf.set_text_color(50, 50, 50)
exec_summary = """This comprehensive analysis examines 5,000 patient cases from the early phase 
of the COVID-19 outbreak (January - March 2020). The study provides critical insights into 
demographic patterns, infection transmission dynamics, recovery timelines, and regional 
impact to support evidence-based public health decision-making."""
pdf.multi_cell(0, 7, exec_summary)

pdf.ln(5)

# Key Stats Cards
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Key Statistics at a Glance', 0, 1, 'L')
pdf.ln(3)

# Row 1
pdf.set_x(25)
pdf.add_stat_card('Total Cases', '5,000', 'analyzed patients', 25)
pdf.add_stat_card('Recovery Rate', '68.4%', 'of total cases', 110)
pdf.ln(50)

pdf.set_x(25)
pdf.add_stat_card('Avg Recovery Time', '12.8 days', 'median: 12 days', 25)
pdf.add_stat_card('Avg Patient Age', '44.8 years', 'range: 1-90 years', 110)
pdf.ln(50)

pdf.set_x(25)
pdf.add_stat_card('Deceased', '559', '11.2% of cases', 25)
pdf.add_stat_card('Active Cases', '1,019', '20.4% isolated', 110)

pdf.ln(15)

# Insight Box
pdf.add_insight_box('KEY INSIGHT: Contact with confirmed cases accounts for 34.8% of infections, highlighting the critical importance of contact tracing.')

# ============================================================================
# DEMOGRAPHIC ANALYSIS
# ============================================================================

pdf.add_page()
pdf.section_title('Demographic Analysis')
pdf.subsection_title('Who is Getting Infected?')

pdf.set_font('Arial', '', 10)
pdf.set_text_color(60, 60, 60)

# Age Distribution
pdf.subsection_title('Age Distribution')
age_data = [
    ['Age Group', 'Cases', 'Percentage'],
    ['0-18 years', '245', '4.9%'],
    ['19-30 years', '892', '17.8%'],
    ['31-45 years', '1,245', '24.9%'],
    ['46-60 years', '1,567', '31.3%'],
    ['60+ years', '1,051', '21.0%']
]
pdf.add_table(['Age Group', 'Cases', 'Percentage'], age_data[1:])

pdf.ln(5)

# Gender Distribution
pdf.subsection_title('Gender Distribution')
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 6, 'Note: Gender data requires further validation as significant missing values were detected.')
pdf.ln(3)

# Infection Sources
pdf.subsection_title('Primary Infection Sources')
infection_data = [
    ['Infection Source', 'Cases', 'Percentage'],
    ['Contact with confirmed case', '1,740', '34.8%'],
    ['Travel history', '1,250', '25.0%'],
    ['Community spread', '1,100', '22.0%'],
    ['Healthcare worker', '350', '7.0%'],
    ['Mass gathering', '300', '6.0%'],
    ['Family cluster', '260', '5.2%']
]
pdf.add_table(['Infection Source', 'Cases', 'Percentage'], infection_data[1:])

pdf.add_insight_box('INSIGHT: Contact with confirmed cases is the dominant transmission mode, suggesting that breaking transmission chains through contact tracing and isolation is critical.')

# ============================================================================
# RECOVERY ANALYSIS
# ============================================================================

pdf.add_page()
pdf.section_title('Recovery Analysis')

pdf.subsection_title('Recovery Timeline Statistics')

# Recovery Stats Table
recovery_data = [
    ['Metric', 'Value', 'Interpretation'],
    ['Recovery Rate', '68.4%', '3,422 patients recovered'],
    ['Average Recovery Time', '12.8 days', 'Typical recovery duration'],
    ['Median Recovery Time', '12 days', 'Half recover within 12 days'],
    ['Minimum Recovery', '5 days', 'Fastest recovery'],
    ['Maximum Recovery', '30 days', 'Longest recovery'],
    ['Standard Deviation', '5.2 days', 'Moderate variability']
]
pdf.add_table(['Metric', 'Value', 'Interpretation'], recovery_data[1:])

pdf.ln(8)

# Recovery by Age Group
pdf.subsection_title('Recovery Time by Age Group')
recovery_age = [
    ['Age Group', 'Avg Recovery (days)', 'Sample Size'],
    ['0-18 years', '10.2', '185'],
    ['19-30 years', '11.5', '612'],
    ['31-45 years', '12.4', '856'],
    ['46-60 years', '13.8', '1,078'],
    ['60+ years', '15.2', '691']
]
pdf.add_table(['Age Group', 'Avg Recovery (days)', 'Sample Size'], recovery_age[1:])

pdf.ln(5)
pdf.add_insight_box('CLINICAL INSIGHT: Older patients (60+ years) require approximately 50% longer recovery time compared to younger patients (0-18 years), indicating the need for age-specific care protocols.')

# ============================================================================
# REGIONAL IMPACT
# ============================================================================

pdf.add_page()
pdf.section_title('Regional Impact Analysis')

pdf.subsection_title('Most Affected Regions')

region_data = [
    ['Rank', 'Region', 'Cases', 'Percentage'],
    ['1', 'Maharashtra', '348', '7.0%'],
    ['2', 'New York', '347', '6.9%'],
    ['3', 'Sao Paulo', '346', '6.9%'],
    ['4', 'Rajasthan', '344', '6.9%'],
    ['5', 'Gujarat', '343', '6.9%'],
    ['6', 'Delhi', '341', '6.8%'],
    ['7', 'California', '339', '6.8%'],
    ['8', 'Tamil Nadu', '337', '6.7%'],
    ['9', 'Texas', '335', '6.7%'],
    ['10', 'Florida', '330', '6.6%']
]
pdf.add_table(['Rank', 'Region', 'Cases', 'Percentage'], region_data[1:])

pdf.ln(8)

# Outcomes Summary
pdf.subsection_title('Patient Outcomes by Region')
outcome_data = [
    ['Outcome', 'Count', 'Percentage'],
    ['Recovered (Released)', '3,422', '68.4%'],
    ['Active (Isolated)', '1,019', '20.4%'],
    ['Deceased', '559', '11.2%']
]
pdf.add_table(['Outcome', 'Count', 'Percentage'], outcome_data[1:])

pdf.add_insight_box('RESOURCE ALLOCATION: The top 10 regions account for over 68% of all cases, suggesting targeted resource deployment could significantly impact outbreak control.')

# ============================================================================
# FACTORS INFLUENCING RECOVERY
# ============================================================================

pdf.add_page()
pdf.section_title('Factors Influencing Recovery')

pdf.subsection_title('Correlation Analysis')

correlation_data = [
    ['Factor', 'Correlation Coefficient', 'Interpretation'],
    ['Age', '+0.42', 'Moderate positive correlation - older patients take longer to recover'],
    ['Contact Number', '+0.18', 'Weak positive correlation - more contacts slightly increase recovery time']
]
pdf.add_table(['Factor', 'Correlation Coefficient', 'Interpretation'], correlation_data[1:])

pdf.ln(8)

pdf.subsection_title('Linear Regression Model Performance')

model_data = [
    ['Metric', 'Value', 'Interpretation'],
    ['R2 Score', '0.176', 'Model explains 17.6% of variance in recovery time'],
    ['RMSE', '4.8 days', 'Average prediction error is 4.8 days'],
    ['Age Coefficient', '+0.12 days/year', 'Each year of age adds 0.12 days to recovery'],
    ['Contact Coefficient', '+0.08 days/contact', 'Each additional contact adds 0.08 days to recovery']
]
pdf.add_table(['Metric', 'Value', 'Interpretation'], model_data[1:])

pdf.ln(5)
pdf.add_insight_box('MODEL INSIGHT: Age is the most significant predictor of recovery time, explaining approximately 18% of the variation. Other factors like underlying conditions may contribute to the remaining variance.')

# ============================================================================
# RECOMMENDATIONS
# ============================================================================

pdf.add_page()
pdf.section_title('Strategic Recommendations')

pdf.set_font('Arial', 'B', 11)
pdf.set_text_color(30, 60, 90)

recommendations = [
    ('1. SCREENING PRIORITIZATION', 'Focus screening efforts on the 45+ age group, which shows higher case counts and longer recovery times. Implement targeted testing in senior communities and healthcare facilities.'),
    ('2. CONTACT TRACING ENHANCEMENT', 'With 34.8% of cases linked to contact with confirmed patients, expand contact tracing capacity. Prioritize individuals with more than 10 contacts for rapid testing and quarantine.'),
    ('3. REGIONAL RESOURCE ALLOCATION', 'Concentrate healthcare resources in Maharashtra, New York, and Sao Paulo which account for nearly 21% of all cases. Establish surge capacity in these regions.'),
    ('4. AGE-SPECIFIC PROTOCOLS', 'Develop treatment protocols based on age groups. Elderly patients require extended monitoring (15+ days) while younger patients may recover faster with standard care.'),
    ('5. EARLY WARNING SYSTEM', 'Strengthen surveillance in regions showing rapid case growth. Implement real-time monitoring of contact networks to identify super-spreader events early.')
]

for title, description in recommendations:
    pdf.set_font('Arial', 'B', 10)
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

conclusion_text = """The analysis successfully provides actionable insights for public health 
decision-making during the early phase of an infectious disease outbreak. Key findings 
demonstrate that:

- Age is a significant factor in recovery time, with elderly patients requiring 
  extended care periods
- Contact tracing should be prioritized as the primary intervention strategy
- Regional resource allocation can be optimized based on case distribution
- The linear regression model provides a foundation for predicting recovery timelines

These insights can help authorities implement targeted interventions, optimize 
resource allocation, and improve patient outcomes during future outbreaks."""

pdf.set_font('Arial', '', 11)
pdf.set_text_color(50, 50, 50)
pdf.multi_cell(0, 7, conclusion_text)

pdf.ln(10)

# Closing
pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, 'For additional analysis or customization requests, please contact:', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 6, 'HealthGuard Analytics Pvt. Ltd. | analytics@healthguard.com', 0, 1, 'C')

# Save PDF
try:
    pdf.output('HealthGuard_Professional_Report.pdf')
    print("\n" + "="*70)
    print("PROFESSIONAL PDF REPORT CREATED SUCCESSFULLY!")
    print("="*70)
    print("\nFile: HealthGuard_Professional_Report.pdf")
    print("Location: C:\\Users\\ASUS\\healthguard_project")
    print("\nReport Features:")
    print("   - Professional cover page with branding")
    print("   - Color-coded statistics cards")
    print("   - Formatted data tables")
    print("   - Insight boxes with key takeaways")
    print("   - Strategic recommendations section")
    print("\nTo open, type: start HealthGuard_Professional_Report.pdf")
except Exception as e:
    print(f"\nError: {e}")