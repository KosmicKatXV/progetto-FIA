import pandas as pd
import dataPreproc
#We read the file
try:
    df = pd.read_parquet('challenge_campus_biomedico_2024.parquet')
except:
    raise Exception("no file was found")

print("Columns: %i" % len(df.columns))
print("Rows: %i" % df.shape[0])
#We check for NaN
print(dataPreproc.showNaN(df))
df = df.dropna(axis=0)
#We remove cancelled samples
df = df[pd.isnull(df['data_disdetta'])]
#We drop the column as it is empty
df = df.drop(columns=['data_disdetta'])
#As most of the the columns with missing information are redundant we can simply drop them
df = df.drop(columns=['codice_provincia_residenza',
                      'comune_residenza',
                      'codice_provincia_erogazione'])
#We drop all redundant columns
df = df.drop(columns=['regione_residenza',
                      'asl_residenza',
                      'descrizione_attivita',
                      'regione_erogazione',
                      'asl_erogazione',
                      'struttura_erogazione',
                      'tipologia_struttura_erogazione',
                      'tipologia_professionista_sanitario'])
#We drop the samples with no timestamp as they are less than 0.01 of the total
df = df.dropna(axis=0)
#We check that we no longer have NaN
print(dataPreproc.showNaN(df))

#Now we need to create a dataset from this one where each sample will represent a patient
patient_df = df[['id_paziente',
                 'data_nascita',
                 'sesso',
                 'codice_regione_residenza',
                 'codice_asl_residenza',
                 'provincia_residenza',
                 'codice_comune_residenza']]
df = df.drop(columns=['data_nascita',
                      'sesso',
                      'codice_regione_residenza',
                      'codice_asl_residenza',
                      'provincia_residenza',
                      'codice_comune_residenza'])

#We obtain can now concatenate new columns from the available data