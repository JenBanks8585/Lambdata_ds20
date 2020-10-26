print("hello")

# from module import function
# or from lambdata20.mymod import enlarge


from pandas import DataFrame
from mymod import enlarge

print(enlarge(2))

df = DataFrame({'A' :[2, 4] })
print(df.head())