to_do_items = {}

# Main menu items



def to_do_list():

    while True:
    
        print("\nChoose or enter a to do list item you'd like to complete:")
        print("\n1. View items")
        print("\n2. Add item")
        print("\n3. Remove item")
        print("\n4. Exit the app")
        answer = input("\nPlease enter your choice: ")

    
        if answer == "1":
            print("Here are your current to do items: ")
            print(f"You have {len(to_do_items)}, they are: {to_do_items}")
            continue

        elif answer == "2":
            print("What task would you like to add?")
            add_item = input("")
            position = input("What position would you like to put it? Please enter numbers only!\n")
            try:
                value = int(position)
                to_do_items[value] = add_item
            except ValueError:
                print("You must enter a number!")
            print(f"You added {add_item} to position {position}, now do that task!")
            continue

        elif answer == "3":
            print("What task would you like to remove?")
            
        elif answer == "4":
            print("Are you sure you would like to quit?")

        else:
            print(f"I'm sorry, {answer} is not an option. Please select an option from the list.")

        
to_do_list()