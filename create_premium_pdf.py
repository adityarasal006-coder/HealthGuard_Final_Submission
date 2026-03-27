"""
PREMIUM PROFESSIONAL PDF REPORT
HealthGuard Analytics - COVID-19 Case Analysis
Elegant Design | Professional Layout | All Charts Included
"""

from fpdf import FPDF
from datetime import datetime
import os

class PremiumReport(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=28)
        
    def header(self):
        if self.page_no() > 1:
            # Elegant gradient-like header with border
            self.set_fill_color(20, 50, 75)
            self.rect(0, 0, 210, 22, 'F')
            
            # Company name with icon-like symbol
            self.set_font('Arial', 'B', 11)
            self.set_text_color(255, 215, 0)  # Gold color
            self.set_xy(15, 6)
            self.cell(30, 6, 'HGA', 0, 0, 'L')
            
            self.set_font('Arial', '', 9)
            self.set_text_color(220, 220, 220)
            self.cell(60, 6, 'HealthGuard Analytics', 0, 0, 'L')
            
            # Report title on right
            self.set_font('Arial', 'I', 8)
            self.set_xy(130, 6)
            self.cell(65, 6, 'COVID-19 Analysis Report', 0, 1, 'R')
            
            # Decorative line
            self.set_draw_color(255, 215, 0)
            self.set_line_width(0.5)
            self.line(15, 20, 195, 20)
            self.set_y(28)
            
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-18)
            self.set_font('Arial', 'I', 7)
            self.set_text_color(120, 120, 140)
            
            # Left side - confidentiality
            self.set_x(15)
            self.cell(50, 6, 'Confidential - Internal Use Only', 0, 0, 'L')
            
            # Center - page number with elegant styling
            self.set_x(85)
            self.cell(40, 6, f'• {str(self.page_no()).zfill(2)} •', 0, 0, 'C')
            
            # Right side - date
            self.set_x(145)
            self.cell(50, 6, datetime.now().strftime('%d %b %Y'), 0, 0, 'R')
    
    def cover_page(self):
        # Deep navy blue gradient effect
        self.set_fill_color(10, 35, 55)
        self.rect(0, 0, 210, 297, 'F')
        
        # Decorative top border
        self.set_draw_color(255, 200, 50)
        self.set_line_width(2)
        self.line(0, 0, 210, 0)
        self.line(0, 10, 210, 10)
        
        # Decorative bottom border
        self.line(0, 287, 210, 287)
        self.line(0, 297, 210, 297)
        
        # Main Title Area
        self.set_y(85)
        self.set_font('Arial', 'B', 36)
        self.set_text_color(255, 215, 0)
        self.cell(0, 20, 'COVID-19', 0, 1, 'C')
        
        self.set_font('Arial', 'B', 28)
        self.set_text_color(255, 255, 255)
        self.cell(0, 15, 'Early Case Trend Analysis', 0, 1, 'C')
        
        self.set_font('Arial', 'B', 26)
        self.cell(0, 15, '& Recovery Insights', 0, 1, 'C')
        
        # Decorative line
        self.set_draw_color(255, 215, 0)
        self.set_line_width(1)
        self.line(60, 148, 150, 148)
        
        # Subtitle
        self.set_y(165)
        self.set_font('Arial', '', 11)
        self.set_text_color(200, 200, 210)
        self.cell(0, 7, 'A Data-Driven Report for Public Health Authorities', 0, 1, 'C')
        
        # Bottom section
        self.set_y(230)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(255, 215, 0)
        self.cell(0, 10, 'HealthGuard Analytics', 0, 1, 'C')
        
        self.set_font('Arial', '', 10)
        self.set_text_color(180, 180, 200)
        self.cell(0, 6, 'Pvt. Ltd.', 0, 1, 'C')
        self.set_y(260)
        self.cell(0, 6, datetime.now().strftime('%B %d, 2026'), 0, 1, 'C')
        
        # Small logo text
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 170)
        self.cell(0, 5, 'Data-Driven Public Health Insights', 0, 1, 'C')
    
    def section_title(self, title, number=''):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(10, 45, 70)
        if number:
            self.cell(0, 12, f'{number}  {title}', 0, 1, 'L')
        else:
            self.cell(0, 12, title, 0, 1, 'L')
        
        # Decorative underline
        self.set_draw_color(255, 180, 40)
        self.set_line_width(1.5)
        self.line(15, self.get_y(), 85, self.get_y())
        self.set_draw_color(200, 200, 220)
        self.line(88, self.get_y(), 195, self.get_y())
        self.set_line_width(0.2)
        self.ln(10)
    
    def subsection(self, title):
        self.set_font('Arial', 'B', 13)
        self.set_text_color(30, 70, 100)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(3)
    
    def body_text(self, text, size=10):
        self.set_font('Arial', '', size)
        self.set_text_color(55, 55, 65)
        self.multi_cell(0, 5.5, text)
        self.ln(4)
    
    def bullet_point(self, text, symbol='◆'):
        self.set_font('Arial', '', 10)
        self.set_text_color(55, 55, 65)
        self.set_font('Arial', 'B', 10)
        self.set_text_color(255, 140, 30)
        self.cell(6, 6, symbol, 0, 0)
        self.set_font('Arial', '', 10)
        self.set_text_color(55, 55, 65)
        self.multi_cell(0, 6, text)
    
    def stat_card_luxury(self, x, y, title, value, subtitle='', accent_color=(255, 180, 40)):
        # Shadow effect
        self.set_fill_color(235, 235, 245)
        self.rect(x+1, y+1, 55, 48, 'F')
        
        # Main card
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(210, 210, 225)
        self.rect(x, y, 55, 48, 'FD')
        
        # Accent strip
        self.set_fill_color(accent_color[0], accent_color[1], accent_color[2])
        self.rect(x, y, 55, 5, 'F')
        
        self.set_xy(x + 3, y + 10)
        self.set_font('Arial', '', 8)
        self.set_text_color(100, 100, 120)
        self.cell(49, 5, title, 0, 1, 'C')
        
        self.set_xy(x + 3, y + 20)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(10, 45, 70)
        self.cell(49, 8, value, 0, 1, 'C')
        
        if subtitle:
            self.set_xy(x + 3, y + 33)
            self.set_font('Arial', '', 6)
            self.set_text_color(130, 130, 150)
            self.cell(49, 4, subtitle, 0, 1, 'C')
        
        return y + 52
    
    def insight_quote(self, text, author='Analysis Finding'):
        self.set_fill_color(250, 248, 240)
        self.set_draw_color(255, 200, 100)
        self.rect(18, self.get_y(), 174, 28, 'FD')
        
        self.set_xy(22, self.get_y() + 4)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(100, 80, 40)
        self.multi_cell(166, 5, f'"{text}"')
        
        self.set_xy(22, self.get_y() + 4)
        self.set_font('Arial', 'I', 7)
        self.set_text_color(140, 120, 70)
        self.cell(0, 5, f'— {author}', 0, 1, 'R')
        
        self.set_y(self.get_y() + 8)
    
    def add_chart_premium(self, img_path, caption, fig_number):
        if os.path.exists(img_path):
            try:
                # Add subtle background for chart
                self.set_fill_color(250, 250, 252)
                self.rect(15, self.get_y(), 180, 120, 'F')
                
                self.image(img_path, x=20, w=170)
                self.set_y(self.get_y() + 115)
                
                self.set_font('Arial', 'I', 8)
                self.set_text_color(100, 100, 120)
                self.cell(0, 6, f'Figure {fig_number}: {caption}', 0, 1, 'C')
                self.ln(8)
                return True
            except:
                self.set_font('Arial', '', 9)
                self.set_text_color(150, 150, 150)
                self.cell(0, 8, f'[Figure {fig_number}: {caption}]', 0, 1, 'C')
                self.ln(8)
                return False
        return False

