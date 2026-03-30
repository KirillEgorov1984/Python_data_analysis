print('')
print('Definition')
tup = (4,5,6)
print (tup)
print(type(tup))

print('')
print('Converting to a tuple')

tup_ = tuple("string")
print (tup_)
print(type(tup_))

print('')
print('Accessing an element of a tuple')
print(tup_[0:4])

print('')
print('Big tuple')

nested_tup = (4, 5, 6), (7, 8)
print(nested_tup[0])
print(nested_tup[1])

print('')
print('Concatenating a tuple')

tuple_a = (4, 5, 6)
tuple_b = (7, 8)
print(tuple_a)
print(tuple_b)
print(tuple_a + tuple_b)

print('')
print('tuple multiplication')

tuple_с = (4, 5, 6) * 4
print(tuple_с)
