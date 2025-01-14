# Get input from the user
a = input("Enter items in the format [item1, item2, ...]: ")

# Clean and split the input
items = a.strip('[]').split(',')

# Initialize lists
even = []
odd = []
strings = []

# Process each item
for i in items:
    i = i.strip()  # Remove any extra spaces
    if i.isdigit():  # Check if the item is a number
        n = int(i) 
        (even if n % 2 == 0 else odd).append(n)
    else:
        strings.append(i)

# Output results
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Strings:", strings)
