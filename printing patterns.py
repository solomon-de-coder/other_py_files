'''a=int(input("enter your number:"))
b=str(input(" enter what you want to replicate:"))
for i in range(1,a+1):
    print(b*i)'''
while True:
    b=input("what you want to print:")
    a = int(input())
    for i in range(a + 1, 0, -1):
        for j in range(i):
            print(b , end="")
        print()
