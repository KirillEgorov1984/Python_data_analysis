#1. Создание кортежа
tup = (1,2,3,4,5)
print(tup[0])
print(tup[-1])
#2. Индексация
t = (10, 20, 30, 40, 50)
print(t[1])
print(t[-2])
#3 Срезы (slice)
t = (1, 2, 3, 4, 5, 6, 7)
print(t[0:3])
print(t[-2:])
print(t[1::2])
#4. Длина кортежа
t = (5, 8, 2, 9, 1, 7)
print(len(t))
#5. count()
t = (1, 2, 2, 3, 2, 4)
show = t.count(2)
print(show)
#6. index()
t = (5, 3, 7, 3, 9)
show = t.index(3)
print(show)
#7. Проверка наличия
t = (1, 4, 6, 8)
print(10 in t)
#8. Простая распаковка
t = (100, 200, 300)
a, b, c = t
print(a)
print(b)
print(c)
#9. Расширенная распаковка
t = (1, 2, 3, 4, 5)
a,b,*_ = t
print(a)
print(b)
print(*_)
#10. Игнорирование значений
t = (10, 20, 30)
first = t[0]
last = t[-1]
print(first)
print(last)
#11. Доступ к вложенным данным
data = (
    ("Иван", 25),
    ("Анна", 30),
    ("Олег", 22)
)

print(data[1][1])
#12. Перебор
data = (
    ("Иван", 25),
    ("Анна", 30),
    ("Олег", 22)
)

for a in data:
    print(a)
#13. Найти максимум
data = (
    ("Иван", 25),
    ("Анна", 30),
    ("Олег", 22)
)
oldest = max(data, key=lambda x: x[1])
print(oldest)

max_person = data[0]

for person in data:
    if person[1] > max_person[1]:
        max_person = person

print(max_person)

#14. Фильтрация
sales = (
    ("apple", 100),
    ("banana", 50),
    ("orange", 75)
)
for item in sales:
    if item[1] > 60:
        print(item)
#Через list comprehension (продвинутый вариант)
result = [product for product, value in sales if value > 60]
print(result)