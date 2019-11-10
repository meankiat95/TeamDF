import pandas as pd

def tabulate(json_object_list,sheet_names,data_file_path):
    """This function converts all the json data objects into

    excel format via pandas dataframes and writes them to a single .xlsx
    file in separate sheets"""
    writer = pd.ExcelWriter(data_file_path,engine='xlsxwriter')
    for json_obj,sheet in zip(json_object_list,sheet_names):
        # converting json to dataframes
        df = pd.DataFrame(json_obj)
        # writing into excel sheets
        df.to_excel(writer,sheet_name=sheet)
    writer.save()
    print("Registry data has been extracted to data_registry folder as an excel sheet")
