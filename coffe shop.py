while True: 
    print("WELCOME TO SOLOMON COFFE SHOP".center(80))
    print()
    a = input("How would u like ur coffe dark or light:")
    b = input("hot or cold:")
    c = int(input('how many u need'))
    b = b.lower()
    a = a.lower()
    hot = 3.0
    cold = 2.0
    if a == "dark" or 'dark coffe':
        if b == 'cold' or 'cold coffe':
            print('great your total for',c,'dark cold coffe is:' + str((cold+(cold*10/100//1))*c) + '$')
        else:
            print('Great your total is:',c,'dark hot coffe is:' + str((hot+(hot*10/100//1))*c) + '$')
    else:
        if b == 'hot' or 'hot coffe':
            print('Great your total is:' + str((hot-(hot*10/100//1))*c) + '$')
        else:
            print('great your total is:' + str((cold+(cold*10/100//1))*c) + '$')

    
