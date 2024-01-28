import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    try:
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        print(df)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
