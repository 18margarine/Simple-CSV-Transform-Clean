import doc_reader, os

# DIRECTORY VARIABLES
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = 'CSV'
full_dir_search = os.path.join(base_dir,folder_name)
found_csv = None
# SEARCH CSV FILES ON THE DIRECTORY AND RETURN ONLY THE FIRST MATCH
for file in os.listdir(full_dir_search):
    if file.endswith('.csv'):
        found_csv = os.path.join(full_dir_search, file)
        break

if found_csv is not None:
    df_costumer, column_name_list = doc_reader.reader(found_csv)
    max_index = len(column_name_list) - 1
    while True:
    # PROMPT TO USER WHICH COLUMN TO CHOOSE
        column_filter = input('Which column you would like to filter, list index here separated by comma: ')
        try:
            listed_index = [item.strip() for item in column_filter.split(',')]
            if any(item == '' for item in listed_index):
                raise ValueError('Empty values detected. Remove extra commas.')
            filtered_column_index = [int(item) for item in listed_index]
            if any(num < 0 for num in filtered_column_index):
                raise ValueError('Select numbers only within the range of index.')
            if len(filtered_column_index) != len(set(filtered_column_index)):
                raise ValueError('Duplicate numbers detected, remove duplicate.')
            if any(num > max_index for num in filtered_column_index):
                raise ValueError('Select numbers only within the range of index.')
            break
        except ValueError as e:
            print(f'Invalid input: {e}')
            print(f'Please enter only valid integer separated by comma')

    # FILTER SELECTED COLUMN AND PROCESS BOTH CLEAN AND MISSING ROWS
    finished = doc_reader.filtered_csv(df_costumer,column_name_list,filtered_column_index)
    missing_disp, clean_disp = doc_reader.cleaning_csv(finished)
    # GENERATE A NEW CSV FILE IN THE BASE DIR
    clean_disp.to_csv('clean filtered.csv', index=False)
    missing_disp.to_csv('missing reports.csv', index=False)
else:
    print(f"No valid file found in {full_dir_search}.")