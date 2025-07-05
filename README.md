# 🧠 Subnet Analyzer

A Python-based tool to analyze and visualize IP subnets from Excel files.  
It calculates subnet details (CIDR, network, usable hosts), detects overlapping subnets, generates a structured report, and visualizes the data using bar charts.

> ✍️ Report written manually by Esraa based on analyzer output.

---

## 📂 Project Structure
├── ip_data.xlsx # Input Excel file with IPs and Subnet Masks

├── subnet_analyzer.py # Script to analyze IPs and generate subnet_report.csv + JSON

├── visualize.py # Script to generate bar chart from subnet_report.csv

├── subnet_report.csv # Output CSV after analysis

├── subnet_grouped_ip.json # Output JSON with grouped IPs

├── network_plot.png # Bar chart image

├── report.md # Answers to the analysis questions

├── Dockerfile # Containerizes the solution

├── .dockerignore 


---

## 🧪 Run the Project Locally

> ⚠️ Make sure you have Python 3.10+ and pip installed.

### 1. Install dependencies
```terminal
pip install pandas matplotlib openpyxl
```
### 2. Run the Analyzer
```
python subnet_analyzer.py
```
### 3. Run the Visualizer
```
python visualize.py
```

---
## 🐳 Run the Project with Docker
> ⚠️ Requires Docker installed on your system.

### 1. Build the Docker image
```terminal
docker build -t subnet-analysis .
```

### 2. Run the container (and bind current directory)
> ⚠️For Windows Powershell.
```terminal
docker run --rm -v ${PWD}:/app subnet-analysis
```
---
## 📊 Sample Output

![Output](https://github.com/user-attachments/assets/eee3f7c0-251c-42bb-8bed-8e6949371547)

---
## 🧾 Author

Esraa — as part of the Barq DevOps Internship Task

Date: July 2025




