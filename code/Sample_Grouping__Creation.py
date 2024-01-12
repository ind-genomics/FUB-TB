import os
import pandas as pd
import  sys
from  random import sample

# Directory to load data

FunTB_dir = os.getcwd()

# Input arguments - python Sample_Grouping_Creation.py Metadata File.csv

metadata_file = sys.argv[1] # Metadata file (.csv)
file_path = os.path.join(FunTB_dir, os.path.join('Metadata_files',metadata_file)) # Metadata file path
metadata_df = pd.read_csv(file_path, encoding = 'utf-8') # Metadata file load

Selected_columns = sys.argv[2:]

# General functions 

def filter_dataframe(df, filter_dict):
    """
    Filter a DataFrame based on specified filter conditions.
    Parameters:
        - df: DataFrame to be filtered
        - filter_dict: Dictionary containing column names as keys and filter conditions as values
    Returns:
        - Filtered DataFrame
    """
    query_parts = []

    for column, value in filter_dict.items():
        if isinstance(value, str):
            query_parts.append(f"{column} == '{value}'")
        else:
            query_parts.append(f"{column} == {value}")

    query = " and ".join(query_parts)
    filtered_df = df.query(query)

    return filtered_df

def get_filters_conditions(df, group, column_name, filter_conditions):
    """
    This function prompts the user to enter a value for a specific column in a DataFrame and checks if the entered value
    exists in the DataFrame's column. It updates the filter_conditions dictionary with the entered value if it exists.

    Args:
        df (DataFrame): The DataFrame containing the data.
        column_name (str): The name of the column for which the user is prompted to enter a value.
        filter_conditions (dict): A dictionary containing filter conditions for different columns.

    Returns:
        value_flag (bool): A flag indicating whether the entered value was found in the DataFrame's column.
        filter_conditions (dict): The updated filter_conditions dictionary.

    """
    value = input(str(column_name) + ' value for ' + 'group ' + str(group) + ' ' + str(set(df[column_name].values)) + ': ')
    if value.isdigit():
      if int(value) in set(df[column_name].values):
        value_flag = True
        filter_conditions[column_name] = int(value)
      else:
        print('Value not found >:V, try again')
        value_flag = False
    else:
      if value in set(df[column_name].values):
        value_flag = True
        filter_conditions[column_name] = value
      else:
        print('Value not found >:V, try again')
        value_flag = False
    return value_flag, filter_conditions

def save_group_Ids(file_name, samples_Ids):
  """
    This function saves a list of sample IDs to a text file.

    Args:
        file_name (str): The name of the output file.
        samples_Ids (list): A list of sample IDs to be saved.

    Returns:
        None

  """
  with open(file_name + ".txt", "w") as output:
      output.write(str(samples_Ids))

def get_groups_names(number_of_groups):
   """
    Prompts the user to enter names for a specified number of groups.

    Args:
        number_of_groups (int): The number of groups for which to enter names.

    Returns:
        list: A list of group names entered by the user.
   """
   groups_names = []
   for i in range(number_of_groups):
      groups_names.append(input('Set name of groups ' + str(i+1) + ': '))
   return groups_names 
   
# Main program

number_of_groups = int(input('Set number of groups: '))
Groups_names = get_groups_names(number_of_groups)

for group in Groups_names:
  filter_conditions = {}
  for column_name in Selected_columns:
    value_flag = False
    while value_flag == False:
      value_flag,filter_conditions = get_filters_conditions(metadata_df, group, column_name, filter_conditions)
  filtered_data = filter_dataframe(metadata_df, filter_conditions)

  save_file = os.path.join(FunTB_dir, os.path.join('Samples_lists', group)) # list file and path

  save_group_Ids(save_file, list(filtered_data['ID']))