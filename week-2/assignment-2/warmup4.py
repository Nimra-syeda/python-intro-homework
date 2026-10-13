# num_1 = input ("Enter the first number: ")
# num_2 =10
# sum =num_1 + num_2

# print(sum)
#  sum =num_1 + num_2
#        ~~~~~~^~~~~~~
#TypeError: can only concatenate str (not "int") to str
# In the above code,got a Type error because the input function always returns a value as a string,
# we cannot add a string and an integer together.
num_1 = int(input("Enter the number: "))
#first we need to convert the string to an integer usint int()function and then we can add the two numbers 
num_2 = 10
sum = num_1 + num_2
print(sum)