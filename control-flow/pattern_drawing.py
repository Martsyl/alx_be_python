pattern = int(input("Enter the size of the pattern: "))
rows = 0
while rows < pattern:
    for i in range(pattern):
        print("*", end="")
    print()
    rows += 1   
    
