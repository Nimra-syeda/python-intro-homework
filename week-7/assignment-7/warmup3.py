#Warmup 3: Use the os Module
import os 
#get the current working directory
print(os.getcwd())

path =os.path.exists('../data/expenses.csv')
if path:
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

join=os.path.join("..","data","expenses.csv")
print(join)

