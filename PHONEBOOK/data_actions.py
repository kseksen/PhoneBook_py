contact_data = {
    'first_name': None, 
    'second_name': None, 
    'pat_name': None, 
    'phone_number': None,
    }

def get_data():
    surname = input("Insert surname: ")
    f_name = input("Insert name: ")
    pt_name = input("Insert paternal name: ")
    phone = input("Insert phone number: ")
    contact = {'second_name': surname,
               'first_name': f_name,
               'pat_name': pt_name,
               'phone_number': phone}
    return contact

def add_new_contact():
    contact = get_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value + ';')
        file.write('\n')
    return True

def open_phonebook():
    title = ["Surname:", "Forname:", "Paternal Name:", "Phone Number:"]
    print('--'*50)
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        print('--'*50)
        for line in file:
            print("\t\t".join(line.split(";")))
            

def find_contact():
    search_type = input(f"Choose search type:\n1. Surname.\n2. Forename.\n3. Paternal Name.\n4. Phone Number.")
    search_query = input("Insert search query: ")
    title = ["Surname: ", "Forename: ", "Paternal Name: ", "Phone Number: "]
    contacts = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            contact_info = line.strip().split(';')
            if len(contact_info) < 4:
                continue
            if search_type == "1" and search_query.lower() in contact_info[0].lower():
                contacts.append(contact_info)
                print("\t\t".join(contact_info))
            elif search_type == "2" and search_query.lower() in contact_info[1].lower():
                contacts.append(contact_info)
                print("\t\t".join(contact_info))
            elif search_type == "3" and search_query.lower() in contact_info[2].lower():
                contacts.append(contact_info)
                print("\t\t".join(contact_info))
            elif search_type == "4" and search_query.lower() in contact_info[3].lower():
                contacts.append(contact_info)
                print("\t\t".join(contact_info))
    return contacts

def copy_contact():
    contacts_to_copy = find_contact()
    if not contacts_to_copy:
        print("Contact not found.")
        return
    copy_to_file = input("Enter the filename to copy contacts to: ")
    with open(copy_to_file + '.txt', 'a', encoding='utf-8') as file:
        for contacts in contacts_to_copy:
            file.write(';'.join(contacts) + '\n')
    print("Contacts copied successfully.")

def main():
    while True: 
        print("Choose one of the options:")
        print("1. Find contact")
        print("2. Add new contact")
        print("3. Open phonebook")
        print("4. Copy contact")
        print("5. Exit")
        menu_selection = int(input("-> "))
        if menu_selection == 1:
            find_contact()
        elif menu_selection == 2:
            add_new_contact()
        elif menu_selection == 3:
            open_phonebook()
        elif menu_selection == 4:
            copy_contact()
        elif menu_selection == 5:
            break
        input("Press <Enter> to continue")

if __name__ == "__main__":
    main()
