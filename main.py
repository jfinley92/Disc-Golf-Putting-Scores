import json
import sys


def main_menu():
    # Welcomes the player and gives options to which screen to go to
    print("Welcome to Perfect Putt! Please select an option below.")
    print("1. Play")
    print("2. Create Profile")
    print("3. Delete Profile")
    print("4. Delete Previous Round")
    print("5. Statistics")
    print("6. Help")
    print("7. Exit\n")
    option = input("")
    while True:
        if option == '1':
            play()
        elif option == '2':
            create_profile()
        elif option == '3':
            delete_profile()
        elif option == '4':
            delete_round()
        elif option == '5':
            statistics()
        elif option == '6':
            help_screen()
        elif option == '7':
            end()
        else:
            print("\n")
            main_menu()


def play():
    # Prompts the user to choose a profile and then enter in how many shots they made
    with open('data.txt') as json_file:
        data = json.load(json_file)
    name = input("Who is going to be playing?\n")
    if name.lower() in data:
        ten_feet = int(input("How many shots out of 10 did you make from 10 feet?\n"))
        fifteen_feet = int(input("How many shots out of 15 did you make from 10 feet?\n"))
        twenty_feet = int(input("How many shots out of 20 did you make from 10 feet?\n"))
        twenty_five_feet = int(input("How many shots out of 25 did you make from 10 feet?\n"))
        thirty_feet = int(input("How many shots out of 30 did you make from 10 feet?\n"))
        data[name.lower()]['current_round']["10'"] = ten_feet
        data[name.lower()]['current_round']["15'"] = fifteen_feet
        data[name.lower()]['current_round']["20'"] = twenty_feet
        data[name.lower()]['current_round']["25'"] = twenty_five_feet
        data[name.lower()]['current_round']["30'"] = thirty_feet
        data[name.lower()]['total_attempts']["10'"] += 10
        data[name.lower()]['total_attempts']["15'"] += 10
        data[name.lower()]['total_attempts']["20'"] += 10
        data[name.lower()]['total_attempts']["25'"] += 10
        data[name.lower()]['total_attempts']["30'"] += 10
        data[name.lower()]['total_made']["10'"] += ten_feet
        data[name.lower()]['total_made']["15'"] += fifteen_feet
        data[name.lower()]['total_made']["20'"] += twenty_feet
        data[name.lower()]['total_made']["25'"] += twenty_five_feet
        data[name.lower()]['total_made']["30'"] += thirty_feet
        with open('data.txt', 'w+') as outfile:
            json.dump(data, outfile)
        print("\n")
        main_menu()
    else:
        print("That profile name doesn't exist!\n")
        main_menu()


def create_profile():
    # Allows the user to make a profile name
    with open('data.txt') as json_file:
        data = json.load(json_file)
    name = input("What profile name would you like? Enter 'x' for main menu. \n")
    if name == 'x':
        print("\n")
        main_menu()
    elif name.lower() not in data:
        print("Welcome " + name.title() + "! You are all set to start playing.\n")
        data[name.lower()] = {"current_round": {"10'": 0, "15'": 0, "20'": 0, "25'": 0, "30'": 0},
                              "total_attempts": {"10'": 0, "15'": 0, "20'": 0, "25'": 0, "30'": 0},
                              "total_made": {"10'": 0, "15'": 0, "20'": 0, "25'": 0, "30'": 0},
                              }
        with open('data.txt', 'w+') as outfile:
            json.dump(data, outfile)
        print("\n")
        main_menu()

    else:
        print("This name already exists!\n")
        create_profile()


def delete_profile():
    # Allows the user to delete a profile
    with open('data.txt') as json_file:
        data = json.load(json_file)
    name = input("Which profile would you like to delete? \n")
    if name.lower() in data:
        warning = input("Are you sure you want to delete? ('y' or 'n') Your scores will not be saved \n")
        if warning == 'y':
            del data[name.lower()]
            with open('data.txt', 'w+') as outfile:
                json.dump(data, outfile)
            print("We are sorry to see you go!\n")
            main_menu()
        elif warning == 'n':
            print("\n")
            main_menu()
        else:
            print("Please choose either yes ('y') or no ('n').")
            delete_profile()
    else:
        print("That profile name does not exist!\n")
        main_menu()


