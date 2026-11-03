# Mini-Project — Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
choice = 0

while choice != 5:
   print("=== Number Cruncher ===")
   print("1. Find minimum")
   print("2. Find maximum")
   print("3. Search for a number")
   print("4. Sort the list")
   print("5. Quit")
   choice = int(input("Choose an option (1-5): "))
 
# Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
   if choice == 1:
    minimum_number = numbers[0]
    for num in numbers:
       if num < minimum_number:
        minimum_number =num
    print("The minimum number is:",minimum_number)
# Find maximum — same approach, tracking the largest value. Do not use max().
   elif choice == 2:
       maximum_number =numbers[0]
       for num in numbers:
           if num > maximum_number:
               maximum_number = num
       print("The maximum number is:",maximum_number)
# Search — ask the user for a number, then implement a linear search loop.
   elif choice ==3:
       target = int(input("Enter the number to search for: "))
       index = -1 #initialize the index to -1 "number not found"
       #Linear search through the list to find the target number
       for i in range(len(numbers)):
          if numbers[i] == target:
            index = i
            print("Number found at index:", index)
            break
       if index ==-1:
          print("Number not found")
 # Sort — implement bubble sort
       
   elif choice == 4:
       swapped = True
       while swapped:
           swapped = False
           for i in range(len(numbers)-1):
               if numbers[i]> numbers[i+1]:
                   numbers[i],numbers[i+1] =  numbers[i+1],numbers[i]
                   swapped = True
       print("Sorted list:", numbers) 
 # Quit — print a goodbye message and exit the loop.      
   elif choice == 5:
       print("Goodbye!")
       break
   else:
       print("Invalid choice.Please try again.")
    



