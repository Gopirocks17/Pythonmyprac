import pandas as pd

file='stats.ods'

xl=pd.Excelfile(file)

print(xl.sheet_names)
