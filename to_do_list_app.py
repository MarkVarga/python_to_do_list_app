
data = []

def show_menu():
    print('Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

def add_items():
    item = input('What do you need to do? ')
    data.append(item)
    print('You have added: ', item)
    add_more_items()
    
def add_more_items():    
    user_choice = input('Do you want to add anything else? Press Y/N: ')
    if user_choice.lower() == 'y':
        add_items()
    elif user_choice.lower() =='n':
        app_on()
    elif user_choice.lower() != 'y' or user_choice.lower() != 'n':
        print('Invalid choice')
        add_more_items()
            

def remove_items():
    item = input('What have you completed? ')
    if item in data:
        data.remove(item)
        print(item, 'has been removed from your list')
        remove_more_items()
    else:
        print('This item does not exist')
        app_on()    

def remove_more_items():        
    user_choice = input('Do you want to remove anything else? Press Y/N: ')
    if user_choice.lower() == 'y':
        remove_items()
    elif user_choice.lower() =='n':
        app_on()
    else:
        print('Invalid choice')
        remove_more_items()

def show_items():
    print('Here is your to-do-list: ')
    for item in data:
        print(item)
    app_on()

def exit_app():
    print('Thanks for using the app! See you later!')




def app_on():
    show_menu()
    user_input = input('Enter your choice: ')
    print('You entered:', user_input)

    if user_input == '1':
        add_items()
        
    elif user_input == '2':
        remove_items()
            
    elif user_input == '3':
        show_items()

    elif user_input == '4':
        exit_app()
    else:
        print('Invalid choice. Please enter 1, 2, 3 or 4')
        app_on()

app_on()