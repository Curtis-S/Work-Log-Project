import load_write_functions
import os

print("hello welcome to work log recorder script")
while True:
    first_response = input("please choose one of the options\n"
                           "1. Add new entry.\n"
                           "2. Search entry.\n"
                           "3. Quit\n")
    if first_response == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            add_entry_ob = load_write_functions.FileWriter()
            try:
                add_entry_ob.write_entry_append(input("enter task name: "),
                                                int(input(
                                                    "enter minutes spent"
                                                    "(numbers only "
                                                    "please): ")),
                                                input(
                                                    "enter additional"
                                                    " notes: ")
                                                , input("enter"
                                                        " date in "
                                                        "dd/mm/yyyy "
                                                        "format: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            except ValueError:
                print(
                    "please enter numbers for minutes"
                    " spent,a date in the"
                    "dd/mm/yyyy format\nand additional notes to continue")
    elif first_response == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        search_ob = load_write_functions.DataSearch()
        while True:
            second_response = input("please choose a way to search\n"
                                    "1. by name.\n"
                                    "2. by date.\n"
                                    "3. by minutes \n"
                                    "4. by regex\n"
                                    "5. previous menu\n")
            if second_response == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                name_list = search_ob.find_by_name(
                    input("enter name of task: "))
                for index, entries in enumerate(name_list):
                    print("             {} out of {}\n"
                          "task: {}\n"
                          "time spent: {} minutes\n"
                          "notes: {}\n"
                          "date {}\n".format(index + 1,
                                             len(name_list),
                                             entries.get("task"),
                                             entries.get("time_spent"),
                                             entries.get("notes"),
                                             entries.get("date")))
                    third_response = input(
                        "type e to escape any key to see next entry (if any"
                        ")")
                    if third_response.lower() == "e":
                        break
                    os.system('cls' if os.name == 'nt' else 'clear')

            if second_response == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    try:
                        date_list = search_ob.find_by_date(
                            input("enter a date to "
                                  "search (dd/mm/yyyy"
                                  "format.): "))
                        for index, entries in enumerate(date_list):
                            print("             {} out of {}\n"
                                  "task: {}\n"
                                  "time spent: {} minutes\n"
                                  "notes: {}\n"
                                  "date {}\n".format(index + 1,
                                                     len(date_list),
                                                     entries.get("task"),
                                                     entries.get("time_spent"),
                                                     entries.get("notes"),
                                                     entries.get("date")))
                            third_response = input(
                                "type e to escape any key to"
                                " see next entry (if any"
                                ")")
                            if third_response.lower() == "e":
                                break
                            os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    except ValueError:
                        print(
                            "please enter a valid date dd/mm/yyyy format")

            if second_response == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    try:
                        time_list = search_ob.find_by_time_spent(
                            input("enter how much"
                                  " minutes to "
                                  "the"
                                  " task took: "))
                        for index, entries in enumerate(time_list):
                            print("             {} out of {}\n"
                                  "task: {}\n"
                                  "time spent: {} minutes\n"
                                  "notes: {}\n"
                                  "date {}\n".format(index + 1,
                                                     len(time_list),
                                                     entries.get("task"),
                                                     entries.get("time_spent"),
                                                     entries.get("notes"),
                                                     entries.get("date")))
                            third_response = input(
                                "type e to escape any key to "
                                "see next entry (if any"
                                ")\n")
                            if third_response.lower() == "e":
                                break
                            os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    except ValueError:
                        print(
                            "please enter a whole number eg. '600' ")

            if second_response == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    try:
                        regex_match_list = search_ob.find_by_regex(
                            input("enter regex "
                                  "pattern: "))
                        for index, entries in enumerate(regex_match_list):
                            print("             {} out of {}\n"
                                  "task: {}\n"
                                  "time spent: {} minutes\n"
                                  "notes: {}\n"
                                  "date {}\n".format(index + 1,
                                                     len(regex_match_list),
                                                     entries.get("task"),
                                                     entries.get("time_spent"),
                                                     entries.get("notes"),
                                                     entries.get("date")))
                            third_response = input(
                                "type e to escape any key to "
                                "see next entry (if any"
                                ")")
                            if third_response.lower() == "e":
                                break
                            os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    except ValueError:
                        print(
                            "please enter a valid  regex pattern\n\n")

            if second_response == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    elif first_response == "3":
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("please choose a option from the list\n")
