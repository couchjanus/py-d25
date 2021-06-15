choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')

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


fields = ("name", "phone", "address", "note", "date")

def addContact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    return contact

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
            print(contacts)
        elif choice == 2:
            contacts.append(addContact())
            print(contacts)
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
