to_do_items = {}

def to_do_list():

    while True:
        # Main menu items
        print("\nChoose or enter a to do list item you'd like to complete:")
        print("\n1. View items")
        print("\n2. Add item")
        print("\n3. Remove item")
        print("\n4. Exit the app")
        answer = input("\nPlease enter your choice: ")
    
        # User response options
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
                if position in to_do_items:
                    to_do_items[position].append(add_item)
                else:
                    to_do_items[value] = add_item
            except ValueError:
                print("You must enter a number!")
            print(f"You added {add_item} to position {position}, now do that task!")
            continue

        elif answer == "3":
            print("What task would you like to remove? Please enter position only!")
            remove_item = input("")
            removed_item = to_do_items.pop(remove_item, None)
            if remove_item is not None:
                print(f"Removed {position, add_item} from your to do list! Good job!")
            else:
                print(f"That item {position, add_item} is not in your list!")

        elif answer == "4":
            print("Are you sure you would like to quit?")

        else:
            print(f"I'm sorry, {answer} is not an option. Please select an option from the list.")

        
to_do_list()