import pandas as pd
price = pd.Series([2.99, 4.45, 1.36])
price_sum = price.sum() #сумма чисел
price_product = price.product() #произведение чисел
price_avg = price.mean() #среднее
price_std = price.std() # стандартное отклонение

print(price)
print(price_sum)
print(price_product)
print(price_avg)
print(price_std)
print(price, price_sum, price_product, price_avg, price_std)

