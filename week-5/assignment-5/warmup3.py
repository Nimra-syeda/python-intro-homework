#Linear Search
# Start with a hardcoded list of names. Ask the user to enter a name. 

students =['sarah','john','mary','amy','jazmine']
name  = input("Enter the name to search for : ").strip().lower()
index = -1 # initialize the index to -1 "not found"
for i in range(len(students)):
    if students[i] == name:
       index = i
       break
    
if index != -1: 
    print(f'Found "{name}" at index {index}.')
else:
    print(f' "{name}" was not found in the list.')




