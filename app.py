# Data Cleaning App - Streamlit Version
'''
This application takes datasets and cleans the data.
Features:
- Upload CSV or Excel files
- Detect and remove duplicates
- Handle missing values (mean for numeric, drop for categorical)
- Download cleaned data
'''

# Import dependencies
import pandas as pd
import numpy as np
import streamlit as st
import io
import time

def data_cleaning_master(uploaded_file, data_name):
    # Check the file type
    if uploaded_file.name.endswith('.csv'):
        st.info("Processing CSV file")
        data = pd.read_csv(uploaded_file, encoding_errors='ignore')
        
    elif uploaded_file.name.endswith('.xlsx'):
        st.info("Processing Excel file")
        data = pd.read_excel(uploaded_file)
        
    else:
        st.error("Unknown file type, please upload CSV/Excel file!")
        return None, None
    
    # Show number of records
    st.write(f"Number of rows: {data.shape[0]}, Number of columns: {data.shape[1]}")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Start with cleaning
    status_text.text("Checking for duplicates...")
    progress_bar.progress(20)
    
    duplicates = data.duplicated()
    total_duplicates = duplicates.sum()
    
    st.write(f"Dataset has total duplicate records: {total_duplicates}")
    
    # Saving the duplicates
    duplicate_records = None
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        st.write("Duplicate records found and separated")
    
    # Deleting the duplicates 
    status_text.text("Removing duplicates...")
    progress_bar.progress(40)
    df = data.drop_duplicates()
    
    # Finding missing values
    status_text.text("Checking for missing values...")
    progress_bar.progress(60)
    
    total_missing_value = df.isnull().sum().sum()
    missing_value_per_column = df.isnull().sum()
    
    st.write(f"Total missing values in the dataset: {total_missing_value}")
    if total_missing_value > 0:
        st.write("Missing values by columns:")
        st.write(missing_value_per_column[missing_value_per_column > 0])
    
    # Dealing with missing values
    status_text.text("Handling missing values...")
    progress_bar.progress(80)
    
    columns = df.columns
    
    for col in columns:
        # Filling mean for numeric columns
        if df[col].dtype in ('float64', 'int64'):
            df = df.copy()
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].mean())
                st.write(f"Filled missing values in {col} with mean")
            
        else:
            # Dropping rows with missing records for non number column
            before_rows = df.shape[0]
            df = df.dropna(subset=[col])
            after_rows = df.shape[0]
            if before_rows > after_rows:
                st.write(f"Dropped {before_rows - after_rows} rows with missing values in column {col}")
    
    status_text.text("Cleaning completed!")
    progress_bar.progress(100)
    
    # Data is cleaned
    st.success(f"Dataset cleaned successfully! Final dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    
    return df, duplicate_records

def main():
    st.set_page_config(page_title="Data Cleaning Master", page_icon="🧹")
    
    st.title("Data Cleaning Master 🧹")
    st.markdown("Upload your CSV or Excel file for data cleaning")
    
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        data_name = st.text_input("Enter a name for your dataset", "MyCleanData")
        
        if st.button("Clean Data"):
            with st.spinner('Cleaning in progress...'):
                cleaned_data, duplicate_records = data_cleaning_master(uploaded_file, data_name)
                
                if cleaned_data is not None:
                    st.subheader("Preview of Cleaned Data")
                    st.dataframe(cleaned_data.head())
                    
                    # Download options
                    csv = cleaned_data.to_csv(index=False)
                    st.download_button(
                        label="Download Cleaned Data as CSV",
                        data=csv,
                        file_name=f'{data_name}_Clean_data.csv',
                        mime='text/csv',
                    )
                    
                    if duplicate_records is not None and not duplicate_records.empty:
                        st.subheader("Preview of Duplicate Records")
                        st.dataframe(duplicate_records.head())
                        
                        csv_dup = duplicate_records.to_csv(index=False)
                        st.download_button(
                            label="Download Duplicate Records as CSV",
                            data=csv_dup,
                            file_name=f'{data_name}_duplicates.csv',
                            mime='text/csv',
                            key='download_duplicates'
                        )

if __name__ == "__main__":
    main()