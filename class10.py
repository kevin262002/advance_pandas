import pandas

db1 = pandas.DataFrame( {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
                         'Price': [23845, 17995, 135925 , 71400]})

db2 = pandas.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
                        'horsepower': [141, 80, 182 , 160]})

data1 = pandas.DataFrame(db1)
data2 = pandas.DataFrame(db2)

ans = data1.merge(data2)

print(ans)


