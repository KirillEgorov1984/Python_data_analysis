import numpy as np

arr1 = np.array([1,2,3], dtype=np.float64)
arr2 = np.array([1,2,3], dtype=np.int32)

type_arr1 = arr1.dtype
print(type_arr1)

type_arr2 = arr2.dtype
print(type_arr2)

float_arr2 = arr2.astype(np.float64) #преобразование масисива из одного типа данных в другой
print(float_arr2.dtype)