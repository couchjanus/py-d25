from datetime import datetime, date, time

choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')
fields = ("name", "phone", "address", "note")

# Initialize dictionary with None values
contact = dict()
print(contact)

# d_items = contacts.items()
# print(d_items) # Here d_items is a view of items

contact["name"] = 'items name'
contact["phone"] = '1234567'
contact["address"] = 'items address'
contact["note"] = 'items note'

# итерировать словарь, используя объект представления, возвращаемый .items():

for item in contact.items():
   print(item)


contact.update({"phone": '5555555555', "address": 'Anorhe items address'})
# Цикл по значениям

for val in contact.values():
   print(val)

def del_elem(id):
   del contact[id] # remove nums[id]

del_elem("note")

for item in contact.items():
   print(item)

def remove_elem(id):
   # проверка наличия ключа
   if id in contact:
       del contact[id]

def pop_elem(id):
   # проверка наличия ключа
   if id in contact:
       return contact.pop(id)

remove_elem = pop_elem("address")
print(remove_elem)

for item in contact.items():
   print(item)

contact.clear()
print(contact)


# Dick of contacts 
# Add Item to Dictionary

# Python List of Dictionaries
# In Python, you can have a List of Dictionaries. 
# You already know that elements of the Python List could be objects of any type.
# Create a List of Dictionaries in Python

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

print(contacts)
# Each element of the list is a dictionary.

# Access key:value pairs in List of Dictionaries
# Access key:value pairs in List of Dictionaries
# Dictionary is like any element in a list. Therefore, you can access each dictionary of the list using index.

print(contacts[0])
print(contacts[0]['name'])

print(contacts[1])
print(contacts[1]['phone'])

print(contacts[2])
print(contacts[2]['address'])

# Update key:value pairs of a Dictionary in List of Dictionaries

#update value for 'bar' in first dictionary
contacts[0]['phone'] = '01010011'

#add a new key:value pair to second dictionary
contacts[1]['name'] = 'Mary Ann'

#delete a key:value pair from third dictionary
del contacts[2]['address']

print(contacts)

# Append a Dictionary to List of Dictionaries

#append dictionary to list
contacts.append({'name':'Jhon', 'phone':'4444444'})

print(contacts)

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

def addContact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
        
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    return contact

def findContact():
    name = input(f'Enter {fields[0]} for serach: ')
    for item in contacts:
        if name in item:
            return item
        else: return None

def editContact(i):
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    contacts[i] = contact

# Define a main function
def main():
    
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
            contacts.append(addContact())
            print(contacts)
        # SHow item
        elif choice == 3:
            res = findContact()
            contact = res if res else 'Nothing found'
            for item in contact.items():
                print(item)

            # print(contact)
        # Edit contact
        elif choice == 4:
            res = findContact()
            index = contacts.index(res)
            editContact(index)
            print(contacts)
        # Delet contact
        elif choice == 5:
            res = findContact()
            index = contacts.index(res)
            print(index)
            print(contacts[index]) 
            del contacts[index]
            print(contacts)
        # Quit script
        elif choice == 6:
            print('Thanks for using FoneBook')
            break
        else:
            print('Incorrect Chice!')

main()
