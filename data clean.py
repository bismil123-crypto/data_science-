import pandas as pd
import numpy as np
import re
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = """age	gender	city	country	education_level	occupation	monthly_income_bracket	earning_bracket	hours_played_per_day	how_often_do_you_play_online_games	what_motivates_you_to_play_online_games	playerlevel	gamedifficulty
25	Male	Karachi	Pakistan	Bachelor'S Degree	Student	Unknown	Unknown	108	Daily	Stress Relief	79	Medium
21	Female	Karachi	Pakistan	Bachelor'S Degree	Cyber	Unknown	Unknown	144	Daily	Exploration	11	Medium
28	Female	Batkhela	Pakistan	Bachelor'S Degree	Panel Management Officer	Unknown	Unknown	142	Daily	Competition	35	Easy
22	Male	Karachi	Pakistan	Bachelor'S Degree	Unknown	Unknown	Unknown	85	Daily	Exploration	57	Easy
25	Male	Karachi	Pakistan	Bachelor'S Degree	Nothing	Unknown	Unknown	131	Daily	Stress Relief	95	Medium
21	Male	Faisalabad	Pakistan	High School	Graphic Designer	Unknown	Unknown	81	Daily	Stress Relief	74	Easy
24	Male	Gujranwala	England	Bachelor'S Degree	Buisnesse	Unknown	Unknown	50	Daily	Stress Relief	13	Hard
22	Female	Lahore	Pakistan	Associate Degree	Student	Unknown	Unknown	48	3-5 times a week	Exploration	27	Medium
21	Female	Lahore	Pakistan	Bachelor'S Degree	Khayaban-E-Amin, Defense Road	Unknown	Unknown	101	Daily	Competition	23	Easy
23	Female	Karachi	Pakistan	High School	Business	Unknown	Unknown	95	3-5 times a week	Competition	99	Easy
23	Male	Lahore	Pakistan	Bachelor'S Degree	Businessman	Unknown	Unknown	95	3-5 times a week	Competition	14	Hard
23	Female	Unknown	Unknown	Nan	Software Dev	Unknown	Unknown	124	Daily	Exploration	62	Easy
23	Male	Lahore	Pakistan	Bachelor'S Degree	Electrical Engineer	Unknown	Unknown	18	1-2 times a week	Competition	52	Easy
23	Female	Lahore	Pakistan	Bachelor'S Degree	Estimator	Unknown	Unknown	156	1-2 times a week	Competition	33	Easy
20	Male	Karachi	Unknown	Metric	Unknown	Unknown	Unknown	41	Daily	Competition	98	Easy
17	Male	Karachi	Unknown	Enter	Unknown	Unknown	0	156	Daily	Exploration	58	Medium
20	Male	Karachi	Unknown	Intermidi	Unknown	Unknown	Student	154	Daily	Stress Relief	62	Easy
19	Male	Karachi	Unknown	Matric	Unknown	Unknown	30000	131	Daily	Stress Relief	13	Medium
25	Female	Karachi	Unknown	Inter	Unknown	Unknown	30000	135	Daily	Stress Relief	77	Easy
18	Female	Karachi	Unknown	Intermediate	Unknown	Unknown	Unknown	56	Daily	Stress Relief	21	Easy
26	Female	Karachi	Unknown	Matric	Unknown	Unknown	20000	177	Daily	Stress Relief	34	Easy
15	Female	Karachi	Unknown	9Th	Unknown	Unknown	0	159	Daily	Unknown	36	Easy
20	Male	Karachi	Unknown	Intermediate	Unknown	Unknown	none	120	Daily	Unknown	81	Medium
19	Male	Karachi	Unknown	Undergraduate	Unknown	Unknown	7000 rupees	117	3-5 times a week	Unknown	40	Easy
20	Male	Karachi	Unknown	Software Engineering	Unknown	Unknown	Online game boosting, earn average figure	161	3-5 times a week	Unknown	1	Medium
19	Female	Karachi	Unknown	Undergraduate	Unknown	Unknown	3k - 5k	82	3-5 times a week	Unknown	1	Hard
23	Male	Karachi	Unknown	Bba	Unknown	Unknown	50000	118	Daily	Achievement	71	Medium
26	Male	Karachi	Unknown	Graduate	Unknown	Unknown	1000$ - 2000$	177	Daily	Stress Relief	59	Easy
26	Male	Karachi	Unknown	Graduated	Unknown	Unknown	-	57	Daily	Stress Relief	2	Easy
22	Female	Karachi	Unknown	Bachelors In Computer Science	Unknown	Unknown	35000-70000	155	Daily	Competition	85	Easy
20	Female	Unknown	Unknown	Nan	Unknown	Unknown	Unknown	67	Daily	Competition	35	Easy
25	Male	Karachi	Pakiatan	Bachelor'S Degree	Sse	$500 - $1000	Unknown	70	Daily	Exploration	50	Easy
20	Female	Winnipeg	Canada	High School	Unknown	Below PKR 20,000	Unknown	127	Daily	Achievement	48	Hard
19	Male	Karachi	Pakistan	Other	Unknown	Unknown	Unknown	48	Daily	Competition	62	Hard
22	Male	Karachi	Pakistan	Bachelor'S	Unknown	Below PKR 20,000	Unknown	120	Daily	Competition	24	Hard
19	Female	Karachi	Pakistan	High School	Unknown	Below PKR 20,000	Unknown	166	Daily	Achievement	24	Medium
23	Male	Karachi	Pakistan	High School	Unknown	Below PKR 20,000	Unknown	28	Daily	Competition	79	Hard
23	Male	Karachi	Pakistan	Bachelor'S	Unknown	Below PKR 20,000	Unknown	61	Daily	Stress Relief	26	Medium
19	Female	Lahore	Pakistan	High School	Unknown	Below PKR 20,000	Unknown	112	1-2 times a week	Stress Relief	14	Medium
21	Female	Sahiwal	Pakistan	High School	Unknown	Below PKR 20,000	Unknown	116	1-2 times a week	Stress Relief	52	Hard
23	Female	Mailsi	Pakistan	Master'S	Unknown	PKR 50kâ€“100k	Unknown	43	1-2 times a week	Stress Relief	93	Medium
22	Male	Karachi	Pakistan	Bachelor'S	Unknown	Below PKR 20,000	Unknown	151	Daily	Achievement	76	Medium
17	Male	Karachi	Pakistan	High School	Unknown	Below PKR 20,000	Unknown	68	1-2 times a week	Achievement	88	Medium
81	Male	Karachi	Pakistan	Bachelor'S	Unknown	PKR 20kâ€“50k	Unknown	115	1-2 times a week	Achievement	98	Medium
17	Female	Jeddah	Saudi Arabia	High School	Unknown	Below PKR 20,000	Unknown	149	Daily	Exploration	10	Easy
17	Male	Riyadh	Saudia Arabia	High School	Unknown	Below PKR 20,000	Unknown	65	3-5 times a week	Exploration	34	Medium
21	Male	Karachi	Pakistan	Bachelor'S	Job	Below PKR 20,000	Unknown	176	3-5 times a week	Exploration	45	Easy
18	Male	Karachi	Pakistan	High School	Studying	Below PKR 20,000	Unknown	31	Unknown	Stress Relief	73	Medium
21	Female	Karachi	Pakistan	Bachelor'S	Student	PKR 20kâ€“50k	Unknown	77	Unknown	Stress Relief	51	Easy
18	Male	Karachi	Pakistan	High School	Student	Above PKR 100k	Unknown	94	Unknown	Unknown	31	Hard
20	Male	Malabon	Philippines	Bachelor'S	Unknown	Below PKR 20,000	Unknown	146	3-5 times a week	Unknown	22	Hard
22	Male	Karachi	Pakistan	Bachelor'S	Student	PKR 20kâ€“50k	Unknown	45	Unknown	Unknown	19	Medium
20	Male	Karachi	Pakistan	Bachelor'S	Software Engineer	Below PKR 20,000	Unknown	134	Unknown	Exploration	64	Easy
19	Male	Karachi	Pakistan	Bachelor'S	Student	PKR 50kâ€“100k	Unknown	50	Unknown	Stress Relief	95	Easy
22	Male	Karachi	Pakistan	Bachelor'S	Engineer	PKR 20kâ€“50k	Unknown	171	Unknown	Competition	6	Easy
18	Female	Karachi	Pakistan	High School	Unknown	PKR 20kâ€“50k	Unknown	46	Unknown	Competition	8	Easy
18	Male	Karachi	Pakistan	Bachelor'S Degree	Freelancer	Below PKR 20,000	Unknown	139	3-5 times a week	Exploration	20	Easy
18	Male	Karachi	Pakistan	High School Or Equivalent	Business	Below PKR 20,000	Unknown	36	Unknown	Competition	88	Easy
18	Male	Faisalbad	Pakistan	Bachelor'S Degree	Student	Below PKR 20,000	Unknown	148	Unknown	Competition	73	Easy
18	Female	Karachi	Pakistan	Bachelor'S Degree	Non	Below PKR 20,000	Unknown	153	3-5 times a week	Unknown	46	Easy
18	Male	Karachi	Pakistan	High School Or Equivalent	Student	Below PKR 20,000	Unknown	138	Unknown	Exploration	27	Hard
18	Female	Karachi	Pakistan	Bachelor'S Degree	Student	Below PKR 20,000	Unknown	155	Unknown	Competition	35	Medium
18	Female	Karachi	Pakistan	High School Or Equivalent	Social Media Handling	Below PKR 20,000	Unknown	94	Unknown	Competition	76	Easy
18	Male	Chakdara	Pakistan	Bachelor'S Degree	Student	Below PKR 20,000	Unknown	140	Unknown	Unknown	10	Hard
18	Male	Karachi	Pakistan	Bachelor'S Degree	Student	Below PKR 20,000	Unknown	94	Unknown	Competition	38	Easy
18	Female	Karachi	Pakistan	Bachelor'S Degree	Freelancer	Below PKR 20,000	Unknown	94	Unknown	Competition	80	Easy
18	Female	Unknown	Unknown	Undergraduate	Student	Below PKR 20,000	Unknown	94	Unknown	Competition	58	Easy
21	Female	Unknown	Unknown	Undergraduate	Unknown	Below PKR 20,000	Unknown	94	Unknown	Stress Relief	26	Medium
18	Female	Unknown	Unknown	Other	Unknown	Unknown	Unknown	94	Unknown	Competition	3	Easy
12	Male	Unknown	Unknown	High School	.	Unknown	Unknown	94	Unknown	Competition	72	Medium
20	Female	Unknown	Unknown	Undergraduate	Nothing	Unknown	Unknown	94	Unknown	Stress Relief	29	Easy
19	Male	Unknown	Unknown	High School	Nil	Unknown	Unknown	94	Unknown	Social Interaction	45	Medium
25	Male	Unknown	Unknown	Undergraduate	Designer	Unknown	Unknown	94	Unknown	Achievement	46	Easy
19	Female	Unknown	Unknown	Undergraduate	Nill	Unknown	Unknown	94	Unknown	Stress Relief	12	Medium
20	Male	Unknown	Unknown	Undergraduate	Student	Unknown	Unknown	94	Unknown	"Competition
Stress Relief
Achievement"	91	Easy
16	Male	Unknown	Unknown	High School	Student	Unknown	Unknown	94	Unknown	"Competition
Achievement"	23	Easy
26	Male	Unknown	Unknown	Undergraduate	Student And Housewife	Unknown	Unknown	94	Unknown	Achievement	9	Medium
27	Male	Unknown	Unknown	Postgraduate	Businessman	Unknown	Unknown	94	Unknown	Stress Relief	15	Easy
18	Female	Unknown	Unknown	Undergraduate	Unknown	Unknown	Unknown	94	Unknown	Competition	33	Easy
23	Male	Unknown	Unknown	Undergraduate	Student	Unknown	Unknown	94	Unknown	Social Interaction	15	Easy
24	Female	Unknown	Unknown	Undergraduate	Student	Unknown	Unknown	94	Unknown	Stress Relief	24	Easy
23	Male	Unknown	Unknown	Undergraduate	Freelancer	Unknown	Unknown	94	Unknown	Exploration	14	Medium
27	Male	Unknown	Unknown	Undergraduate	Freelancing	Unknown	Unknown	94	Unknown	Social Interaction	40	Easy
21	Male	Unknown	Unknown	Undergraduate	Student	Unknown	Unknown	94	Unknown	"Social Interaction
Stress Relief"	73	Easy
25	Male	Lahore	Pakistan	Nan	Thousands	Unknown	Unknown	94	Unknown	Competition	14	Easy
25	Male	Karachi	Pakistan	Nan	Supply Chain Officer	Unknown	Unknown	94	Unknown	Competition	4	Medium
18	Female	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Competition	89	Easy
18	Male	Karachi	Pakistan	Nan	Sale Marketing	Unknown	Unknown	94	Unknown	Competition	78	Hard
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Competition	40	Medium
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Stress Relief	11	Medium
25	Male	Karachi	Pakistan	Nan	Pharmacist	Unknown	Unknown	94	Unknown	Stress Relief	59	Medium
25	Male	Karachi	Pakistan	Nan	Banker	Unknown	Unknown	94	Unknown	Social Interaction	76	Easy
18	Female	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Social Interaction	77	Easy
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Social Interaction	80	Easy
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Competition	33	Hard
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Exploration	3	Easy
18	Male	Karachi	Pakistan	Nan	Student Hybrid Job Remote Internships	Unknown	Unknown	94	Unknown	Achievement	61	Medium
18	Male	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Achievement	1	Easy
18	Female	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Achievement	54	Easy
25	Female	Karachi	Pakistan	Nan	Student Complete My Bachelors Along With The Full Time Job	Unknown	Unknown	94	Unknown	Achievement	65	Hard
25	Male	Karachi	Pakistan	Nan	Ceo	Unknown	Unknown	94	Unknown	Stress Relief	89	Medium
18	Female	Karachi	Pakistan	Nan	Student	Unknown	Unknown	94	Unknown	Social Interaction	53	Hard
22	Male	Islamabad	Pakistan	Bachelor'S	Develper	Unknown	50000	3	Unknown	Exploration	54	Easy
22	Female	Karachi	Pakistan	Bachelor'S	Student	Unknown	Unknown	1	Unknown	Social Interaction	38	Medium
20	Female	Karachi	Paki	Bachelor'S	Unknown	Unknown	0	0	Unknown	Achievement	22	Easy
21	Male	Karachi	Pakistan	Bachelor'S	Student	Unknown	00000??	0	Unknown	Achievement	73	Easy
19	Male	Karachi	Pakistan	High School	Student	Unknown	-	1	Unknown	Achievement	56	Easy
19	Male	Karachi	Pakistan	Other	Unknown	Unknown	30000	3.5	Unknown	Achievement	45	Hard
20	Male	Karachi	Pakistan	Bachelor'S	Undergraduate Student	Unknown	Unknown	1	Unknown	Competition	75	Medium
20	Male	Karachi	Pakistan	Bachelor'S	Student	Unknown	25/30	2	Unknown	Competition	2	Easy
20	Female	Karachi	Pakistan	Other	Unknown	Unknown	Unknown	94	Unknown	Competition	10	Easy
28	Male	Karachi	Pakistan	Bachelor'S	School Principle	Unknown	120000	3	Unknown	Unknown	5	Hard
20	Male	Islamabad	Pakistan	Bachelor'S	Nil	Unknown	Not sure 	5	Unknown	Unknown	88	Medium
25	Female	Rawalpindi	Pakistan	Bachelor'S	Student	Unknown	Unknown	1	Unknown	Unknown	72	Medium
22	Female	Islamabad	Pakistan	Bachelor'S	None Yet	Unknown	Unknown	1	Unknown	Unknown	42	Easy
27	Male	Karachi	Pakistan	Master'S	Doctor	Unknown	Unknown	1	Unknown	Unknown	34	Hard
22	Female	Karachi	Pakistan	Bachelor'S	_	Unknown	_	1	Unknown	Unknown	24	Medium
22	Female	Karachi	Pakistan	Bachelor'S	Karachi	Unknown	Unknown	0.1	Unknown	Unknown	12	Easy
"""

