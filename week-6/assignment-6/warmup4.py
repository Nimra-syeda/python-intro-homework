#Warmup 4
def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False
user_input = int(input("Enter the score: "))
# print(is_valid_score(user_input))
if is_valid_score(user_input):
    print("Valid Score")
else:
    print("Invalid score - must be between 0 and 100.")