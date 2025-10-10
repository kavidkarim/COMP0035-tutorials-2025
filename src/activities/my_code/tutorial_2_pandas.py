def main():
    tutorial_201()

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
    print("starting")


if __name__ == "__main__":
    main()