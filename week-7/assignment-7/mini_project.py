import os 
import csv
from datetime import datetime 

path = os.path.join('..','data','expenses.csv')
if not os.path.exists(path):
    print("expenses.csv doesn't exist")
else:
    with open(path, 'r') as f:
       reader = csv.DictReader(f)
       expenses =list(reader)
      
   
  
    for row in expenses:
       row['amount'] = float(row['amount'])
   
    
    food_expenses = [row for row in expenses if row['category']== "Food"]
    
       
    total= sum(row['amount'] for row in food_expenses)
    print(f"Total Food expenses: ${total:.2f}")
    
    
report = 'food_report.txt'
with open(report, 'w') as f:
    f.write(f"Food Expense Report — generated {datetime.now().strftime('%B %d, %Y')}\n")
    
    for row in food_expenses:
        f.write(f"{row['date']}: ${row['amount']:.2f}\n")

    f.write(f"Total:      ${total:.2f}")
    
    
#Optional Task: Write the transport report to a file    
transport_expenses =[row for row in expenses if row['category']== "Transport"]
total_transport = sum (row['amount'] for row in transport_expenses)


report_2= 'transport_report.txt'
with open(report_2, 'w') as f:
    f.write(f"Transport expense Report - generated {datetime.now().strftime('%B %d, %Y')}\n")
    for row in transport_expenses:
        f.write(f"{row['date']}: ${row['amount']:.2f}\n")
    f.write(f"Total:      ${total_transport:.2f}")