# Convert to DataFrame, specifying tab as separator
df = pd.read_csv(StringIO(data), sep='\t')

# --- 1. APPLYING YOUR CLEANING FUNCTIONS (with modifications for robustness and correctness) ---
print("--- Initial Data Cleaning Stage ---")

# Your original cleaning functions
def clean_age(age):
    try:
        age_val = float(age)
        return age_val if 5 <= age_val <= 80 else np.nan
    except (ValueError, TypeError):
        return np.nan

def clean_gender(gender):
    gender_str = str(gender).strip().lower()
    if not gender_str or gender_str in ['unknown', 'none', 'nan']: # Added 'nan'
        return np.nan
    return 'Male' if gender_str.startswith('m') else 'Female' if gender_str.startswith('f') else np.nan

def clean_city(city):
    city_str = str(city).strip().title()
    if not city_str or city_str.lower() in ['unknown', 'none', 'nil', 'nan']: # Added 'nan'
        return np.nan
    
    corrections = {
        'Karachi': 'Karachi', # ensure consistent casing
        'Lahore': 'Lahore',
        'Islamabad': 'Islamabad',
        'Faisalbad': 'Faisalabad',
        'Karachi ': 'Karachi', # strip trailing spaces covered by .strip()
        'Lahore ': 'Lahore',
        'Pakiatan': 'Pakistan' # Correcting typo for country if used here
    }
    # For country, specific correction for 'Saudia Arabia'
    if city_str == 'Saudia Arabia': return 'Saudi Arabia'
    if city_str == 'Paki': return 'Pakistan' # for country column

    return corrections.get(city_str, city_str)


