#Warmup 3: Handle a misiing file
try:
    # Open the .txt file and read its content
    with open("../data/missing.txt", 'r') as f:
        #reads the entire file into a string
        content = f.read()
except FileNotFoundError:
    print("Error: \"missing.txt\" was not found. Please check the file path and try again.")
else:
    #display a content if no error occured
    print(content)    