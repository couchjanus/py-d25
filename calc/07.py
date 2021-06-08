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

print(0 <= a < 10 and 0 <= b < 10)
print(a < b and b < 10 or b >= 1)

if b != 0:
    print("a / b = ", a / b)

print("a + b = ", a + b)