def clean_education(edu):
    edu_str = str(edu).strip().title()
    if not edu_str or edu_str.lower() in ['unknown', 'none', 'nan', 'other']: # Added 'nan', 'other'
        return np.nan # Return NaN for these generic unknown terms
    
    mapping = {
        "bachelor's degree": "Bachelor's Degree", # More specific
        "bachelor's": "Bachelor's Degree",
        "bachelor": "Bachelor's Degree",
        "master's": "Master's Degree",
        "master": "Master's Degree",
        "high school or equivalent": "High School",
        "high school": "High School",
        "metric": "Matriculation",
        "matric": "Matriculation",
        "intermidi": "Intermediate",
        "intermediate": "Intermediate",
        "inter": "Intermediate",
        "graduate": "Graduate", # Could be Bachelor or Master, might need context
        "graduated": "Graduate",
        "undergraduate": "Undergraduate", # Student pursuing Bachelor
        "bba": "Bachelor's Degree", # Assuming BBA is a Bachelor's
        "software engineering": "Bachelor's Degree", # Assuming it's a degree title
        "bachelors in computer science": "Bachelor's Degree",
        "9th": "Schooling", # A more general category for below Matric/High School
        "enter": "Schooling", # Assuming 'Enter' means entered some level of schooling
        "postgraduate": "Postgraduate"
    }
    
    edu_lower = edu_str.lower()
    for key, value in mapping.items():
        if key in edu_lower:
            return value
    # If no specific mapping found, but it's not 'Unknown' etc., keep original title-cased
    # Or decide to map to 'Other' category if it's too varied. For now, keep as is.
    return edu_str if len(edu_str) > 3 else np.nan # Avoid very short, unclear entries like 'Nan'

