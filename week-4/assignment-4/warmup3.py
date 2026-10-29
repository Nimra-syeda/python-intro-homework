# Set Operations


# Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:
course_1=['C++','C#','Python','Java']
course_2= ['Html','Python','Javascript','C#']

# Convert each list to the set
set_1= set(course_1)
set_2 = set(course_2)

# The union (all languages from both lists, no duplicates)
print(set_1.union(set_2))
# The intersection (languages in both lists)
print(set_1.intersection(set_2))
# The difference (languages only in the first list)
print(set_1.difference(set_2))