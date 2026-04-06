tuple_number_one = (4, 5, 6)
a, b ,c = tuple_number_one
print(b)

print('-------------------------------')

a_, b_ = 1, 2
print(a_)
print(b_)

b_, a_ = a_, b_
print(a_)
print(b_)

print('-------------------------------')
print('List traversal')

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')

print('-------------------------------')
print('...rest')

values = 1,2,3,4,5,6,7,8,9
a, b, *rest = values
print(a)
print(b)
print(rest)
