from datetime import datetime, date, time

def addContact(contact):
    for key in contact:
        value = input(f'Enter {key}: ')
        contact[key] = value
    contact['created'] = datetime.today().strftime("%Y-%m-%d")
    return contact

# Define a welcome function
def welcome():
    prompt = """
    Welcome to PhoneBook.
        At hand:\n"""
    tip = "Your choice("

    choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Clear contacts', 'Exit')
    for (index, item) in enumerate(choices):
        if index == 0: continue 
        tip += f"{index},"
        prompt += f'{" "*8} {index}. {item}\n'
    return input(prompt + f"{' '*8} {tip[:-1]} 0r q): ")

def init():
    contacts = [
        {
            'name':'Tom',
            'phone':'111111',
            'address': 'Addres 1',
            'note': 'Note 1'
        },
        {
            'name':'Mary',
            'phone':'2222222',
            'address': 'Addres 2',
            'note': 'Note 2'
        },
        {
            'name':'Dic',
            'phone':'3333333',
            'address': 'Addres 3',
            'note': 'Note 3'
        }
    ]
    fields = ("name", "phone", "address", "note")

    # # Initialize dictionary with None values
    contact = dict.fromkeys(fields)
    
    return (contacts, contact)

# Define a main function
def main():

    contacts, contact = init()
    
    while True:
        choice = welcome()
        if choice == 'q': break
        choice = int(choice if choice.isdigit() else 0)

        if choice == 0:
            continue
        # All contacts
        elif choice == 1:
            print(contacts)
        # Add new
        elif choice == 2:
            contacts.append(addContact(contact.copy()))
            print(contacts)
        # SHow item
        elif choice == 3:
            print(contacts)
        # Edit contact
        elif choice == 4:
            print(contacts)
        # Delet contact
        elif choice == 5:
            print(contacts)
        # Clear contacts
        elif choice == 6:
            contacts = []
            print(contacts)
        # Quit script
        elif choice == 7:
            print('Thanks for using FoneBook')
            break
        else:
            print('Incorrect Chice!')

main()
