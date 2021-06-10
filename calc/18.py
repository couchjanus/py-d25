STR_TITLE = "Smart Calculator"

running = True

def hello():
    print("{!s:=^40}".format("It’s me, {0}".format(STR_TITLE)))
    print("{!s:=^40}".format("I Know Kung Fu"))
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

def formula():
    return input("Enter expression(2 + 2):")

while True:
    
    if hello() == 'n':
        print('Thank You for using {0} !'.format(STR_TITLE))
        break # это останавливает цикл while
    else:
        s1, o, s2 = formula().split(" ", 3)
        a = float(s1)
        b = float(s2)

        print (f"{a} {o} {b}")

        if o == 'q':
            print('Thank You for using {0} !'.format(STR_TITLE))
            break # это останавливает цикл while
        else:
            if o == '+':
                res =  add(a, b)
            elif o == '-':
                res =  a - b
            elif o == '*':
                res = a * b
            elif (o == "/" or o == "//" or o == "%"):
                if b!=0:
                    res = div(a, b, o)
                else:
                    print("Oops, division by zero")
            else:
                if o == '':
                    print("Oops, not operation yet")
                else:
                    print("I don't know what You want")
            print (f"{a} {o} {b} = {res}")
