# display.py
# This module contains functions for displaying messages and contacts in a contact management system.
def display_messsage(message):
    print(message)
    # Example usage
def display_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")