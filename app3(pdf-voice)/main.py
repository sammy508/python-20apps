import pandas as pnd
import glob

filepaths = glob.glob("invoices/*.xlsx")
print(len(filepaths))

for filepath in filepaths:
    df = pnd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)   