from DataHandler import DataHandler
import itertools

data_handler = DataHandler()

try:
    print(data_handler)
    print("")
    df_names = data_handler.files
    df_combinations = itertools.combinations(df_names,2)
    for combination in df_combinations:
        common_columns = data_handler.list_all_columns(selected_columns=combination)
        column1 = common_columns.values()[0]
        column2 = common_columns.values()[1]
        intersection = set(column1).intersection(column2)
        if not intersection:
            continue
        print("Columns %s,%s Have %s in common" % (common_columns.keys()[0], common_columns.keys()[1], intersection))
    print("")
except Exception as e:
    print(e)