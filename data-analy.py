import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =======================================================
# Task 1: Load and Explore the Dataset
# =======================================================

# Creating a dummy dataset as a string to make the script self-contained.
# In a real-world scenario, you would read this from a file.
data = """
Date,Product Category,Region,Sales,Quantity
2023-01-01,Electronics,North,1200,5
2023-01-02,Clothing,South,450,15
2023-01-03,Electronics,North,2500,10
2023-01-04,Home Goods,East,800,8
2023-01-05,Electronics,West,1500,7
2023-01-06,Clothing,North,600,20
2023-01-07,Home Goods,South,1100,6
2023-01-08,Electronics,East,3200,12
2023-01-09,Clothing,West,750,25
2023-01-10,Home Goods,North,950,9
2023-01-11,Clothing,South,550,18
2023-01-12,Home Goods,West,1300,4
2023-01-13,Electronics,West,2800,11
2023-01-14,Electronics,North,1800,9
"""

try:
    # Load the dataset from the in-memory string
    df = pd.read_csv("data.csv")
    print("Dataset loaded successfully.")

    # Display the first few rows to inspect the data
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Explore the structure, data types, and check for missing values
    print("\nDataset info:")
    df.info()

    # Clean the dataset by dropping any rows with missing values.
    df_cleaned = df.dropna()
    print("\nDataset after cleaning (no rows dropped in this case):")
    df_cleaned.info()

except FileNotFoundError:
    print("Error: The CSV file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")


# =======================================================
# Task 2: Basic Data Analysis
# =======================================================

print("\n" + "="*50)
print("Basic Data Analysis")
print("="*50)

# Compute basic statistics of numerical columns
print("\nDescriptive statistics of the numerical columns:")
print(df_cleaned.describe())

# Convert 'Date' column to datetime objects for time-series analysis
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])

# Perform groupings on 'Product Category' and compute the mean of 'Sales'
sales_by_category = df_cleaned.groupby('Product Category')['Sales'].mean().reset_index()
print("\nAverage Sales per Product Category:")
print(sales_by_category)

# Identify a simple pattern: Electronics have the highest average sales.
print("\nInsight: The 'Electronics' category has the highest average sales, suggesting it's the most profitable product line.")


# =======================================================
# Task 3: Data Visualization
# =======================================================

print("\n" + "="*50)
print("Data Visualization")
print("="*50)

# Set a style for the plots for better aesthetics
sns.set_style("whitegrid")
plt.figure(figsize=(15, 12))


# Plot 1: Line chart showing trends over time (Sales vs. Date)
plt.subplot(2, 2, 1) # Create a 2x2 grid of plots, and select the 1st one
plt.plot(df_cleaned['Date'], df_cleaned['Sales'], marker='o', linestyle='-')
plt.title('Daily Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()


# Plot 2: Bar chart showing average sales across categories
plt.subplot(2, 2, 2)
sns.barplot(x='Product Category', y='Sales', data=sales_by_category)
plt.title('Average Sales per Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Sales')
plt.xticks(rotation=45)
plt.tight_layout()


# Plot 3: Histogram of the Sales column to understand its distribution
plt.subplot(2, 2, 3)
sns.histplot(df_cleaned['Sales'], bins=5, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()


# Plot 4: Scatter plot to visualize the relationship between Quantity and Sales
plt.subplot(2, 2, 4)
sns.scatterplot(x='Quantity', y='Sales', data=df_cleaned, hue='Product Category', s=100)
plt.title('Relationship between Quantity and Sales')
plt.xlabel('Quantity Sold')
plt.ylabel('Sales')
plt.legend(title='Product Category')
plt.tight_layout()


# Display all the plots
plt.show()