def clean_income(income):
    income_str = str(income).strip()
    if not income_str or income_str.lower() in ['unknown', 'none', '-', 'nan', 'not sure', '0', '00000??', '_']: # Added more unknown markers
        return np.nan
    
    # Standardize currency symbols and separators
    income_str = income_str.replace(',', '').replace('₹', 'rs').replace('rupees', 'rs')
    
    # Regex to find numbers, allowing for ranges like "X-Y" or "X/Y"
    numbers = re.findall(r'\d+\.?\d*', income_str) # Gets all numbers, including decimals
    
    if not numbers:
        # Handle cases like "Online game boosting, earn average figure" or textual descriptions
        if "below pkr 20000" in income_str.lower(): return "Below PKR 20,000"
        if "above pkr 100k" in income_str.lower(): return "Above PKR 100k"
        if "student" in income_str.lower(): return "Student (Likely Low/No Income)" # Special category for students
        return "Other_Textual" # If numbers can't be extracted and not student

    # Convert extracted numbers to float
    num_values = [float(n) for n in numbers]

    # If it's a range X-Y or X/Y, take the average or the first number for simplicity
    # For this EDA, let's use the first number found if multiple, or average if it's clearly a range
    # This part can be very complex; a simpler approach for now:
    amount = num_values[0]

    # Check for currency indicators
    is_pkr = 'pkr' in income_str.lower() or 'rs' in income_str.lower()
    is_usd = '$' in income_str

    if is_pkr:
        if amount < 20000: return "Below PKR 20,000"
        elif amount < 50000: return "PKR 20k–50k"
        elif amount < 100000: return "PKR 50k–100k"
        else: return "Above PKR 100k"
    elif is_usd:
        # If it was a range like $1000 - $2000
        if len(num_values) > 1 and (income_str.count('-') > 0 or income_str.count('/') > 0):
             return f"${int(num_values[0])} - ${int(num_values[1])}" # Keep as range string
        return f"${int(amount)}" # Single USD amount
    elif "k" in income_str.lower(): # e.g. 3k - 5k (could be PKR or other)
        # Assuming PKR if not specified for "k" amounts common in Pakistan context
        if amount * 1000 < 20000: return "Below PKR 20,000"
        elif amount * 1000 < 50000: return "PKR 20k–50k"
        elif amount * 1000 < 100000: return "PKR 50k–100k"
        else: return "Above PKR 100k"
    
    # If it's just a number without clear currency, and it's large, assume PKR
    # This is heuristic
    if amount >= 20000 and amount <= 500000: # Plausible large PKR amounts
        if amount < 20000: return "Below PKR 20,000" # Redundant here but for clarity
        elif amount < 50000: return "PKR 20k–50k"
        elif amount < 100000: return "PKR 50k–100k"
        else: return "Above PKR 100k"

    return "Other_Numeric" # Fallback for unclassified numeric income

