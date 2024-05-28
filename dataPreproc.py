def showNaN(data):
    print("Missing values:")
    print( data.isna().sum().where(lambda x : x!=0.00).dropna())
    
    print("Percentage of samples missing data:")
    nanSeriesRows = data.isna().sum(axis=1)
    print(nanSeriesRows.groupby(nanSeriesRows).size().where(lambda x : x!=0.00).dropna())