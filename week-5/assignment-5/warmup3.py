# Start with a hardcoded list of names. Ask the user to enter a name. 
# Loop through the list and print whether the name was found 
# and at what index — 
# or a not-found message if it isn't in the list
students =['Sarah','John','Mary','Amy','Jazmine']
name  = input("Enter the name to search for : ").strip().capitalize()
index = -1 
for i in range(len(students)):
    if students[i] == name:
       index = i
       break
    
if index != -1: 
    print(f'Found "{name}" at index {index}.')
else:
    print(f' "{name}" was not found in the list.')




