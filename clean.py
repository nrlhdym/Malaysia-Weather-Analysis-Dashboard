import pandas as pd
import os
import numpy as np

project_path = r"C:\Users\user\Desktop\Project\Weather"
df = pd.read_csv(os.path.join(project_path, "weather_clean.csv"))

df['DateTime'] = pd.to_datetime(df['DateTime'], utc=True, errors='coerce')

df['Temperature'] = df['Temperature'].mask((df['Temperature'] < 0) | (df['Temperature'] > 45))
df['Apparent Temperature'] = df['Apparent Temperature'].mask((df['Apparent Temperature'] < 0) | (df['Apparent Temperature'] > 50))
df['Humidity'] = df['Humidity'].mask((df['Humidity'] <= 0) | (df['Humidity'] > 1))
df['Wind Speed'] = df['Wind Speed'].mask((df['Wind Speed'] < 0) | (df['Wind Speed'] > 60))
df['Wind Bearing'] = df['Wind Bearing'].mask((df['Wind Bearing'] < 0) | (df['Wind Bearing'] > 360))
df['Pressure'] = df['Pressure'].mask((df['Pressure'] <= 900) | (df['Pressure'] > 1100))
df['Visibility'] = df['Visibility'].mask((df['Visibility'] < 0) | (df['Visibility'] > 20))

# Function to flag rows with any NaN in key columns
def flag_qc(row):
    if pd.isna(row['Temperature']) or pd.isna(row['Pressure']) or pd.isna(row['Humidity']):
        return "Bad"
    else:
        return "Good"

# Apply QC Flag
df['QC_Flag'] = df.apply(flag_qc, axis=1)

# Save the result
output_path = os.path.join(project_path, "weather_with_qc_flag.csv")
df.to_csv(output_path, index=False)

print(f" QC applied and flagged. File saved to:\n{output_path}")
