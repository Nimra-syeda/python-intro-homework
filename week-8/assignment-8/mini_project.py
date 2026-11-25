# Mini Project - Defensive CSV Reader
import os
import csv

#join the file path
path = os.path.join('..','data','messy_data.csv')
try:
    # Open the file  and read 
    with open(path,'r') as f:
        """Read the CSV file and convert each row into a dictionary, 
         with the column names from the first row serving as the keys."""
        reader= csv.DictReader(f)
        #convert the reader into list
        rows = list(reader)        
except FileNotFoundError:
    print("Error: \"messy_data.csv\" was not found. Please check the file path and try again.")
else:
   #create a empty list to collect value error and key error data/row into seperate list.
    skipped_rows = []
    #create a empty list to collect the clean data into list- which has no error  
    clean_data = []
    # Check each row for extra columns. If an extra column is found,
    # record the row number, add it to the skipped rows list, and skip processing that row
    for row_num, row in enumerate(rows, start=1):
        if None in row:
            skipped_rows.append(f"Row {row_num}: extra column detected - skipped.")
            
            continue    
        try:                           
            row['amount'] = float(row['amount'])
            entry={'name':row['name'], 
                'category':row['category'],
                'amount':row['amount']}               
            clean_data.append(entry)
        except ValueError:
          value_error = (f"Row {row_num}: ValueError - could not convert '{row['amount']}' to float.")
          skipped_rows.append(value_error)
        except KeyError :
            key_error =(f"Row {row_num}: Missing expected column.")
            skipped_rows.append(key_error)
        except TypeError:
            skipped_rows.append(
                f"Row {row_num}: amount is missing - skipped.")
    total =len(clean_data)+len(skipped_rows)      
    print("=== CSV Report ===")          
    print(f"Rows attempted: {total}")
    print(f"Row parsed: {len(clean_data)}")   
    print(f"Rows Skipped:{len(skipped_rows)}")   
    print("\nSkipped row:")
    for row in skipped_rows:
        print(f"  {row}")    
    print("\nClean data:")
    for row in clean_data:
        print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")
           

    