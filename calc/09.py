str_title = "Smart Calculator"
print("It’s me, ", str_title)

# a = b = 2
# I Know Kung Fu.
print("I Know Kung Fu")

# Чтобы преобразовать строку из цифр в целое число, воспользуемся функцией int(). Например, int('23') вернет число 23.
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
