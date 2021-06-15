
# Как проверить, существует ли элемент в tuple?
# За проверку вхождения значения в tuple отвечает оператор in.

choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')

print('Delete contact' in choices) # True
print('Delete' in choices) # False

# Как узнать длину tuple в Python?
# Функция len(), позволяет получить одномерную длину tuple.
print(len(choices)) # 6

# Как получить значение tuple по индексу?
print(choices[0]) 
print(choices[2]) 

# Отрицательные индексы интерпретируются как подсчёт с конца tuple.
print(choices[-2]) 
print(choices[-1]) 

# То же действие можно воспроизвести следующим образом:
print(len(choices)-1) 

# Как перебрать значения tuple в Python?
# Python позволяет использовать цикла for с tuple:

for item in choices:
    print(item)

# Индекс текущего элемента в цикле можно получить используя функцию enumerate:
for (index, item) in enumerate(choices):
    print('The item in position {} is: {}'.format(index, item))

# Так же, можно проходить по tuple используя функцию range.

for i in range(0, len(choices)):
    print(choices[i])


# Define a welcome function

def welcome():
    prompt = """
    Welcome to PhoneBook.
        At hand:\n"""
    tip = "Your choice("

    for (index, item) in enumerate(choices):
        if index == 0: continue 
        tip += f"{index},"
        prompt += f'{" "*8} {index}. {item}\n'
    return input(prompt + f"{' '*8} {tip[:-1]} 0r q): ")

# Define a main function
def main():
    # List of contacts 
    contacts = []
    
    while True:
        choice = welcome()
        if choice == 'q': break
        choice = int(choice if choice.isdigit() else 0)

        if choice == 0:
            continue
        elif choice == 1:
            print(choice)
        elif choice == 2:
            print(choice)
        elif choice == 3:
            print(choice)
        elif choice == 4:
            print(choice)            
        elif choice == 5:
            print(choice)  
        elif choice == 6:
            print('Thanks for using FoneBook')
            break
        else:
            print('Incorrect Chice!')

main()
