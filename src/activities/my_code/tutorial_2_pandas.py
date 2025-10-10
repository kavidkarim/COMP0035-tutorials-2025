def main():
    tutorial_202()

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


if __name__ == "__main__":
    main()