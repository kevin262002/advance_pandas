import pandas

db = pandas.read_csv('Automobile_data.csv')

a = db.groupby('company')

b = a.get_group('audi')

print(b)
