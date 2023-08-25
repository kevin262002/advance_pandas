import pandas

db1 = pandas.DataFrame({'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
                        'Price': [23845, 171995, 135925 , 71400]})
print(db1)



db2 = pandas.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
                        'Price': [29995, 23600, 61500 , 58900]})
print(db2)

print('After Concatenating:')
print(pandas.concat([db1,db2]))




