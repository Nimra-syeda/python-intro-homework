#List operations
#Create a hardcoded list of 8 numbers.
lists = [20,22,24,26,28,30,32,34]
print("First: ",lists[0])
print("Last: ",lists[-1])
middle =len(lists)//2
print("Middle: ",lists[middle-2:middle+2])
lists.reverse()
print("Reversed: ",lists)