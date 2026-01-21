import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

b= data * 10 # все элементы массива умножаем на 10
print(b)

c= data + data # сложение элементов массива
print(c)

size = data.shape
type_array = data.dtype

print(size, type_array) # размер массива по каждому имзерению, через кортеж shape, и тип данных

