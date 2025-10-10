def main():
    csv_df, xlsx_df_0, xlsx_df_1 = tutorial_202()
    tutorial_203(csv_df)


def tutorial_201():
    #python file structures

    from pathlib import Path

    #Going to define the project root as the activites folder. Parent of this file is my_code, parent of that is activies

    code_root = Path(__file__).parent
    project_root = Path(code_root).parent

    #Now go down from project root (which is the activies folder) into the location you want using names

    paralympics_csv = project_root / 'data' / 'paralympics_raw.csv'

    if paralympics_csv.exists():
        print(f"CSV found: {paralympics_csv}")
    else:
        print("CSV file not found")

def tutorial_202():

    #tutorial 2.02 - Pandas dataframes
    import pandas as pd
    
    #get parent folder
    from pathlib import Path
    project_root = Path(__file__).parent.parent

    #get needed files
    paralympics_csv = project_root / 'data' / 'paralympics_raw.csv'
    paralympics_xlsx = project_root / 'data' / 'paralympics_all_raw.xlsx'

    #get the csv as a dataframe
    csv_df = pd.read_csv(paralympics_csv)
    xlsx_df_0 = pd.read_excel(paralympics_xlsx)
    xlsx_df_1 = pd.read_excel(paralympics_xlsx, sheet_name=1)

    return(csv_df, xlsx_df_0, xlsx_df_1)

def tutorial_203(dataframe):
    import pandas as pd

    """This function will return info about a passed in dataframe
    
    Parameters:
    dataframe (dataframe): dataframe

    Returns:
    str: Description of the dataframe

    """

    print(dataframe.shape)
    pd.set_option("display.max_columns", None)
    print(dataframe.head)
    print(dataframe.tail)
    print(dataframe.columns)
    print(dataframe.dtypes)
    print(dataframe.info)
    print(dataframe.describe)



if __name__ == "__main__":
    main()