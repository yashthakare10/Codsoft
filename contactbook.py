import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def display_menu():
    print("\nContact Management System:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print("{} - {}".format(name, details['phone']))

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").lower()
    matching_contacts = {name: details for name, details in contacts.items()
                         if query in name.lower() or query in details['phone']}
    
    if not matching_contacts:
        print("No matching contacts found.")
    else:
        view_contacts(matching_contacts)

def update_contact(contacts):
    view_contacts(contacts)
    name = input("Enter the name to update: ")
    
    if name in contacts:
        updated_phone = input("Enter the updated phone number (leave blank to keep current): ")
        updated_email = input("Enter the updated email address (leave blank to keep current): ")
        updated_address = input("Enter the updated address (leave blank to keep current): ")

        if updated_phone:
            contacts[name]['phone'] = updated_phone
        if updated_email:
            contacts[name]['email'] = updated_email
        if updated_address:
            contacts[name]['address'] = updated_address

        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    view_contacts(contacts)
    name = input("Enter the name to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact '{}' deleted.".format(name))

    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
