# Contact Book Application
# This program allows users to manage a contact book by adding, removing, searching, and listing contacts.
from email.mime import message
from contact_book import add_contact, remove_contact, search_contact, list_contacts
from display import display_messsage, display_contacts
# Example usage
# This is the main function that demonstrates the contact book application.
def main():
    contacts = {}
# Add some contacts
    contacts = add_contact(contacts, "John Doe", "123-456-7890")
    contacts = add_contact(contacts, "Jane Doe", "987-654-3210")
# List all contacts
    display_contacts(contacts)
    message = search_contact(contacts, "John Doe")
    display_messsage(message)
# Remove a contact
    contacts = remove_contact(contacts, "John Doe")
    display_contacts(contacts)
if __name__ == "__main__":    
    main()