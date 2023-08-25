import pandas

db = pandas.read_csv('Automobile_data.csv')

db = db [['company','price']][db.price==db['price'].max()]

print(db)
