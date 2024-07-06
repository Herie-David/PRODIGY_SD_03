import json

# Loads contacts from a JSON file (if it exists)
def load_contacts():
  try:
    with open("contacts.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    # No file found, return an empty list
    return []

def save_contacts(contacts):
# Saves contacts to a JSON file
  with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=4)  # Save with indentation for readability

def get_user_input(prompt):
  # Prompts the user for input and validates it (not empty)
  while True:
    value = input(prompt).strip()
    if value:
      return value
    else:
      print("Invalid input. Please enter a value.")

def add_contact():
  # Prompts user for details and adds a new contact
  name = get_user_input("Enter contact name: ")
  phone_number = get_user_input("Enter phone number: ")
  email = input("Enter email address (optional): ").strip()
  contact = {"name": name, "phone": phone_number, "email": email}
  contacts.append(contact)
  save_contacts(contacts)
  print("Contact added successfully!")

def view_contacts():
  # Displays the list of contacts
  if not contacts:
    print("There are no contacts to display.")
    return
  print("-" * 40)
  print("| {:20s} | {:20s} | {:30s} |".format("Name", "Phone Number", "Email"))
  print("-" * 40)
  for contact in contacts:
    print("| {:20s} | {:20s} | {:30s} |".format(contact["name"], contact["phone"], contact["email"]))
  print("-" * 40)

def edit_contact():
  # Allows editing an existing contact
  if not contacts:
    print("There are no contacts to edit.")
    return
  view_contacts()  # Display contacts for reference
  while True:
    try:
      index = int(input("Enter the index of the contact to edit (starting from 0): "))
      if index < 0 or index >= len(contacts):
        print("Invalid index.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  contact = contacts[index]
  name = get_user_input(f"Update name (press Enter to keep existing - {contact['name']}): ") or contact["name"]
  phone_number = get_user_input(f"Update phone number (press Enter to keep existing - {contact['phone']}): ") or contact["phone"]
  email = input(f"Update email address (press Enter to keep existing - {contact['email']}): ").strip() or contact["email"]
  contacts[index] = {"name": name, "phone": phone_number, "email": email}
  save_contacts(contacts)
  print("Contact updated successfully!")

def delete_contact():
  # Allows deleting an existing contact
  if not contacts:
    print("There are no contacts to delete.")
    return
  view_contacts()  # Display contacts for reference
  while True:
    try:
      index = int(input("Enter the index of the contact to delete (starting from 0): "))
      if index < 0 or index >= len(contacts):
        print("Invalid index.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  del contacts[index]
  save_contacts(contacts)
  print("Contact deleted successfully!")

def main_menu():
  # Displays the main menu with options
  print("\nContact Management System")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Edit Contact")
  print("4. Delete Contact")
  print("5. Exit")
  choice = input("Enter your choice (1-5): ")
  return choice

# Load contacts from file on startup
contacts = load_contacts()

while True:
  # Main program loop that keeps presenting the menu and handling user choices
  choice = main_menu()
  if choice == "1":
    add_contact()
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    edit_contact()
  elif choice == "4":
    delete_contact()
  elif choice == "5":
    print("Exiting Contact Management System...")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")