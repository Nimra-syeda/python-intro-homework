#Sign and Parity

num =int(input("Enter a number: "))

if num > 0:
    print(str(num) + " is positive.")
elif num < 0:
    print(str(num) + " is negative.") 
else:
    print(str(num)+ " is zero.")

if num % 2==0:
    print(str(num) + " is even.")
else:
    print(str(num) + " is odd.")