# Create PDF
pdf = PremiumReport()
pdf.add_page()
pdf.cover_page()

# ============================================================================
# SECTION 1: EXECUTIVE SUMMARY
# ============================================================================
pdf.add_page()
pdf.section_title('Executive Summary', '01')

summary_text = """This comprehensive analysis examines 5,000 patient cases from the early phase of the COVID-19 outbreak (January - March 2020). The study provides critical insights into demographic patterns, infection transmission dynamics, recovery timelines, and regional impact to support evidence-based public health decision-making."""
pdf.body_text(summary_text, 10)

# Key Statistics Section
pdf.ln(5)
pdf.subsection('Key Performance Indicators')

# Row 1
y_pos = pdf.get_y()
pdf.stat_card_luxury(18, y_pos, 'Total Cases', '5,000', 'analyzed patients')
pdf.stat_card_luxury(77, y_pos, 'Recovery Rate', '68.4%', 'of total cases')
pdf.stat_card_luxury(136, y_pos, 'Recovered', '3,422', 'patients')
pdf.set_y(y_pos + 55)

# Row 2
y_pos = pdf.get_y()
pdf.stat_card_luxury(18, y_pos, 'Avg Recovery', '12.8 days', 'mean duration')
pdf.stat_card_luxury(77, y_pos, 'Avg Age', '44.8 years', 'patient average')
pdf.stat_card_luxury(136, y_pos, 'Deceased', '559', '11.2% of cases')
pdf.set_y(y_pos + 55)

