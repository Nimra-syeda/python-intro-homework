#Warmup 2: Input Validation with a While Loop
while True:
    try:    
        num = int(input("Enter a positive integer: "))
    
        if num >0:
           print("Got it :",num)
           break
        else:
           print("That's not a positive integer.Try again.")
    except ValueError:
        print("That's not a positive integer.Try again.")

       
        

 

    
    