# Robust cleaning functions for numeric-like columns that user wants to cap
def robust_clean_hours(hours):
    try:
        val = float(hours)
        return val if 0 <= val <= 24 else np.nan # Cap hours at 24
    except (ValueError, TypeError):
        return np.nan

def robust_clean_player_level(level):
    try:
        val = float(level)
        return val if 0 <= val <= 100 else np.nan # Cap player level at 100
    except (ValueError, TypeError):
        return np.nan

# Corrected cleaning_map (using actual column names from your data)
cleaning_map = {
    'age': clean_age,
    'gender': clean_gender,
    'city': clean_city,
    'country': clean_city, # Using clean_city for country as well, with specific fixes inside
    'education_level': clean_education,
    'monthly_income_bracket': clean_income,
    'earning_bracket': clean_income,
    'hours_played_per_day': robust_clean_hours,
    'playerlevel': robust_clean_player_level
}

# Apply cleaning functions
for col, func in cleaning_map.items():
    if col in df.columns:
        df[col] = df[col].apply(func)
    else:
        print(f"Warning: Column '{col}' not found in DataFrame. Skipping cleaning for it.")

print("Cleaning functions applied.")
print("NaNs and original data structure (rows/cols) are preserved as requested.")
print("Skipped fillna and data removal steps from original script.\n")


