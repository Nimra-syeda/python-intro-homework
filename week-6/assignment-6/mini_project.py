# Mini project- Refactor the Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("\nChoose an option (1-5): ")
    return choice     

# numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    """Return the smallest number
    in the list without changing it."""
    smallest = numbers[0]
    for i in range (len(numbers)):
        if  numbers[i] < smallest:
            smallest = numbers[i]
    return smallest

def find_max(numbers):
    """Return the maximum number 
    with out changing the list. """
    
    largest =numbers[0]
    for i in range(len(numbers)):
        if numbers[i] >largest:
            largest = numbers[i]  
    return largest  

def search(numbers, target):
    """Return the index of target in the list, 
    or -1 if it isn't found."""
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
    return  -1      
def bubble_sort(numbers):
    """Return a sorted copy of the list using bubble sort,
    leaving the original unchanged."""
    sorted_numbers= numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers)-1):
            if sorted_numbers[i]>sorted_numbers[i+1]:   
                sorted_numbers[i], sorted_numbers[i+1]= sorted_numbers[i+1],sorted_numbers[i]
                swapped =True
    return sorted_numbers


    
def main(): 
    
 while True:
    answer = show_menu()
    if answer == "1":
        print(f"\nMinimum number: {find_min(numbers)}.")
    elif answer =="2":
        print(f"\nMaximum number:{find_max(numbers)}.")
    elif answer == "3":
        target=int(input("\nEnter a number: "))
        index = search(numbers,target)
        if index != -1:
            print(f"\nFound at index {index}.")
        else:
            print()
            print("Not found")
    elif answer == "4":
        print()
        print(f"Sorted list: {bubble_sort(numbers)}")
        print(f"Original list:{numbers}")
    elif answer =="5":
        print("Good Bye!")
        break 
    else:
        print("\nInvalid number!Try again.\n")  
      
if __name__ == "__main__":
    main()

 