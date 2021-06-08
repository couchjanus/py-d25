str_title = "Smart Calculator"

running = True

while running:
    print("It’s me, ", str_title)
    # I Know Kung Fu.
    print("I Know Kung Fu")
    
    h = input("Can I help You? ('y', 'n'): ")
    
    if h == 'n':
        print('Programm done.')
        running = False # это останавливает цикл while
    else:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("a: ", a)
        print("b: ", b)
        o = input("Enter operation: ")
        if o == '+':
            print("a + b = ", a + b)
        elif o == '-':
            print("a - b = ", a - b)
        elif o == '*':
            print("a * b = ", a * b)
        elif o == '/':
            if b != 0:
                print("a / b = ", a / b)
            else:
                print("Oops, division by zero")
        else:
            if o == '':
                print("Oops, not operation yet")
            else:
                print("I don't know what You want")
