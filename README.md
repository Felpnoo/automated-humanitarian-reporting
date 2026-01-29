# 📋 Automated Humanitarian Reporting Tool

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![NixOS](https://img.shields.io/badge/NixOS-Reproducible-5277C3?style=for-the-badge&logo=nixos&logoColor=white)
![Status](https://img.shields.io/badge/Status-Field%20Ready-green?style=for-the-badge)

**A robust ETL (Extract, Transform, Load) pipeline designed to automate data cleaning and reporting for humanitarian field operations.**

## 🌍 The Problem
In high-pressure humanitarian environments (like refugee shelters or transit centers), data often arrives in inconsistent formats—messy Excel files, mixed date formats, and typo-ridden names. Field officers spend valuable hours manually cleaning this data instead of focusing on strategic decision-making.

## 💡 The Solution
This tool simulates a **Data Management Assistant** workflow. It ingests raw, "dirty" CSV data, applies rigorous cleaning logic using **Pandas**, and automatically generates a professional **PDF Report** with key operational metrics.

### Key Features
- **🛡️ Data Integrity:** Automatically fixes inconsistent capitalization, extracts valid ages, and standardizes dates.
- **⚡ Automation:** Reduces a 2-hour manual reporting task to a <1 second script execution.
- **❄️ Reproducibility:** Built with **Nix Flakes**, ensuring the environment runs exactly the same on any machine, anywhere.
- **📄 Reporting:** Generates a clean, print-ready PDF using `FPDF`.

---

## 🚀 Quick Start

### Option A: Using Nix (Recommended)
If you are using NixOS or have the Nix package manager installed, you can enter a reproducible shell immediately:

# 1. Clone the repo
git clone [https://github.com/Felpnoo/automated-humanitarian-reporting.git](https://github.com/Felpnoo/automated-humanitarian-reporting.git)
cd automated-humanitarian-reporting

# 2. Enter the development environment
nix develop

# 3. Run the pipeline
python main.py
Option B: Standard Python
If you are on a standard Linux/Windows/Mac setup:

# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install pandas fpdf openpyxl

# 3. Run the pipeline
python main.py

# 📂 Project Structure

```tree
.
├── flake.nix            # NixOS Environment Configuration (Infrastructure as Code)
├── flake.lock           # Dependency Lockfile for reproducibility
├── main.py              # Core Logic (Data Generation -> Cleaning -> PDF)
├── .gitignore           # Git ignore rules
└── README.md            # Documentation
```

# 📊 Sample Output
After running the script, two files are generated:

raw_shelter_data.csv: A simulated dataset containing errors (e.g., "25 years", "active", "  MARIA ").

Daily_Shelter_Report.pdf: The final output containing:

Total Beneficiaries Count.

Average Age Statistic.

A standardized table with cleaned data (Title Case Names, Standardized Status).

# 🛠 Tech Stack
Language: Python 3.13

Data Processing: Pandas (ETL)

Reporting: FPDF

Environment: NixOS (Flakes)

Developed by Felipe Silva as a portfolio project demonstrating skills in Data Management and Process Automation for Humanitarian Contexts.
