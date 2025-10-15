import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Configuration & Path Setup ---
sns.set_style("whitegrid")
file_name = 'D:\\lab programs\\Internship_tasks\\train_dataset.csv'

# Set the intended output directory.
# !!! IMPORTANT: Check this path is exactly where you want the images !!!
OUTPUT_DIR = r"D:\lab programs\Internship_tasks" 

# --- PATH FIX: Create the directory if it doesn't exist ---
try:
    # Use exist_ok=True so it doesn't raise an error if the directory is already there
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Ensured output directory exists: {OUTPUT_DIR}")
except OSError as e:
    print(f"Error creating directory {OUTPUT_DIR}: {e}")
    print("Please check if the D: drive is accessible and you have write permissions.")
    exit()
# ------------------------------------------------------------


# --- 1. Load the Data ---
csv_path = os.path.join(OUTPUT_DIR, file_name)
try:
    df = pd.read_csv(csv_path)
    print(f"Dataset '{file_name}' loaded successfully. Total rows: {len(df)}")
except FileNotFoundError:
    print(f"Error: The file '{csv_path}' was not found. Please check the file path.")
    exit()

# --- 2. Data Cleaning & Feature Engineering (Necessary steps) ---
print("\n--- Data Cleaning Summary ---")
# Age
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)
# Embarked
most_frequent_embarked = df['Embarked'].mode()[0]
df['Embarked'].fillna(most_frequent_embarked, inplace=True)
# Cabin
df.drop('Cabin', axis=1, inplace=True)
# Features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = np.where(df['FamilySize'] == 1, 1, 0)
print("Data cleaning and feature engineering complete.")


# --- 3. Exploratory Data Analysis (EDA) and Saving Plots ---

print("\n--- Generating Visualizations ---")
plots_generated = 0

# 1. Distribution of Age
plt.figure(figsize=(9, 5))
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Passenger Ages', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Count', fontsize=12)
save_path = os.path.join(OUTPUT_DIR, 'age_distribution.png')
plt.savefig(save_path)
plt.close()
plots_generated += 1

# 2. Survival by Sex
plt.figure(figsize=(7, 5))
sns.barplot(x='Sex', y='Survived', data=df, palette={'male':'teal', 'female':'coral'})
plt.title('Survival Rate by Gender', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
save_path = os.path.join(OUTPUT_DIR, 'survival_by_gender.png')
plt.savefig(save_path)
plt.close()
plots_generated += 1

# 3. Survival by Class
plt.figure(figsize=(7, 5))
sns.barplot(x='Pclass', y='Survived', data=df, palette='viridis')
plt.title('Survival Rate by Passenger Class', fontsize=16)
plt.xlabel('Passenger Class (1=1st, 2=2nd, 3=3rd)', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
save_path = os.path.join(OUTPUT_DIR, 'survival_by_pclass.png')
plt.savefig(save_path)
plt.close()
plots_generated += 1

# 4. Survival vs. Being Alone
plt.figure(figsize=(7, 5))
sns.barplot(x='IsAlone', y='Survived', data=df, palette='plasma')
plt.title('Survival Rate: Traveling Alone vs. With Family', fontsize=16)
plt.xlabel('Travel Status (0=With Family, 1=Alone)', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
plt.xticks([0, 1], ['With Family', 'Alone'])
save_path = os.path.join(OUTPUT_DIR, 'survival_by_alone_status.png')
plt.savefig(save_path)
plt.close()
plots_generated += 1

# 5. Correlation Matrix
corr_data = df[['Survived', 'Pclass', 'Age', 'Fare', 'FamilySize', 'IsAlone']]
plt.figure(figsize=(9, 7))
sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, linecolor='black')
plt.title('Correlation Matrix of Numerical Features', fontsize=16)
save_path = os.path.join(OUTPUT_DIR, 'correlation_matrix.png')
plt.savefig(save_path)
plt.close()
plots_generated += 1

print(f"\nSuccessfully generated {plots_generated} image files in: {OUTPUT_DIR}")
print("\n--- EDA Task Complete ---")