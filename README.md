# TOPSIS Implementation in Python

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method in Python and provides:

-  A **command-line interface (CLI)**
-  A **web service using Flask**
-  A **colorful frontend (HTML + CSS)**
-  **Email-based delivery** of results
-  Packaging and distribution via **PyPI**

--------------------------------

# What is TOPSIS?

TOPSIS is a **multi-criteria decision-making (MCDM)** technique used to rank alternatives by comparing their distances from an **ideal best** and an **ideal worst** solution.

The best alternative:
- Has the **shortest distance from the ideal best**
- Has the **farthest distance from the ideal worst**

--------------------------------

# Project Structure
```
102303542_TOPSIS/
│
├── topsis/
│ ├── init.py
│ └── topsis.py
│ # Main TOPSIS implementation (CLI & logic)
│
├── app.py
│ # Flask backend for web service
│
├── email_utils.py
│ # Email sending utility (SMTP)
│
├── templates/
│ ├── index.html
│ └── success.html
│ # Success page after email delivery
│
├── uploads/
│ # Uploaded CSV files
│
├── results/
│ # Generated TOPSIS result files
│
├── plot_graphs.py
│ # Script to generate TOPSIS graphs
│
├── Topsis-Dataset.csv
│ # Sample input dataset
│
├── text_classification_result.csv
│ # Example TOPSIS output
│
├── topsis_scores.png
│ # TOPSIS score graph
│
├── topsis_ranking.png
│ # Ranking graph
│
├── screenshots/
│   ├── homepage.png
│   └── success.png
│
├── README.md
├── setup.py
├── pyproject.toml
└── LICENSE
```
-----------------------------------

# Requirements

- Python 3.x
- numpy
- pandas
- flask
- matplotlib(for graphs)

Install dependencies using:
pip install numpy pandas matplotlib flask

-------------------------------------

# Usage(Command Line)
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>

# Web Service for TOPSIS
A Flask-based web service was developed to provide a user-friendly interface for the TOPSIS algorithm.
Features:
Upload input CSV file
Enter weights and impacts (comma-separated)
Enter email ID
Receive TOPSIS result via email
Input validation for:
   Weights and impacts count
   Valid impact symbols (+ or -)
   Email format

##  Web Interface Screenshots

### Homepage – Input Form
![TOPSIS Web Interface](screenshots/homepage.png)

### Success Page
![TOPSIS Success Page](screenshots/success.png)

## Graphical Analysis
Generate graphs using: 
python plot_graphs.py

Parameters:
InputDataFile → CSV file with alternatives and criteria
Weights → Comma-separated weights
Impacts → + for benefit, - for cost
ResultFileName → Output CSV file (auto-generated)

Input File Format:
First column: Alternative names
Remaining columns: Numeric criteria

