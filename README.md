# Internship Project: Titanic Data Analysis (EDA & Cleaning)

## 🎯 Project Goal

This project was completed as part of an internship task focusing on fundamental data science practices: **data cleaning**, **feature engineering**, and **Exploratory Data Analysis (EDA)**.

The objective was to analyze the famous Titanic survival dataset to identify crucial relationships, patterns, and trends that influenced a passenger's chance of survival.

---

## 🛠️ Technology & Libraries Used

| Tool/Library | Purpose |
| :--- | :--- |
| **Python** | Primary programming language |
| **Pandas** | Data loading, cleaning, and manipulation |
| **NumPy** | Numerical operations and array manipulation |
| **Matplotlib / Seaborn** | Data visualization and generating statistical plots |

---

## 🗂️ Repository Contents

* **`SCT_DS_2.py`**: The core Python script containing all data cleaning, feature engineering, and EDA logic.
* **`train_dataset.csv`**: The raw dataset used for the analysis.
* **`README.md`**: This file.
* **`*.png` files**: The generated visualization outputs (e.g., `survival_by_gender.png`, `correlation_matrix.png`).

---

## 🧹 Data Cleaning & Feature Engineering

Before analysis, the following steps were taken to ensure data quality and add analytical depth:

1.  **Missing Value Imputation:**
    * Missing **`Age`** values were filled using the **median** (to maintain robustness against outliers).
    * Missing **`Embarked`** values were filled using the **mode** (the most frequent port of embarkation).
2.  **Column Dropping:** The **`Cabin`** column was dropped due to an excessive number of missing values (over 77%).
3.  **Feature Creation:**
    * **`FamilySize`**: Created by combining `SibSp` (Siblings/Spouses) and `Parch` (Parents/Children) plus the passenger themselves (`+ 1`).
    * **`IsAlone`**: A binary (0/1) feature indicating whether the passenger was traveling by themselves.

---

## 📈 Key Findings & Trends

The Exploratory Data Analysis revealed several clear and statistically significant patterns:

1.  **Gender Bias (The "Women and Children First" Rule):**
    * **Trend:** Female passengers had a dramatically higher survival rate compared to male passengers.
2.  **Class Privilege:**
    * **Trend:** Passengers traveling in **First Class (`Pclass=1`)** were significantly more likely to survive than those in Third Class (`Pclass=3`), highlighting socio-economic influence.
3.  **Optimal Family Size:**
    * **Trend:** Passengers traveling in **small to medium-sized groups (FamilySize 2-4)** had the highest survival probability. Both traveling alone and being part of a very large family decreased the chances of survival.
4.  **Correlation Insights:**
    * **`Fare`** showed a moderate positive correlation with survival (higher fare, higher survival).
    * **`Pclass`** showed a strong negative correlation with survival (lower class number, higher survival).

---

## 🚀 How to Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPO_URL]
    cd Titanic_EDA_Internship
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  **Execute the Script:**
    ```bash
    python SCT_DS_2.py
    ```

The script will print the cleaning steps and observations to the console, and save all generated charts (`.png` files) into the project directory.