def delete_round():
    # Allows the user to delete the most recent round
    with open('data.txt') as json_file:
        data = json.load(json_file)
    name = input("Whose previous round would you like to delete?\n")
    if name in data:
        if data[name.lower()]['total_attempts']["10'"] == 0:
            print("There isn't a previous round to delete!\n")
            main_menu()
        else:
            data[name.lower()]['total_attempts']["10'"] -= 10
            data[name.lower()]['total_attempts']["15'"] -= 10
            data[name.lower()]['total_attempts']["20'"] -= 10
            data[name.lower()]['total_attempts']["25'"] -= 10
            data[name.lower()]['total_attempts']["30'"] -= 10
            data[name.lower()]['total_made']["10'"] -= data[name.lower()]['current_round']["10'"]
            data[name.lower()]['total_made']["15'"] -= data[name.lower()]['current_round']["15'"]
            data[name.lower()]['total_made']["20'"] -= data[name.lower()]['current_round']["20'"]
            data[name.lower()]['total_made']["25'"] -= data[name.lower()]['current_round']["25'"]
            data[name.lower()]['total_made']["30'"] -= data[name.lower()]['current_round']["30'"]
            with open('data.txt', 'w+') as outfile:
                json.dump(data, outfile)
            print("\n")
            main_menu()
    else:
        print("This profile name does not exist!\n")
        main_menu()


def statistics():
    # Lets the user look at the overall average for a profile
    with open('data.txt') as json_file:
        data = json.load(json_file)
    name = input("Whose statistics would you like to check? Enter 'x' for main menu. \n")
    if name == 'x':
        print("\n")
        main_menu()
    elif name.lower() not in data:
        print("You need to register this name first!\n")
    elif data[name.lower()]['total_attempts']["10'"] == 0:
        print("Putting Averages")
        print("10 Feet: " + "0.00%")
        print("15 Feet: " + "0.00%")
        print("20 Feet: " + "0.00%")
        print("25 Feet: " + "0.00%")
        print("30 Feet: " + "0.00%")
        print("\n")
    elif name.lower() in data:
        print("Putting Averages")
        print("10 Feet: " + str(round(data[name.lower()]['total_made']["10'"] / data[name.lower()]['total_attempts']["10'"] *
                                100, 1)) + "%")
        print("15 Feet: " + str(round(data[name.lower()]['total_made']["15'"] / data[name.lower()]['total_attempts']["15'"] *
                                100, 1)) + "%")
        print("20 Feet: " + str(round(data[name.lower()]['total_made']["20'"] / data[name.lower()]['total_attempts']["20'"] *
                                100, 1)) + "%")
        print("25 Feet: " + str(round(data[name.lower()]['total_made']["25'"] / data[name.lower()]['total_attempts']["25'"] *
                                100, 1)) + "%")
        print("30 Feet: " + str(round(data[name.lower()]['total_made']["30'"] / data[name.lower()]['total_attempts']["30'"] *
                                100, 1)) + "%\n")
        print("\n")
    else:
        print("That name does not exist!\n")
    main_menu()


def help_screen():
    # Tells the player about the game and the features in the menu
    print("Welcome to Perfect Putt. This program allows you to keep track of "
          "your putting scores. Below are descriptions of the menu options.\n")
    print("1. Play - Choose a profile and enter how many shots out of ten you made \n\t\t  from different distances.")
    print("2. Create Profile - Create a profile so you can play and keep track of\n\t\t\t\t    your scores.")
    print("3. Delete Profile - Delete a profile if you want to start over or no  \n\t\t\t\t    longer want to play.")
    print("4. Delete Round - Here you can delete your most recent round.")
    print("5. Statistics - Check your average at each distance across all rounds.")
    print("6. Help - You are here.")
    print("7. Exit - Exit the program.\n")
    main_menu()


def end():
    # Exits the program
    print("Thanks for playing!")
    sys.exit()


main_menu()
