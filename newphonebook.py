from sys import exit

phonebook = {"MATT": "555-555-5555", "JERI":"444-444-4444"}

def phoneapp():
    running = "N"
    print """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
    option = raw_input("What do you want to do (1 -5)? ")
    while running == "N":
        if option == "1":
            optionOne()



    running = str.upper(raw_input("Are you finished using Phonebook (Y or N)? "))
    print "Bye."

def optionOne():
    search = str.upper(raw_input("Who are you searching for? "))
    print "%s's number is" % search, phonebook.get(search, "Sorry, I couldn't find that name.")

def optionTwo():
    name = str.upper(raw_input("What's your name? "))
    phone = str(raw_input("What's your number (xxx-xxx-xxx)? "))
    phonebook[name] = phone
    print "Entry created for %s." % name

def optionThree():
    destroy = str.upper(raw_input("Who would you like to delete? "))
    del phonebook[destroy]
    print "%s's entry has been destroyed" % destroy

def optionFour():
    for key, value in phonebook.items():
        print "Found a listing for %s : %s" % (key, value)

def optionFive():
    print "Bye."
    exit(0)


phoneapp()
