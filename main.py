import pandas as pd
from fpdf import FPDF
import random
from datetime import datetime

# --- CONFIGURATION ---
RAW_DATA_FILE = "raw_shelter_data.csv"
REPORT_FILE = "Daily_Shelter_Report.pdf"

# --- 1. GENERATE DUMMY DATA (Simulating a messy Excel file from field) ---
def generate_messy_data():
    print("Generating dummy raw data...")
    data = {
        'Refugee_ID': [f'REF-{i:03d}' for i in range(1, 21)],
        'Full_Name': ['  juan perez ', 'MARIA gomez', 'Carlos   SILVA', 'Ana  rodriguez', 'LUIS diaz'] * 4,
        'Age': ['25', '34 years', '19', 'unknown', '42'] * 4,  # Messy format
        'Status': ['Active', 'active', 'Departed', 'Active', 'Arrived'] * 4, # Inconsistent casing
        'Entry_Date': ['2025-01-10', '12/01/2025', '2025-01-11', '2025/01/09', 'today'] * 4
    }
    df = pd.DataFrame(data)
    df.to_csv(RAW_DATA_FILE, index=False)
    print(f"Raw data saved to {RAW_DATA_FILE}")

# --- 2. DATA CLEANING PIPELINE (ETL) ---
def clean_data():
    print("Cleaning data...")
    df = pd.read_csv(RAW_DATA_FILE)

    # Standardize Names (Title Case + Strip whitespace)
    df['Full_Name'] = df['Full_Name'].str.strip().str.title()

    # Clean Age (Extract numbers only, set errors to 0)
    df['Age'] = pd.to_numeric(df['Age'].str.extract(r'(\d+)', expand=False), errors='coerce').fillna(0).astype(int)

    # Standardize Status (Uppercase)
    df['Status'] = df['Status'].str.upper()

    # Filter only Active/Arrived for the report
    valid_status = ['ACTIVE', 'ARRIVED']
    df_filtered = df[df['Status'].isin(valid_status)]
    
    return df_filtered

# --- 3. GENERATE PDF REPORT ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'UNHCR Simulation - Daily Shelter Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(df):
    print("Generating PDF report...")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Summary Metrics
    total_people = len(df)
    avg_age = df['Age'].mean()
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(0, 10, f"Total Beneficiaries: {total_people}", ln=True)
    pdf.cell(0, 10, f"Average Age: {avg_age:.1f} years", ln=True)
    pdf.ln(10)

    # Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(40, 10, "ID", 1, 0, 'C', 1)
    pdf.cell(80, 10, "Full Name", 1, 0, 'C', 1)
    pdf.cell(30, 10, "Age", 1, 0, 'C', 1)
    pdf.cell(40, 10, "Status", 1, 1, 'C', 1)

    # Table Rows
    pdf.set_font("Arial", size=9)
    for _, row in df.iterrows():
        pdf.cell(40, 10, row['Refugee_ID'], 1)
        pdf.cell(80, 10, row['Full_Name'], 1)
        pdf.cell(30, 10, str(row['Age']), 1, 0, 'C')
        pdf.cell(40, 10, row['Status'], 1, 1, 'C')

    pdf.output(REPORT_FILE)
    print(f"Report generated successfully: {REPORT_FILE}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    generate_messy_data()  # Step 1
    clean_df = clean_data() # Step 2
    generate_pdf(clean_df) # Step 3
