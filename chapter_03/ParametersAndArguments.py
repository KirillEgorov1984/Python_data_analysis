import pandas as pd

fruits = ["Apple", "Orange", "Plum", "Grape", "Bluebbarry", "Watermelon", "Pineapple"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#
print(pd.Series(fruits))
print(pd.Series(weekdays))
print(pd.Series(fruits, weekdays))
print(pd.Series(weekdays, fruits))
print(pd.Series(data = fruits, index = weekdays))
print(pd.Series(index = weekdays, data = fruits))
print(pd.Series(fruits,  index = weekdays))
print(pd.Series())

