import pandas as pd
import os
import csv

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def read_csv_from_path(path):
    try:
        csv_file = pd.read_csv(path)
        return csv_file
    except Exception as e:
        print(e)


def path_for_csv_file(filename):
    try:
        csv_file = 'DataSets/' + filename + '.csv'
        return os.path.join(ROOT_PATH, csv_file)
    except Exception as error:
        print(error)


class DataHandler:

    files = [
        'Production', 
        'Failures', 
        'Defected_Parts', 
        'Sales', 
        'Employees', 
        'Shifts', 
        'Customers'
    ]

    datasets = {}
    
    featured_datasets = {}

    def __init__(self):
        # Load DataSets
        for filename in self.files:
            self.datasets[filename] = read_csv_from_path(path_for_csv_file(filename))

    def join_production_sales(self):
        result = self.join('Production','Sales')
        return result

    def join_production_defected(self):
        result = self.join('Production', 'Defected_Parts', column = 'Box RFID')
        return result

    def join_shifts_employees(self):
        result = self.join('Shifts','Employees', column = 'Emp ID')
        return result
        
    def join(self, ds1_name, ds2_name, column = None):
        try:
            ds1 = self.datasets[ds1_name]
            ds2 = self.datasets[ds2_name]
            print("%s index is %s" % (ds1_name, ds1.index))
            print("%s index is %s" % (ds2_name, ds2.index))
            if column != None:
                print("Selected Column Is %s" % (column))
                # print(ds1[column].head())
                # print(ds2[column].head())
                result = pd.merge(ds1, ds2,how='inner', on=column)
                return result
            else:
                return pd.concat([ds1,ds2], axis=1, join_axes=[ds1.index])
        except Exception as e:
            print(e)

    def list_all_columns(self, selected_columns = []):
        all_df_columns = {}
        iterated_dfs = []
        if not selected_columns:
            iterated_dfs = self.files
        else:
            iterated_dfs = selected_columns
        for df_name in iterated_dfs:
            df = self.datasets[df_name]
            all_df_columns[df_name] = list(df)
        return all_df_columns

    def __str__(self):
        rep = ''
        for filename in self.files:
            rep += "\n--------------------" \
                   "\n%s" \
                   "\n--------------------" \
                   "\n%s" \
                   % (filename, self.datasets[filename].head())
        return rep
# Generate Alternate DataSets - Combine DataSets & Create New Fact Variables

# Save Generated DataSets

