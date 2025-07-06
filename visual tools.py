import pandas as pd
from ydata_profiling import ProfileReport

# Step 1: Load your data (use raw string for path)
file_path = r"C:\Users\aiman\OneDrive\Desktop\data science\cleaned_output.csv"
df = pd.read_csv(file_path)

# Step 2: Just light cleaning (no data loss)
# e.g., strip whitespaces from column names
df.columns = df.columns.str.strip()

# (Optional) Fill missing values for presentation, but keep original
# Example: Fill numeric NaNs with mean — only if justified
# df.fillna(df.mean(numeric_only=True), inplace=True)

# Save minimally cleaned data
cleaned_file_path = r"C:\Users\aiman\OneDrive\Desktop\data science\final_cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)

# Step 3: Generate HTML report for justification
profile = ProfileReport(df, title="Authentic Data Cleaning Justification Report", explorative=True)

# Step 4: Save the HTML report
report_path = r"C:\Users\aiman\OneDrive\Desktop\data science\data_cleaning_report.html"
profile.to_file(report_path)
#profile.to_file(report_path)

print("✅ Report generated without data loss!")
