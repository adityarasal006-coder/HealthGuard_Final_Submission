"""
FINAL FIXED PROFESSIONAL PDF REPORT
HealthGuard Analytics - No Empty Pages, Proper Spacing
"""

from fpdf import FPDF
from datetime import datetime
import os

class FixedPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=28)
        
    def header(self):
        if self.page_no() > 1:
            self.set_fill_color(20, 50, 75)
            self.rect(0, 0, 210, 22, 'F')
            
            self.set_font('Arial', 'B', 11)
            self.set_text_color(255, 215, 0)
            self.set_xy(15, 6)
            self.cell(30, 6, 'HGA', 0, 0, 'L')
            
            self.set_font('Arial', '', 9)
            self.set_text_color(220, 220, 220)
            self.cell(60, 6, 'HealthGuard Analytics', 0, 0, 'L')
            
            self.set_font('Arial', 'I', 8)
            self.set_xy(130, 6)
            self.cell(65, 6, 'COVID-19 Analysis', 0, 1, 'R')
            
            self.set_draw_color(255, 215, 0)
            self.line(15, 20, 195, 20)
            self.set_y(28)
    
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-18)
            self.set_font('Arial', 'I', 7)
            self.set_text_color(120, 120, 140)
            self.set_x(15)
            self.cell(50, 6, 'Confidential', 0, 0, 'L')
            self.set_x(85)
            self.cell(40, 6, f'Page {self.page_no()}', 0, 0, 'C')
            self.set_x(145)
            self.cell(50, 6, datetime.now().strftime('%d %b %Y'), 0, 0, 'R')
    
    def cover_page(self):
        self.set_fill_color(10, 35, 55)
        self.rect(0, 0, 210, 297, 'F')
        
        self.set_draw_color(255, 200, 50)
        self.set_line_width(2)
        self.line(0, 0, 210, 0)
        self.line(0, 287, 210, 287)
        
        self.set_y(85)
        self.set_font('Arial', 'B', 36)
        self.set_text_color(255, 215, 0)
        self.cell(0, 20, 'COVID-19', 0, 1, 'C')
        
        self.set_font('Arial', 'B', 28)
        self.set_text_color(255, 255, 255)
        self.cell(0, 15, 'Early Case Trend Analysis', 0, 1, 'C')
        
        self.set_font('Arial', 'B', 26)
        self.cell(0, 15, 'and Recovery Insights', 0, 1, 'C')
        
        self.set_draw_color(255, 215, 0)
        self.line(60, 148, 150, 148)
        
        self.set_y(165)
        self.set_font('Arial', '', 11)
        self.set_text_color(200, 200, 210)
        self.cell(0, 7, 'A Data-Driven Report for Public Health Authorities', 0, 1, 'C')
        
        self.set_y(230)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(255, 215, 0)
        self.cell(0, 10, 'HealthGuard Analytics', 0, 1, 'C')
        
        self.set_font('Arial', '', 10)
        self.set_text_color(180, 180, 200)
        self.cell(0, 6, 'Pvt. Ltd.', 0, 1, 'C')
        self.set_y(260)
        self.cell(0, 6, datetime.now().strftime('%B %d, 2026'), 0, 1, 'C')
    
    def section_title(self, title, number=''):
        self.set_font('Arial', 'B', 18)
        self.set_text_color(10, 45, 70)
        if number:
            self.cell(0, 10, f'{number}  {title}', 0, 1, 'L')
        else:
            self.cell(0, 10, title, 0, 1, 'L')
        self.set_draw_color(255, 180, 40)
        self.line(15, self.get_y(), 85, self.get_y())
        self.set_draw_color(200, 200, 220)
        self.line(88, self.get_y(), 195, self.get_y())
        self.ln(6)
    
    def subsection(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(30, 70, 100)
        self.cell(0, 7, title, 0, 1, 'L')
        self.ln(2)
    
    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(55, 55, 65)
        self.multi_cell(0, 5, text)
        self.ln(3)
    
    def bullet(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(55, 55, 65)
        self.cell(6, 5, '-', 0, 0)
        self.multi_cell(0, 5, text)
    
    def stat_card(self, x, y, title, value, subtitle=''):
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(210, 210, 225)
        self.rect(x, y, 55, 42, 'FD')
        self.set_fill_color(255, 180, 40)
        self.rect(x, y, 55, 4, 'F')
        
        self.set_xy(x + 3, y + 8)
        self.set_font('Arial', '', 7)
        self.set_text_color(100, 100, 120)
        self.cell(49, 4, title, 0, 1, 'C')
        
        self.set_xy(x + 3, y + 16)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(10, 45, 70)
        self.cell(49, 7, value, 0, 1, 'C')
        
        if subtitle:
            self.set_xy(x + 3, y + 28)
            self.set_font('Arial', '', 6)
            self.set_text_color(130, 130, 150)
            self.cell(49, 4, subtitle, 0, 1, 'C')
    
    def insight(self, text):
        self.set_fill_color(250, 248, 240)
        self.set_draw_color(255, 200, 100)
        self.rect(18, self.get_y(), 174, 18, 'FD')
        self.set_xy(22, self.get_y() + 4)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(100, 80, 40)
        self.multi_cell(166, 4, f'"{text}"')
        self.set_y(self.get_y() + 8)
    
    def add_chart_small(self, img_path, caption, fig_num):
        if os.path.exists(img_path):
            try:
                self.image(img_path, x=20, w=170)
                self.ln(3)
                self.set_font('Arial', 'I', 7)
                self.set_text_color(100, 100, 120)
                self.cell(0, 5, f'Figure {fig_num}: {caption}', 0, 1, 'C')
                self.ln(5)
                return True
            except:
                self.set_font('Arial', '', 8)
                self.cell(0, 6, f'[Figure {fig_num}: {caption}]', 0, 1, 'C')
                self.ln(5)
                return False
        return False

# Create PDF
pdf = FixedPDF()
pdf.add_page()
pdf.cover_page()

# ============================================================================
# PAGE 1: EXECUTIVE SUMMARY
# ============================================================================
pdf.add_page()
pdf.section_title('Executive Summary', '01')

summary_text = """This comprehensive analysis examines 5,000 patient cases from the early phase of the COVID-19 outbreak (January - March 2020). The study provides critical insights into demographic patterns, infection transmission dynamics, recovery timelines, and regional impact to support evidence-based public health decision-making."""
pdf.body_text(summary_text)

pdf.subsection('Key Performance Indicators')

# Statistics Cards - Row 1
y_start = pdf.get_y()
pdf.stat_card(18, y_start, 'Total Cases', '5,000', 'analyzed')
pdf.stat_card(77, y_start, 'Recovery Rate', '68.4%', 'of total')
pdf.stat_card(136, y_start, 'Recovered', '3,422', 'patients')
pdf.set_y(y_start + 48)

# Row 2
y_start = pdf.get_y()
pdf.stat_card(18, y_start, 'Avg Recovery', '12.8 d', 'mean')
pdf.stat_card(77, y_start, 'Avg Age', '44.8 y', 'average')
pdf.stat_card(136, y_start, 'Deceased', '559', '11.2%')
pdf.set_y(y_start + 48)

# Row 3
y_start = pdf.get_y()
pdf.stat_card(18, y_start, 'Active Cases', '1,019', 'isolated')
pdf.stat_card(77, y_start, 'Age Range', '1-90 y', 'full range')
pdf.stat_card(136, y_start, 'Contacts', '5.0', 'per patient')
pdf.set_y(y_start + 48)

pdf.ln(3)
pdf.insight('Contact with confirmed cases accounts for 34.8% of infections, highlighting the critical importance of contact tracing and early isolation.')

# ============================================================================
# PAGE 2: DEMOGRAPHIC ANALYSIS
# ============================================================================
pdf.add_page()
pdf.section_title('Demographic Analysis', '02')
pdf.subsection('Who is getting infected?')

# Add chart
if os.path.exists('output/demographic_analysis.png'):
    pdf.image('output/demographic_analysis.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.set_text_color(100, 100, 120)
    pdf.cell(0, 5, 'Figure 1: Gender distribution, age distribution, age groups, and top affected countries', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Key Findings')
pdf.bullet('Average Patient Age: 44.8 years')
pdf.bullet('Age Range: 1 to 90 years')
pdf.bullet('Most vulnerable: 46-60 years (31.3% of cases)')
pdf.bullet('Elderly (60+): 21.0% of cases')
pdf.bullet('Gender data requires improved collection')

pdf.ln(3)
pdf.insight('The 46-60 age group represents the largest proportion of cases, suggesting workplace and community transmission patterns.')

# ============================================================================
# PAGE 3: INFECTION PATTERNS
# ============================================================================
pdf.add_page()
pdf.section_title('Infection Patterns', '03')
pdf.subsection('How are infections spreading?')

if os.path.exists('output/infection_patterns.png'):
    pdf.image('output/infection_patterns.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.cell(0, 5, 'Figure 2: Infection sources distribution and contact exposure analysis', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Transmission Analysis')
pdf.bullet('Primary Source: Contact with confirmed case (34.8%)')
pdf.bullet('Travel history: 25.0% of cases')
pdf.bullet('Community spread: 22.0% of cases')
pdf.bullet('Healthcare workers: 7.0% of cases')
pdf.bullet('Average contacts per patient: 5.0 individuals')

pdf.ln(3)
pdf.insight('Contact tracing is critical - 1 in 3 cases could be prevented with effective contact isolation.')

# ============================================================================
# PAGE 4: RECOVERY TRENDS
# ============================================================================
pdf.add_page()
pdf.section_title('Recovery Trends', '04')
pdf.subsection('What are the recovery patterns?')

if os.path.exists('output/recovery_trends.png'):
    pdf.image('output/recovery_trends.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.cell(0, 5, 'Figure 3: Recovery time distribution and age-based recovery analysis', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Recovery Metrics')
pdf.bullet('Overall Recovery Rate: 68.4% (3,422 patients)')
pdf.bullet('Average Recovery Time: 12.8 days')
pdf.bullet('Median Recovery Time: 12 days')
pdf.bullet('Recovery Range: 5 to 30 days')
pdf.bullet('Young patients (0-18): 10.2 days average')
pdf.bullet('Elderly patients (60+): 15.2 days average')

pdf.ln(3)
pdf.insight('Elderly patients require 50% longer recovery time, indicating need for age-specific care protocols.')

# ============================================================================
# PAGE 5: REGIONAL IMPACT
# ============================================================================
pdf.add_page()
pdf.section_title('Regional Impact', '05')
pdf.subsection('Which regions are most affected?')

if os.path.exists('output/regional_impact.png'):
    pdf.image('output/regional_impact.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.cell(0, 5, 'Figure 4: Top affected regions and patient outcome distribution', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Geographic Distribution')
pdf.bullet('Most Affected: Maharashtra (348 cases, 7.0%)')
pdf.bullet('Second: New York (347 cases, 6.9%)')
pdf.bullet('Third: Sao Paulo (346 cases, 6.9%)')
pdf.bullet('Top 10 regions account for 68% of all cases')

pdf.subsection('Outcome Summary')
pdf.bullet('Recovered: 3,422 patients (68.4%)')
pdf.bullet('Active/Isolated: 1,019 patients (20.4%)')
pdf.bullet('Deceased: 559 patients (11.2%)')

pdf.ln(3)
pdf.insight('Targeted resource allocation to top 3 regions could impact nearly 21% of all cases.')

# ============================================================================
# PAGE 6: FACTORS INFLUENCING RECOVERY
# ============================================================================
pdf.add_page()
pdf.section_title('Factors Influencing Recovery', '06')
pdf.subsection('What affects recovery time?')

if os.path.exists('output/recovery_factors.png'):
    pdf.image('output/recovery_factors.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.cell(0, 5, 'Figure 5: Age vs Recovery Time correlation analysis', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Correlation Analysis')
pdf.bullet('Age Correlation: +0.42 (Moderate positive relationship)')
pdf.bullet('Contact Number Correlation: +0.18 (Weak positive)')
pdf.bullet('Age Impact: Each year adds 0.12 days to recovery')
pdf.bullet('Age is the strongest predictor of recovery duration')

# ============================================================================
# PAGE 7: PREDICTIVE MODEL
# ============================================================================
pdf.add_page()
pdf.section_title('Predictive Modeling', '07')
pdf.subsection('Linear Regression Analysis')

if os.path.exists('output/regression_model.png'):
    pdf.image('output/regression_model.png', x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 7)
    pdf.cell(0, 5, 'Figure 6: Actual vs Predicted Recovery Time with Residual Analysis', 0, 1, 'C')
    pdf.ln(5)

pdf.subsection('Model Performance')
pdf.bullet('R2 Score: 0.176 (Explains 17.6% of variance)')
pdf.bullet('RMSE: 4.8 days (Average prediction error)')
pdf.bullet('Age Coefficient: +0.12 days per year')
pdf.bullet('Contact Coefficient: +0.08 days per contact')

pdf.ln(3)
pdf.insight('Age explains 18% of recovery variation - other factors like comorbidities contribute significantly.')

# ============================================================================
# PAGE 8: STRATEGIC RECOMMENDATIONS
# ============================================================================
pdf.add_page()
pdf.section_title('Strategic Recommendations', '08')

recommendations = [
    ('1. SCREENING PRIORITIZATION', 'Focus screening efforts on the 45+ age group, which accounts for over 52% of cases and shows extended recovery times.'),
    ('2. CONTACT TRACING ENHANCEMENT', 'With 34.8% of cases linked to contact with confirmed patients, expand contact tracing capacity.'),
    ('3. REGIONAL RESOURCE ALLOCATION', 'Concentrate healthcare resources in Maharashtra, New York, and Sao Paulo which account for nearly 21% of all cases.'),
    ('4. AGE-SPECIFIC PROTOCOLS', 'Develop treatment protocols based on age groups. Elderly patients require extended monitoring (15+ days).'),
    ('5. EARLY WARNING SYSTEM', 'Strengthen surveillance in regions showing rapid case growth. Implement real-time monitoring.'),
    ('6. DATA QUALITY IMPROVEMENT', 'Enhance demographic data collection, particularly gender information, for more precise future analyses.')
]

for title, desc in recommendations:
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(255, 140, 30)
    pdf.cell(0, 7, title, 0, 1)
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(60, 60, 70)
    pdf.multi_cell(0, 4.5, desc)
    pdf.ln(2)

# ============================================================================
# PAGE 9: CONCLUSION
# ============================================================================
pdf.add_page()
pdf.section_title('Conclusion', '09')

conclusion_text = """This comprehensive analysis successfully provides actionable insights for public health decision-making during the early phase of infectious disease outbreaks. The findings demonstrate clear patterns in demographics, transmission, and recovery that can guide intervention strategies.

Key Achievements:
- Complete analysis of 5,000 patient cases from the initial outbreak phase
- Six professional visualizations generated for data-driven insights
- Identification of age as the primary factor influencing recovery time
- Quantification of contact tracing effectiveness potential
- Development of predictive model for recovery time estimation

The insights from this report can help public health authorities implement targeted interventions, optimize resource allocation, and ultimately improve patient outcomes during future outbreaks."""

pdf.body_text(conclusion_text)

pdf.ln(5)
pdf.subsection('Summary at a Glance')

# Summary Table
pdf.set_fill_color(245, 245, 250)
pdf.set_draw_color(200, 200, 220)

col_widths = [80, 60]
pdf.set_font('Arial', 'B', 9)
pdf.cell(col_widths[0], 7, 'Metric', 1, 0, 'C', 1)
pdf.cell(col_widths[1], 7, 'Value', 1, 1, 'C', 1)

summary_data = [
    ['Total Cases Analyzed', '5,000'],
    ['Recovery Rate', '68.4%'],
    ['Average Recovery Time', '12.8 days'],
    ['Primary Infection Source', 'Contact (34.8%)'],
    ['Most Affected Region', 'Maharashtra (348)'],
    ['Average Patient Age', '44.8 years']
]

pdf.set_font('Arial', '', 9)
for row in summary_data:
    pdf.cell(col_widths[0], 6, row[0], 1, 0, 'L')
    pdf.cell(col_widths[1], 6, row[1], 1, 1, 'L')

pdf.ln(8)
pdf.set_font('Arial', 'I', 8)
pdf.set_text_color(100, 100, 120)
pdf.cell(0, 5, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.cell(0, 5, 'Data-Driven Public Health Insights', 0, 1, 'C')

# Save PDF
pdf.output('HealthGuard_Final_Report.pdf')
print("\n" + "="*70)
print("FINAL PROFESSIONAL PDF REPORT CREATED SUCCESSFULLY!")
print("="*70)
print("\nFile: HealthGuard_Final_Report.pdf")
print("\nReport Structure (9 Pages):")
print("  Page 1: Executive Summary + KPI Cards")
print("  Page 2: Demographic Analysis + Chart + Findings")
print("  Page 3: Infection Patterns + Chart + Findings")
print("  Page 4: Recovery Trends + Chart + Findings")
print("  Page 5: Regional Impact + Chart + Findings")
print("  Page 6: Factors Influencing Recovery + Chart")
print("  Page 7: Predictive Model + Chart + Performance")
print("  Page 8: Strategic Recommendations")
print("  Page 9: Conclusion + Summary Table")
print("\nTo open: start HealthGuard_Final_Report.pdf")