a=str(input())
if len(a)<8:
    print("minimum of 8 charters is needed")
elif len(a)>8:
    print("Your password is valid!")
    print("please enter your password again below")
password=input()
if a==password:
    print("password confirmed")
else:
    print("please enter the same password as before")