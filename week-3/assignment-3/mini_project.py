# Day Planner
day = input("What day is it?").strip().lower()
time = input("What time of day?").strip().lower()

if day == "monday"  and time == "morning":
    print("Suggestion: Great Time to learn.")
elif day == "monday" and time == "afternoon":
    print("Suggestion: Have lunch.")
elif day == "monday" and time == "evening":
    print("Suggestion: Time to Excercise.")
elif day == "tuesday" and time == "morning":
    print("Suggestion: Priortize task of the day.")
elif day == "tuesday" and time == "afternoon":
    print("Suggestion: Pick kid from school.")  
elif day == "tuesday" and time == "evening":
    print("Suggestion: Drop kid to a class.")
elif day == "wednesday" and time == "morning":
    print("Suggestion: Great Time to focus.")
elif day == "wednesday" and time == "afternoon":
    print("Suggestion: Time to cook." )
elif day == "wednesday" and time == "evening":
    print("Suggestion: Visit library!")
elif day == "thursday" and time == "morning":
    print("Suggestion: Great time to learn.")   
elif day == "thursday" and time == "afternoon":
    print("Suggestion: You have a doctor appointment at 2 pm.")
elif day == "thursday" and time == "evening":
    print("Suggestion: Time to Excercise.")
elif day == "friday" and time == "morning":
    print("Suggestion: Prioritize task of the day.")
elif day == "friday" and time == "afternoon":
    print("Suggestion: Time for grocery shopping")
elif day == "friday" and time == "evening":
    print("Suggestion: Perfect time to watch movie.")

else:
    print("Sorry, I don't recognise that day and time. Please try day: monday - friday, time: morning,afternoon and evening.")

    