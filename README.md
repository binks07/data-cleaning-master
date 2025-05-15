# Data Cleaning Master

A Streamlit application that helps you clean your datasets with just a few clicks. Upload your data, and let the app handle duplicates and missing values intelligently using Python(Pandas).

## Features

- **Intuitive Upload**: Support for CSV and Excel files
- **Duplicate Detection**: Automatically identifies and separates duplicate records
- **Smart Missing Value Handling**:
  - Numeric columns: Replaces nulls with mean values
  - Categorical columns: Removes rows with missing values
- **Progress Tracking**: Visual indicators of the cleaning process
- **Instant Download**: Get your cleaned data and duplicates as CSV files
- **Data Preview**: See your data before and after cleaning

## 🚀 Quick Start

### Online Usage
Simply visit the https://data-cleaning-master.streamlit.app/ and upload your file!

## 🔧 How It Works

1. **Upload** your CSV or Excel file
2. **Name** your dataset
3. **Click** the "Clean Data" button
4. The app will:
   - Detect and separate duplicates
   - Handle missing values (mean for numeric, drop for categorical)
   - Show you the results
5. **Download** your cleaned data

## 🔜 Future Plans

- Data visualization tools
- Outlier detection and handling
- Custom rules for missing value treatment
- Data transformation options
- API integration