# --- 2. EXPLORATORY DATA ANALYSIS (EDA) ---
print("--- Starting Exploratory Data Analysis ---")

# A. Basic DataFrame Information
print("\n--- A. Basic DataFrame Information ---")
print("\n1. DataFrame Shape (rows, columns):")
print(df.shape)

print("\n2. DataFrame Info (data types, non-null counts):")
df.info() # This will show NaNs by comparing Non-Null Count to total entries

print("\n3. First 5 Rows (Head):")
print(df.head())

print("\n4. Last 5 Rows (Tail):")
print(df.tail())

# B. Descriptive Statistics
print("\n--- B. Descriptive Statistics ---")
print("\nDescriptive statistics for all columns (including NaNs in counts for categoricals):")
# For object columns, describe will show count, unique, top, freq. NaNs are not included in 'count' here by default for object.
# For numerical columns, NaNs are excluded from calculations like mean, std, etc.
print(df.describe(include='all'))


# C. Missing Value Analysis (Keeping NaNs)
print("\n--- C. Missing Value Analysis ---")
print("\n1. Count of NaN values per column:")
nan_counts = df.isnull().sum()
print(nan_counts[nan_counts > 0]) # Only show columns with NaNs

print("\n2. Percentage of NaN values per column:")
nan_percentage = (df.isnull().sum() / len(df)) * 100
print(nan_percentage[nan_percentage > 0]) # Only show columns with NaNs

# Visualizing missing values
if df.isnull().sum().sum() > 0: # Only plot if there are any NaNs
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Heatmap of Missing Values')
    plt.show()
else:
    print("\nNo missing values found in the dataset after initial cleaning to NaN conversion.")


# D. Data Types Check (Post-Cleaning)
print("\n--- D. Data Types ---")
print("\nData types of columns after cleaning:")
print(df.dtypes)


# E. Univariate Analysis (Analyzing individual columns)
print("\n--- E. Univariate Analysis ---")

# Identify numerical and categorical columns for targeted analysis
# After your cleaning, 'age', 'hours_played_per_day', 'playerlevel' should be numeric.
# Other columns are likely object/categorical.
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

print(f"\nIdentified Numerical Columns: {numerical_cols}")
print(f"Identified Categorical Columns: {categorical_cols}")

