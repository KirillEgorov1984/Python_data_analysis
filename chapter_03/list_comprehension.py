#Обычный цикл:
result = []
for x in range(5):
    result.append(x * 2)
print(result)

#С list comprehension это пишется так:
result = [x * 2 for x in range(5)]
print(result)

#[выражение for переменная in iterable if условие]