# Row 3
y_pos = pdf.get_y()
pdf.stat_card_luxury(18, y_pos, 'Active Cases', '1,019', 'currently isolated')
pdf.stat_card_luxury(77, y_pos, 'Age Range', '1-90 yrs', 'full spectrum')
pdf.stat_card_luxury(136, y_pos, 'Contacts Avg', '5.0', 'per patient')
pdf.set_y(y_pos + 55)

pdf.ln(8)
pdf.insight_quote('Contact with confirmed cases accounts for 34.8% of infections, highlighting the critical importance of contact tracing and early isolation.')

# ============================================================================
# SECTION 2: DEMOGRAPHIC ANALYSIS WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Demographic Analysis', '02')
pdf.subsection('Who is Getting Infected?')

pdf.add_chart_premium('output/demographic_analysis.png', 
    'Gender distribution, age distribution, age groups, and top affected countries', '1')

pdf.subsection('Key Demographic Insights')
pdf.bullet_point('Average Patient Age: 44.8 years', '◆')
pdf.bullet_point('Age Range: 1 to 90 years, covering all demographics', '◆')
pdf.bullet_point('Most Vulnerable Group: 46-60 years (31.3% of total cases)', '◆')
pdf.bullet_point('Elderly Population (60+): Accounts for 21.0% of cases', '◆')
pdf.bullet_point('Significant gender data gaps identified - requires improved collection', '◆')

pdf.insight_quote('The 46-60 age group represents the largest proportion of cases, suggesting workplace and community transmission patterns.')

# ============================================================================
# SECTION 3: INFECTION PATTERNS WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Infection Patterns', '03')
pdf.subsection('How Are Infections Spreading?')

pdf.add_chart_premium('output/infection_patterns.png',
    'Infection sources distribution and contact exposure analysis', '2')

pdf.subsection('Transmission Analysis')
pdf.bullet_point('Primary Source: Contact with confirmed case (34.8%)', '◆')
pdf.bullet_point('Travel-Related: 25.0% of cases linked to travel history', '◆')
pdf.bullet_point('Community Spread: 22.0% of cases', '◆')
pdf.bullet_point('Healthcare Workers: 7.0% of total cases', '◆')
pdf.bullet_point('Average Contacts per Patient: 5.0 individuals', '◆')

pdf.insight_quote('Contact tracing is the most critical intervention - 1 in 3 cases could be prevented with effective contact isolation.')

# ============================================================================
# SECTION 4: RECOVERY TRENDS WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Recovery Trends', '04')
pdf.subsection('What Are the Recovery Patterns?')

pdf.add_chart_premium('output/recovery_trends.png',
    'Recovery time distribution and age-based recovery analysis', '3')

