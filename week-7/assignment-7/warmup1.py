# Warmup 1 : Read a Text File Line by Line
with open('../data/notes.txt','r') as f:
    counter = 0
    for line in f:
        counter +=1
        print(f"Line {counter}: {line.strip()}")