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

def findContact(contacts, name):
    for item in contacts:
        # if item['name'] == name:
        #     return item
        if item['name'].lower() == name.lower():
            return item

    return None

def updateContact(contact):
    for key in contact:
        value = input(f'Enter {key}: ') or contact[key]
        contact[key] = value
    contact['created'] = datetime.today().strftime("%Y-%m-%d")
    contact.update()

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
            name = input(f'Enter Name for serach please: ')
            result = findContact(contacts, name)
            if result:
                for item in result.items(): print(item)
            else: print('Nothing found')

        # Edit contact
        elif choice == 4:
            name = input(f'Enter Name for edit please: ')
            result = findContact(contacts, name)
            if result:
                index = contacts.index(result)
                updateContact(contacts[index])
                print(contacts)
            else: print('Nothing found for edit')
        # Delet contact
        elif choice == 5:
            name = input(f'Enter Name for remove please: ')
            result = findContact(contacts, name)
            if result:
                index = contacts.index(result)
                contacts.remove(contacts[index])
                print(contacts)
            else: print('Nothing found')
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
