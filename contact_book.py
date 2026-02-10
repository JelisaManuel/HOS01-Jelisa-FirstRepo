# Contact Book Application
# This program allows users to manage a contact book by adding, removing, searching, and listing contacts.

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return contacts
# Example usage
def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"{name} was removed.")
    else:
        print(f"{name} not found.")
    return contacts
def search_contact(contacts, name):
    return contacts.get(name, f"{name} not found.")
def list_contacts(contacts):
    return contacts