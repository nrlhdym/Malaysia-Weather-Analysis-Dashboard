
# 🌦️ Malaysia Weather Analysis Dashboard

This Power BI dashboard visualizes hourly Malaysian weather data with a strong focus on **data quality control (QC)**, trend analysis, and insightful reporting.

## 📊 Key Features

- ✅ **QC Flagging:** Automatically flags bad data using MLM-style threshold masking
- 🌡️ **Temperature, Humidity, and Pressure Trends** (Yearly)
- 🌬️ **Wind Rose Chart** using Radar/Polar visualization
- 📉 **Data Quality Overview:** Good vs Bad data per year
- 🔍 **Missing Value Breakdown:** Count and percentage per variable
- 🧠 **Smart Insight Card:** Identifies the variable with the most missing data

## 📁 Files Included

| File Name                    | Description |
|-----------------------------|-------------|
| `Malaysia_Weather_Analysis.pbix` | Power BI dashboard file |
| `weather_clean.csv`       | Dataset after QC flagging and NaN masking |
| `clean.py`       | Python script to apply MLM-style data quality control |
| `README.md`                       | Project summary and documentation |
| `dashboard_screenshot.png`       | Dashboard preview |


## 🔍 Data Quality Control

The dataset was preprocessed using `clean.py`. This script applies MLM-style quality control by masking out-of-range values and flagging each row as `"Good"` or `"Bad"`.

### QC thresholds applied:

| Variable      | Range        |
|---------------|--------------|
| Temperature   | 0°C – 45°C   |
| Humidity      | 0.1 – 1.0    |
| Pressure      | > 900 mb     |
| Wind Speed    | 0 – 60 km/h  |

## 📈 Example Insights

- ✅ **Over 99% of rows passed QC**
- 🌡️ **Temperature** had the highest number of missing values (over 10,000 entries)
- 🌬️ Most common wind direction was **from the East (E)**

## 📌 Data Source

[Kaggle – Weather Dataset by Muthu J](https://www.kaggle.com/datasets/muthuj7/weather-dataset)

## 👩‍💻 Created by

**Nurul Hidayah**  
GitHub: [@nrlhdym](https://github.com/nrlhdym)

---
