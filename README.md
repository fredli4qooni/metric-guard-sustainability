# MetricGuard: Automated Data Validation System for GreenMetric

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Data Science](https://img.shields.io/badge/Data_Science-FF6F00?style=for-the-badge&logo=databricks&logoColor=white)
![Sustainability](https://img.shields.io/badge/Sustainability-00C853?style=for-the-badge&logo=leaflet&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Data Validation](https://img.shields.io/badge/Validation-Automated-success?style=flat-square)](https://github.com/fredli4qooni/metric-guard)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com/fredli4qooni/metric-guard)

</div>

## Executive Summary

**MetricGuard** is an automated data validation engine designed to address data integrity challenges in university sustainability reporting (GreenMetric). This project simulates a "Gatekeeper" verification process to detect human errors, data manipulation (greenwashing), and unit inconsistencies in real-time.

This project was built to address the specific needs of the **Data Analyst Officer** position, which is responsible for validating thousands of data entries from universities worldwide.

---

## Key Features

The system implements validation logic based on GreenMetric methodology:

**Logic Integrity Check (SI Category):** Ensures total vegetation area (Forest + Planted) does not exceed total campus area.

**Statistical Outlier Detection (EC Category):** Uses **Z-Score** algorithm to detect electricity usage anomalies (e.g., input errors between Watt vs kWh).

**Compliance Verification:** Automatically detects missing supporting evidence links.

**Auto-Standardization:** Cleanses heterogeneous data formats (e.g., European vs US decimal formats).

---

## Tech Stack

<table>
<tr>
<td align="center" width="25%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" alt="Python"/>
<br><strong>Python 3.9+</strong>
<br><sub>Core Language</sub>
</td>
<td align="center" width="25%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="60" height="60" alt="Pandas"/>
<br><strong>Pandas</strong>
<br><sub>Data Manipulation</sub>
</td>
<td align="center" width="25%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="60" height="60" alt="NumPy"/>
<br><strong>NumPy</strong>
<br><sub>Statistical Analysis</sub>
</td>
<td align="center" width="25%">
<img src="https://img.icons8.com/color/96/microsoft-excel-2019--v1.png" width="60" height="60" alt="Excel"/>
<br><strong>OpenPyXL</strong>
<br><sub>Excel Integration</sub>
</td>
</tr>
</table>

---

## 📁 Project Structure

```bash
metric-guard/
├── raw_greenmetric_data.csv      # Simulation dataset (Generated)
├── generate_data.py              # Script to create dummy data + error scenarios
├── clean_data.py                 # Data format cleaning module (ETL)
├── metric_guard_engine.py        # Core validation logic (Main script)
├── Final_Validation_Report.xlsx  # Error report output for stakeholders
└── README.md                     # Project documentation
```

---

## How It Works (Simulation Scenarios)

This project tests data with 3 common field error scenarios:

<table>
<thead>
<tr>
<th>Error Type</th>
<th>Simulation Scenario</th>
<th>Detection Method</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Logic Error</strong></td>
<td>University claims forest area > campus area</td>
<td><code>if (Forest + Planted) > Total_Area</code></td>
</tr>
<tr>
<td><strong>Unit Error</strong></td>
<td>Electricity input in Watt (should be kWh)</td>
<td><code>Z-Score > 3</code> (Statistical Outlier)</td>
</tr>
<tr>
<td><strong>Format Error</strong></td>
<td>Using comma (<code>,</code>) as decimal separator</td>
<td><code>str.replace(',', '.')</code> cleaning</td>
</tr>
</tbody>
</table>

---

## Sample Output

When the script runs, the system generates a priority report as follows:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    VALIDATION REPORT SUMMARY                              ║
╚═══════════════════════════════════════════════════════════════════════════╝

University_ID   Error_Type            Message
─────────────────────────────────────────────────────────────────────────────
UNIV_005        Logic Error           Total Green Area exceeds Total Campus Area
UNIV_010        Unit Error (Outlier)  Electricity usage is statistically improbable (Z-Score: 8.4)
UNIV_040        Compliance Error      Evidence Link is missing
```

---

## Installation & Usage

### Clone repository

```bash
git clone https://github.com/fredli4qooni/metric-guard.git
cd metric-guard
```

### Install dependencies

```bash
pip install pandas numpy openpyxl
```

### Run the Validation Engine

```bash
python metric_guard_engine.py
```

> **Note:** This script will automatically call the cleaning module first.

---

## Use Cases

- Automated validation for sustainability reporting
- GreenMetric university rankings quality assurance
- Data integrity verification for ESG compliance
- ETL pipeline for heterogeneous data sources

---

## Contact

**Author:** Fredli Fourqoni  
**Target Role:** Data Analyst Officer (Sustainability Focus)

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-fredli4qooni-181717?style=for-the-badge&logo=github)](https://github.com/fredli4qooni)

</div>

---

<div align="center">
<sub>Built with 💚 for sustainable data integrity</sub>
</div>