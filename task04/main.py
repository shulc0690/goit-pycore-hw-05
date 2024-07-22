from utils import parse_input, add_contact, show_contacts, change_contact, get_contact

def main():
    """Start program."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "get":
            print(get_contact(args, contacts))
        else:
            print("Invalid command. Use add/change/all <name> <phone>.")

if __name__ == "__main__":
    main()