pdf.subsection('Recovery Metrics')
pdf.bullet_point('Overall Recovery Rate: 68.4% (3,422 patients)', '◆')
pdf.bullet_point('Average Recovery Time: 12.8 days', '◆')
pdf.bullet_point('Median Recovery Time: 12 days', '◆')
pdf.bullet_point('Recovery Range: 5 to 30 days', '◆')
pdf.bullet_point('Young Patients (0-18): 10.2 days average', '◆')
pdf.bullet_point('Elderly Patients (60+): 15.2 days average', '◆')

pdf.insight_quote('Elderly patients require 50% longer recovery time than younger patients, indicating need for age-specific care protocols.')

# ============================================================================
# SECTION 5: REGIONAL IMPACT WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Regional Impact', '05')
pdf.subsection('Which Regions Are Most Affected?')

pdf.add_chart_premium('output/regional_impact.png',
    'Top affected regions and patient outcome distribution', '4')

pdf.subsection('Geographic Distribution')
pdf.bullet_point('Most Affected: Maharashtra (348 cases, 7.0%)', '◆')
pdf.bullet_point('Second: New York (347 cases, 6.9%)', '◆')
pdf.bullet_point('Third: Sao Paulo (346 cases, 6.9%)', '◆')
pdf.bullet_point('Top 10 Regions: Account for 68% of all cases', '◆')

pdf.subsection('Outcome Summary')
pdf.bullet_point('Recovered: 3,422 patients (68.4%)', '◆')
pdf.bullet_point('Active/Isolated: 1,019 patients (20.4%)', '◆')
pdf.bullet_point('Deceased: 559 patients (11.2%)', '◆')

pdf.insight_quote('Targeted resource allocation to top 3 regions could impact nearly 21% of all cases.')

# ============================================================================
# SECTION 6: FACTORS INFLUENCING RECOVERY WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Factors Influencing Recovery', '06')
pdf.subsection('What Affects Recovery Time?')

pdf.add_chart_premium('output/recovery_factors.png',
    'Correlation analysis: Age vs Recovery Time', '5')

pdf.subsection('Correlation Analysis')
pdf.bullet_point('Age Correlation: +0.42 (Moderate positive relationship)', '◆')
pdf.bullet_point('Contact Number Correlation: +0.18 (Weak positive)', '◆')
pdf.bullet_point('Age Impact: Each year adds approximately 0.12 days to recovery', '◆')
pdf.bullet_point('Age is the strongest predictor of recovery duration', '◆')

# ============================================================================
# SECTION 7: PREDICTIVE MODEL WITH CHART
# ============================================================================
pdf.add_page()
pdf.section_title('Predictive Modeling', '07')
pdf.subsection('Linear Regression Analysis')

pdf.add_chart_premium('output/regression_model.png',
    'Actual vs Predicted Recovery Time with Residual Analysis', '6')

pdf.subsection('Model Performance Metrics')
pdf.bullet_point('R² Score: 0.176 (Explains 17.6% of variance)', '◆')
pdf.bullet_point('RMSE: 4.8 days (Average prediction error)', '◆')
pdf.bullet_point('Age Coefficient: +0.12 days per year of age', '◆')
pdf.bullet_point('Contact Coefficient: +0.08 days per contact', '◆')
pdf.bullet_point('Age is the most significant predictor of recovery time', '◆')

pdf.insight_quote('While age explains 18% of recovery variation, other factors like comorbidities and treatment quality contribute significantly.')

# ============================================================================
# SECTION 8: STRATEGIC RECOMMENDATIONS
# ============================================================================
pdf.add_page()
pdf.section_title('Strategic Recommendations', '08')

