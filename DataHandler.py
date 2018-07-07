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

