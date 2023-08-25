import pandas

db = pandas.read_csv('Automobile_data.csv')

db.fillna('NuN',inplace = True)

print(db)
