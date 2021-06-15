# Define a welcome function

def welcome():
    
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

