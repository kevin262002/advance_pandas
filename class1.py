import pandas

db = pandas.read_csv('Automobile_data.csv')

print("First Five Lines...")
print(db.head(5))

print("Last Five Lines...")
print(db.tail(5))
 
