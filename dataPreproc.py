import numpy as np
import pandas as pd

#We read the file
try:
    df = pd.read_parquet('challenge_campus_biomedico_2024.parquet')
except:
    raise Exception("no file was found")

print("Columns: %i" % len(df.columns))
print("Rows: %i" % df.shape[0])
print("Missing values:")
def percentage(x):
    return x/df.shape[0]
print( df.isna().sum().apply(percentage).where(lambda x : x!=0.00).dropna())
#We make an educated guess and conclude that certain rows have the same missing data
#df.dropna(subset = ['ora_inizio_erogazione', 'ora_fine_erogazione', 'codice_provincia_erogazione','codice_provincia_residenza'])
nanSeriesRows = df.isna().sum(axis=1)
print(nanSeriesRows.groupby(nanSeriesRows).size().apply(percentage).where(lambda x : x!=0.00).dropna())