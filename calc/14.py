STR_TITLE = "Smart Calculator"

running = True

def hello():
    print("It’s me, ", STR_TITLE)
    print("I Know Kung Fu")
    
    h = input("Can I help You? ('y', 'n'): ")
    return h

# define functions
def add(x, y):
    """This function adds two numbers"""

    return x + y

def div(x, y, o):
    """This function divs two numbers"""
    if o == "//":
        return x // y
    elif o == "%":
        return x % y
    elif o == "/":
        return x / y

def menu():
    print ("""
        Select operation:
            'h'                        Display this usage message
            '+'                        Addition
            '-'                        Subtraction
            '*'                        Multiplication
            '/'                        Division
            '%'                        Modulus
            '//'                       Division without the remainder
            '**'                       Exponential
            'q'                        Quit
        """)
    return input("Your choice(+|-|*|/|%|//|**|q):")

while True:
    
    if hello() == 'n':
        print('Thank You for using ' + STR_TITLE + '!')
        break # это останавливает цикл while
    else:
        o = menu()

        if o == 'q':
            print('Thank You for using ' + STR_TITLE + '!')
            break # это останавливает цикл while
        else:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("a: ", a)
            print("b: ", b)

            if o == '+':
                print("a + b = ", add(a, b))
            elif o == '-':
                print("a - b = ", a - b)
            elif o == '*':
                print("a * b = ", a * b)
            elif (o == "/" or o == "//" or o == "%"):
                if b!=0:
                    print("a " + o + " b = ", div(a, b, o))
                else:
                    print("Oops, division by zero")
            else:
                if o == '':
                    print("Oops, not operation yet")
                else:
                    print("I don't know what You want")
