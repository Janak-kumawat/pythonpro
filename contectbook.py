contacts = {}

def show_menu():
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added successfuly !")

    elif choice == '2':
        for name, info in contacts.items():
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(contacts[search_name])
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print("Contact updated successfuly !")
        else:
            print("Contact not found!")

    elif choice == '5':
        name = input("Enter name to delet: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfuly !")
        else:
            print("Contact not found!")

    elif choice == '6':
        print("TaTa!!")
        break

    else:
        print("Invalid choice!")


