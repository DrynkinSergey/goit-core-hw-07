from api import (
    Record,
    AddressBook,
    get_upcoming_birthdays,
    greetings,
    help_api,
    command_parser,
    normalize_users_date,
)


def main():
    book = AddressBook()
    exit_commands = ["q", "quit", "exit", "leave", "left"]
    print('Welcome to assistant bot! You can use "help" command to see more')
    new_contact = Record("ivan")
    new_contact.add_phone("123123123")
    new_contact.add_phone("123123123")
    new_contact.add_birthday("10.04.2024")
    book.add_record(new_contact)
    while True:

        params = input(">>>  ")
        # if str is empty - start new loop
        if not params:
            print("Please, enter not empty string! ")
            continue

        # get main command and attributes
        command, *args = command_parser(params)
        if len(args) != 0:
            name = args[0]

        match (command):
            case "hello" | "start":
                print(greetings())

            case "add" | "create":
                if len(args) < 2:
                    print(f'Please enter, correct args. Example: "add Oleh 0932244555"')
                    continue
                new_contact = Record(name)
                exist_record = book.find_record(name)
                if exist_record:
                    exist_record.add_phone(args[1])
                else:
                    new_contact.add_phone(args[1])
                    book.add_record(new_contact)

            case "find" | "get":
                exist = book.find_record(name)
                print(exist)

            case "birthdays" | "b":
                book.birthdays()

            case "show_birthday":
                if len(args) < 1:
                    print(f'Please enter, correct args. Example: "show_birthday Oleh"')
                    continue
                exist_record = book.find_record(name)
                if exist_record:
                    exist_record.show_birthday()
                else:
                    print("User is not exist")

            case "add_birthday":
                if len(args) < 2:
                    print(
                        f'Please enter, correct args. Example: "add_birthday Oleh 22.03.2024"'
                    )
                    continue
                exist_record = book.find_record(name)
                if exist_record:
                    exist_record.add_birthday(args[1])
                else:
                    print("User is not exist")

            case "update":
                if len(args) < 3:
                    print(
                        f'Please enter, correct args. Example: "update Oleh 0932244555 05012345678"'
                    )
                    continue
                exist = book.find_record(name)
                if exist:
                    exist.edit_phone(args[1], args[2])
                else:
                    print(f'User "{name}" is not found')

            case "delete" | "del":
                book.remove(name)

            case "all" | "show":
                book.show()

            case "help" | "info":
                print(help_api())

            # if main command was in exit commands list - exit
            case command if command in exit_commands:
                print("Bye!")
                break
            # if ony attribute is not match
            case _:
                print("Invalid command! Try again...\n")


if __name__ == "__main__":
    main()