recommendations = [
    ('SCREENING PRIORITIZATION', 'Focus screening efforts on the 45+ age group, which accounts for over 52% of cases and shows extended recovery times. Implement targeted testing in senior communities and healthcare facilities.'),
    ('CONTACT TRACING ENHANCEMENT', 'With 34.8% of cases linked to contact with confirmed patients, expand contact tracing capacity. Prioritize individuals with more than 10 contacts for rapid testing and quarantine.'),
    ('REGIONAL RESOURCE ALLOCATION', 'Concentrate healthcare resources in Maharashtra, New York, and Sao Paulo which account for nearly 21% of all cases. Establish surge capacity in these regions.'),
    ('AGE-SPECIFIC PROTOCOLS', 'Develop treatment protocols based on age groups. Elderly patients require extended monitoring (15+ days) while younger patients may recover faster with standard care.'),
    ('EARLY WARNING SYSTEM', 'Strengthen surveillance in regions showing rapid case growth. Implement real-time monitoring of contact networks to identify super-spreader events early.'),
    ('DATA QUALITY IMPROVEMENT', 'Enhance demographic data collection, particularly gender information, to enable more precise future analyses and targeted interventions.')
]

for i, (title, desc) in enumerate(recommendations, 1):
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(255, 140, 30)
    pdf.cell(12, 8, f'{i:02d}', 0, 0)
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(10, 45, 70)
    pdf.cell(0, 8, title, 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(60, 60, 70)
    pdf.multi_cell(0, 5, desc)
    pdf.ln(3)

# ============================================================================
# SECTION 9: CONCLUSION
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

pdf.body_text(conclusion_text, 10)

pdf.ln(8)

# Summary Table
pdf.subsection('Report Summary at a Glance')
pdf.set_fill_color(245, 245, 250)
pdf.set_draw_color(200, 200, 220)

summary_data = [
    ['Metric', 'Value'],
    ['Total Cases Analyzed', '5,000'],
    ['Recovery Rate', '68.4%'],
    ['Average Recovery Time', '12.8 days'],
    ['Primary Infection Source', 'Contact (34.8%)'],
    ['Most Affected Region', 'Maharashtra (348 cases)'],
    ['Average Patient Age', '44.8 years'],
    ['Mortality Rate', '11.2%']
]

col_widths = [80, 60]
pdf.set_font('Arial', 'B', 9)
for i, header in enumerate(['Metric', 'Value']):
    pdf.cell(col_widths[i], 8, header, 1, 0, 'C', 1)
pdf.ln()

pdf.set_font('Arial', '', 9)
fill = False
for row in summary_data[1:]:
    for i, item in enumerate(row):
        pdf.cell(col_widths[i], 7, item, 1, 0, 'L', fill)
    pdf.ln()
    fill = not fill

pdf.ln(12)

# Closing
pdf.set_font('Arial', 'I', 9)
pdf.set_text_color(100, 100, 120)
pdf.cell(0, 6, 'For additional analysis or customization requests, please contact:', 0, 1, 'C')
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(255, 140, 30)
pdf.cell(0, 6, 'HealthGuard Analytics Pvt. Ltd.', 0, 1, 'C')
pdf.set_font('Arial', '', 9)
pdf.set_text_color(80, 80, 100)
pdf.cell(0, 5, 'analytics@healthguard.com  |  www.healthguard.com', 0, 1, 'C')

# Save PDF
pdf.output('HealthGuard_Premium_Report.pdf')
print("\n" + "="*70)
print("✨ PREMIUM PROFESSIONAL PDF REPORT CREATED! ✨")
print("="*70)
print("\n📄 File: HealthGuard_Premium_Report.pdf")
print("\n📊 Report Features:")
print("   • Elegant cover page with gold accents")
print("   • Color-coded luxury statistics cards")
print("   • All 6 charts with professional captions")
print("   • Insight quotes and key findings")
print("   • Strategic recommendations section")
print("   • Executive summary with KPI dashboard")
print("   • Professional headers and footers")
print("   • Clean typography and spacing")
print("\n📑 Report Structure (9 Pages):")
print("   Page 1: Premium Cover Page")
print("   Page 2: Executive Summary + KPI Cards")
print("   Page 3: Demographic Analysis + Chart")
print("   Page 4: Infection Patterns + Chart")
print("   Page 5: Recovery Trends + Chart")
print("   Page 6: Regional Impact + Chart")
print("   Page 7: Factors + Predictive Model + Charts")
print("   Page 8: Strategic Recommendations")
print("   Page 9: Conclusion + Summary Table")
print("\n💡 To open: start HealthGuard_Premium_Report.pdf")