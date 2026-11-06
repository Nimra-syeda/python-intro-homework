# Warmup 4: FizzBuzz
# Loop from 1 to 30 and print one word per line:

# "FizzBuzz" if the number is divisible by both 3 and 5
# "Fizz" if divisible by 3 only
# "Buzz" if divisible by 5 only
# The number itself otherwise

for num in range(1,31):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    