import pandas as pd
import numpy as np

# READ CSV FILE AND LIST ALL HEADER NAMES
def reader(file_loc):
    list_name = []
    df = pd.read_csv(file_loc)
    listed_column_names = df.columns.tolist()
    for index, item in enumerate(listed_column_names):
        print(f'Index {index} for column {item}')
        list_name.append(item)
    return df, list_name

# FILTER THE COLUMNS BASED ON USER INPUT
def filtered_csv(raw_csv, col_list, column_ind_list):
    f_list_name = []
    for i in column_ind_list:
        f_list_name.append(col_list[i])
    final_csv = raw_csv[f_list_name]
    return final_csv

# CREATE A SEPARATE CSV WITH CLEAN DATA AND CSV WITH MISSING DATA
def cleaning_csv(csv):
    # '^\s+$' to remove white spaces and replace with nan, regex=True to consider '^\s+$'
    # as a regular expression
    csv = csv.replace(r'^\s+$',np.nan, regex=True)
    # pick rows that have empty columns
    missing_df = csv[csv.isna().any(axis=1)]
    # pick rows that are complete
    clean_df = csv.dropna(how='any')
    return missing_df, clean_df