def input_error(func):
    """Validator on exceptions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "There is no requested contact."
        except IndexError:
            return "Use get <name>."

    return inner

def parse_input(user_input):
    """Function parses input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts: dict):
    """Function create new contact."""
    name, phone = args
    if name in contacts:
        return "Contact already exists. Use change to update contact."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
    """Function changes existing contact."""
    name, phone = args
    # If there is no contact raise exception
    test_on_exists = contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_contact(args, contacts: dict):
    """Function get existing contact."""
    name = args
    return contacts[name]

def show_contacts(contacts):
    """Function returns all contacts."""
    if len(contacts) == 0:
        return "Contact list is empty. Use add <name> <phone>."
    return contacts