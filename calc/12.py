str_title = "Smart Calculator"

running = True

def hello():
    print("It’s me, ", str_title)
    print("I Know Kung Fu")
    
    h = input("Can I help You? ('y', 'n'): ")
    return h

def menu():
    print("Select operation:")
    print("Addition: +")
    print("Subtraction: -")
    print("Multiplication: *")
    print("Division: /")
    print("Modulus: %")
    print("Division without the remainder: //")
    print("Exponential: //")
    return input("Your choice(+|-|*|/|%|//|**):")


while running:
    
    if hello() == 'n':
        print('Programm done.')
        running = False # это останавливает цикл while
    else:
        o = menu()
        
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("a: ", a)
        print("b: ", b)
        
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
