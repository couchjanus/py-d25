
# Как проверить, существует ли элемент в списке?
# За проверку вхождения значения в список отвечает оператор in.

choices = ['', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit'] 

print('Delete contact' in choices) # True
print('Delete' in choices) # False

# Как узнать длину списка в Python?
# Функция len(), позволяет получить одномерную длину списка.

print(len([])) # 0
print(len(choices)) # 6

# len() также работает со строками, словарями и другими структурами данных, схожими со списками.
print(len('All contacts'))
# Обратите внимание, что len() — это встроенная функция, а не метод списка.
# Производительность функции len() равна O(1) (константная), то есть скорость получения длины списка не зависит от его длины.

# Как получить значение списка по индексу?
# У каждого элемента списка есть свой уникальный номер. Этот номер называется индексом. Списки в Python имеют нулевую индексацию,  означает, что первый элемент списка имеет индекс 0, второй элемент — индекс 1, третий — 2 и т. д.

print(choices[0]) 
print(choices[2]) 

# Если запросить элемент по индексу за пределами списка, Python выкинет исключение IndexError.
# print(choices[9])  # IndexError: list index out of range

# Отрицательные индексы интерпретируются как подсчёт с конца списка.
print(choices[-2]) 
print(choices[-1]) 

# То же действие можно воспроизвести следующим образом:
print(len(choices)-1) 

# Как перебрать значения списка в Python?
# Python позволяет использовать цикла for со списками:

for item in choices:
    print(item)

# Индекс текущего элемента в цикле можно получить используя функцию enumerate:
for (index, item) in enumerate(choices):
    print('The item in position {} is: {}'.format(index, item))

# Так же, можно проходить по списку используя функцию range. Range генерирует ряд чисел в рамках заданного диапазона, соответственно началом диапазона является число 0 (индекс первого элемента), а концом индекс последнего элемента. Len возвращает длину списка, так как индекс первого элемента является нулем, вычитать из длины списка единицу не нужно, индекс последнего элемента будет соответствовать длине списка:

for i in range(0, len(choices)):
    print(choices[i])


# Define a welcome function

def welcome():
    prompt = """
    Welcome to PhoneBook.
        At hand:\n"""

    for (index, item) in enumerate(choices):
        if index == 0: continue 
        prompt += f'{" "*8} {index}. {item}\n'

    print(prompt + f"{' '*8} Your choice(1,2,3,4,5 0r 6): ")

    return input("""Welcome to PhoneBook.  
                    At hand:
                    1. All contacts
                    2. New contact
                    3. Show contact
                    4. Edit contact
                    5. Delete contact
                    6. Exit
                    Your choice(1,2,3,4,5 0r 6):  """)

# Define a main function
def main():
    # List of contacts 
    contacts = []
    
    while True:
        choice = welcome()
        
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