# E1. Numerical Columns
print("\nE1. Numerical Column Analysis:")
for col in numerical_cols:
    print(f"\n--- Analyzing: {col} ---")
    print(f"Basic Stats:\n{df[col].describe()}")
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    sns.histplot(df[col].dropna(), kde=True) # dropna for plotting, NaNs are still in df
    plt.title(f'Histogram of {col}')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df[col].dropna()) # dropna for plotting
    plt.title(f'Box Plot of {col}')
    
    plt.tight_layout()
    plt.show()

# E2. Categorical Columns
print("\nE2. Categorical Column Analysis:")
for col in categorical_cols:
    print(f"\n--- Analyzing: {col} ---")
    # Using dropna=False to include NaNs in value counts
    print(f"Value Counts (including NaNs):\n{df[col].value_counts(dropna=False)}")
    
    # Plotting value counts (top N categories for readability if too many)
    plt.figure(figsize=(10, 6))
    counts = df[col].value_counts(dropna=False)
    if len(counts) > 15:
        counts.nlargest(15).plot(kind='bar')
        plt.title(f'Bar Plot of Top 15 Categories for {col} (includes NaNs if present)')
    else:
        counts.plot(kind='bar')
        plt.title(f'Bar Plot of {col} (includes NaNs if present)')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# F. Bivariate Analysis (Analyzing relationships between two columns)
print("\n--- F. Bivariate Analysis ---")

# F1. Correlation Matrix for Numerical Columns
if len(numerical_cols) > 1:
    print("\nF1. Correlation Matrix (Numerical Columns):")
    correlation_matrix = df[numerical_cols].corr()
    print(correlation_matrix)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Numerical Columns')
    plt.show()
else:
    print("\nNot enough numerical columns for a correlation matrix.")

# F2. Scatter plots for pairs of numerical variables (example)
if 'age' in numerical_cols and 'hours_played_per_day' in numerical_cols:
    print("\nF2. Scatter Plot Example (Age vs. Hours Played):")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='age', y='hours_played_per_day', data=df.dropna(subset=['age', 'hours_played_per_day']))
    plt.title('Age vs. Hours Played Per Day')
    plt.show()

# F3. Box plot of a numerical column grouped by a categorical column (example)
if 'age' in numerical_cols and 'gender' in categorical_cols:
    print("\nF3. Grouped Box Plot Example (Age by Gender):")
    plt.figure(figsize=(8, 6))
    # df for boxplot should handle NaNs in 'gender' by creating a separate category or ignoring
    # sns.boxplot by default will not plot NaN categories unless explicitly handled
    # To show NaN as a category, you might need to fill it with a string like 'Unknown' temporarily for the plot
    df_temp_gender = df.copy()
    df_temp_gender['gender'] = df_temp_gender['gender'].fillna('Unknown_Gender_Plot')
    sns.boxplot(x='gender', y='age', data=df_temp_gender.dropna(subset=['age']))
    plt.title('Age Distribution by Gender (NaNs in Gender shown as Unknown_Gender_Plot)')
    plt.show()

# F4. Crosstabs for pairs of categorical columns (example)
if 'gender' in categorical_cols and 'gamedifficulty' in categorical_cols:
    print("\nF4. Crosstab Example (Gender vs. Game Difficulty):")
    # Using dropna=False to include NaNs in the margins and counts
    crosstab_gender_difficulty = pd.crosstab(df['gender'], df['gamedifficulty'], dropna=False, margins=True)
    print(crosstab_gender_difficulty)
    
    # Plotting the crosstab (excluding margins for clarity in plot)
    # For plotting, we usually don't plot the 'All' (margins)
    # And for NaNs in categories, they will be plotted if value_counts included them.
    # Crosstab plot can be done via stacked bar chart
    pd.crosstab(df['gender'].fillna('NaN'), df['gamedifficulty'].fillna('NaN')).plot(kind='bar', stacked=True, figsize=(10,7))
    plt.title('Gender vs Game Difficulty (NaNs shown as "NaN")')
    plt.ylabel('Count')
    plt.show()


print("\n--- EDA Complete ---")
# You can save the cleaned DataFrame if needed, it still contains NaNs:
# df.to_csv('cleaned_gaming_data_with_nans.csv', index=False)
# print("\nCleaned data with NaNs saved to 'cleaned_gaming_data_with_nans.csv'")