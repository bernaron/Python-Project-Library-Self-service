my_dict = {'user_1': 'Password_1', 'user_2': 'Password_2', 'user_3': 'Password_3', 'user_4': 'Password_4'}
order_list = []

while True:
    print("Welcome to Fizzville Library")
    print("MENU")
    print('1. Login \n2. Register \n3. Quit')
    choice = input("How can we help you today?: ")

    if choice == '1':
        username = input('Username: ')
        if username in my_dict.keys():
            userpassword = input("Enter your password: ")
            if my_dict[username] == userpassword:
                print(f"Welcome {username}!")
                book_list = (
                    "1. Jane Austen - Pride and Prejudice - Prose \n"
                    "2. William Shakespeare - Macbeth - Drama \n"
                    "3. William Shakespeare - Othello - Drama \n"
                    "4. Thomas Hardy - Jude the Obscure - Prose \n"
                    "5. Christina Rossetti - Goblin Market - Poetry \n"
                    "6. William Blake - The Tyger - Poetry \n"
                    "7. Christopher Marlowe - Doctor Faustus - Drama \n"
                    "8. Charles Dickens - Great Expectations - Prose \n"
                    "9. Charlotte Bronte - Jane Eyre - Prose \n"
                    "10. George Elliot - The Mill on the Floss - Prose"
                )
                print("BOOK LIST:")
                print(book_list)
                print("MENU")
                print("1. Order Books \n2. Return Book(s) \n3. Quit")

                task = input("What do you want to do today?: ")

                if task == '1':
                    Order = input('Make your order: ')
                    order_list.append(Order)
                    print(f"You have ordered: {Order}")
                    print("Proceeding to checkout...")

                elif task == '2':
                    Return_Book = input("Enter book(s) to return: ")
                    print(f"{Return_Book} now returned.")

                elif task == '3':
                    print("Goodbye!")
                    break  # Exit the program

                else:
                    print("Choice not available, please choose a valid option.")
            else:
                print("Incorrect password.")
        else:
            print("Username does not exist.")

    elif choice == '2':
        print("REGISTER")
        new_user = input("Enter your new username: ")
        if new_user in my_dict.keys():
            print("Username already exists. Choose another username.")
        else:
            new_password = input("Enter your new password: ")
            my_dict[new_user] = new_password
            print(f"User {new_user} registered successfully!")
            print(f"Updated user database: {my_dict}")

    elif choice == '3':
        print("Goodbye!")
        break  # Exit the program

    else:
        print("Invalid choice, please select 1, 2, or 3.")
