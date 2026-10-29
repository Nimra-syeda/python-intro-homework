# A data file is provided in week-4/data/roster.py. Copy the students list from that file into your script — it contains dictionaries with name, score, and subject fields.
# Using loops and data structure operations, your script must:

# Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
# Calculate the class average — accumulate the total score in a loop, then divide.
# List all unique subjects — use a set to collect subjects as you loop, then print them.
# List high scorers — use a loop and .append() to get the names of all students who scored above 75.


students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},

]

# Set starting values for tracking the top student's name and score.
top_name = None
top_score = 0
# Check each student score in the list of dictionaries.
for student in students:
#When a higher score is found, save the score and student's name 
     if student['score'] > top_score:
         top_score = student['score']
         top_name = student['name']
print(f"Top scorer: {top_name} ({top_score})")

# Start the total at 0, then add each student's score
total = 0
for student in students:  
    total+= student['score']
    #Divide the total by the number of students to calculate the class average
average = total/len(students)

print(f"Class average: {average:.2f}")

# create an empty set to collect unique subjects and avoid duplicates.
category = set()
for student in students: 
    # Add each student subject to the set 
       category.add(student['subject'])
print(f"Subjects offered: {category}")

#create an empty list to stores the name of students scoring above 75
top_scorer =[]
for student in students: 
    if student['score'] > 75:
    #appened the student's name only if they score above 75 
     top_scorer.append(student['name'])
print(f"High Scorers: {top_scorer}")
        
        
        




    
   
