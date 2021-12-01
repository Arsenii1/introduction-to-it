ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

del ages[-1]
ages.insert(0,9)
ages.append(21)

first = ages[0]
last = ages[-1]

print({ 'first': first, 'last': last })
