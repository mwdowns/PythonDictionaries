from sys import exit
import pickle
from os.path import exists

#phonebook = {"MATT": "555-555-5555", "JERI":"444-444-4444"}

def phoneapp():
    running = "N"
    while running == "N":
        entries()
        running = str.upper(raw_input("Are you finished using Phonebook (Y or N)? "))
    print "Bye."


def entries():

    if exists("phonebook.pickle"):
        print "Loading phonebook..."
        myfile = open("phonebook.pickle", "r")
        phonebook = pickle.load(myfile)
    else:
        phonebook = {}

    print """

    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save all entries
    6. Quit
    """

    option = raw_input("What do you want to do (1 -6)? ")
    if option == "1":
        search = str.upper(raw_input("Who are you searching for? "))
        print "%s's number is" % search, phonebook.get(search, "Sorry, I couldn't find that name.")

    elif option == "2":
        name = str.upper(raw_input("What's your name? "))
        phone = str(raw_input("What's your number (xxx-xxx-xxx)? "))
        phonebook[name] = phone
        print "Entry created for %s." % name

    elif option == "3":
        destroy = str.upper(raw_input("Who would you like to delete? "))
        if destroy in phonebook:
            del phonebook[destroy]
            print "%s's entry has been destroyed" % destroy
        else:
            print "%s's name is not in the phonebook" % destroy

    elif option == "4":
        for key, value in phonebook.items():
            print "Found a listing for %s : %s" % (key, value)

    elif option == "5":
        myfile = open("phonebook.pickle", "w")
        pickle.dump(phonebook, myfile)
        myfile.close()
        print "Phonebook saved."

    elif option == "6":
        print "Bye."
        exit(0)

    else:
        print "Ivalid entry."

phoneapp()
