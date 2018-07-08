from DataHandler import DataHandler

data_handler = DataHandler()

try:
    print(data_handler)
    list = data_handler.list_all_columns(selected_columns=['Failures','Employees','Shifts'])
    print(list)

    print(data_handler.join_shifts_employees().head())
    # print(data_handler.join_production_defected().head())
except Exception as e:
    print(e)