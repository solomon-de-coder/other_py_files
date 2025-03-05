#Program to check odd or even and put them in seperate list 
odd = []
eve = []
a = eval(input("Enter the numbers seperated with commas"))
a = list(a)
for i in a:
    if i%2 == 0:
        eve.append(i)
    else:
        odd.append(i)
print("even numbers:", eve) 
print("odd numbers:", odd)