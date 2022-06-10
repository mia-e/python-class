# Mia Escoto 
# creating a contact book to store extra details

from datetime import date
from turtle import up


contacts = {
    #Where all contact information will be stored
    'first-name' : [],
    'last-name' :[],
    'address' : [],
    'date_created': [],
    'phone_number': [],
    'email_address': []
}


#make variables for each section
firstName = contacts["first-name"]
lastName = contacts["last-name"]
address = contacts["address"]
day = contacts["date_created"]
phoneNumber = contacts["phone_number"]
email = contacts["email_address"]

sections = ['first name', 'last name', 'address', 'phone number', 'email']



def showMenu():
    #introduce the program and promt the user for an action they would want to execute
    print("\nWelcome to your contact book!\n")
    while True:
        try:
            user_choice = int(input("""Enter the number of the action you would like to complete.\n
        1. Add new contact information
        2. Update contact information
        3. Delete contact information
        4. Display all contact information
        5. Search for a contact
        6. Exit contact book.
        : """))  
            if user_choice not in range(1, 7):
                #If the didn't enter one of the displayed
                print("Please Enter a number 1-\nRe enter form:  ")
                continue
            break
        except ValueError:
            #if they entered something besides a number
            print("Please enter a NUMBER")
    print()
    return user_choice

def getInput(type):
    #get the users input and if they did not enter any, re enter.
    while True:
        user_input = input(f"{type}: ").strip().lower()
        if user_input == "":
            print("You may not leave this field blank.\nre enter.\n")
            continue
        break
    return user_input

def repeated(first, last, phone, _email):
    #Check if any information has been repeated, then displaying the information and promting the user to either update or quit
    for i in range(len(firstName)):
        if (lastName[i] == last and firstName[i] == first) or phoneNumber[i] == phone or email[i] == _email:
            showInfo(i)
            while True:
                print("The information above has already been entered for another contact\n")
                try:
                    choice = int(input("""Would you like to:
                    1. Re enter form
                    2. Update contact
                    3. Quit 
                    Please enter one of the above numbers: """))
                #error checking
                except ValueError: 
                    print("Please enter a number")
                    continue
                if choice not in range(1, 4):
                    print("Please eter a number from above\n1-3\nRe Enter.")
                    continue
                break
            return choice
                    


def checkEmail(email):
    #verifying it could be an email address
    #check if the @ is not the first 
    if "@" not in email or ".com" not in email and ".org" not in email and ".net":
            print("Please enter a valid email address\n")
            return False
    

def getNumber():
    #promting the user for a phone number
    while True:
            try:
                input_phone = int(getInput("Phone Number"))
            except ValueError:
                print("Please enter only numbers")
                continue
            if len(str(input_phone))!= 10:
                print("Phone numbers must have 10 digits.\nRe Enter.") 
                continue
            break
    return input_phone


def addContact():
    #error check for email - .org com etc
    while True:
        #taking user input
        input_first = getInput("First Name")
        input_last = getInput("Last Name")
        input_address = getInput("Home Address")
        input_phone = getNumber()
        while True:
            input_email = getInput("Email")
            if checkEmail(input_email) == False:
                continue
            break
        today = date.today()
        #check if the info is repeated
        repeat = repeated(input_first, input_last, input_phone, input_email) 
        if repeat ==1:
            continue
        elif repeat ==2:
            updateContact()
            break
        elif repeat == 3:
            print("Request canceled")
            break
        #add all info 
        #confirmation?
        while True:
            confirmation = input("Add as contact?\n: ").lower().strip()
            if confirmation == "yes":
                firstName.append(input_first)
                lastName.append(input_last)
                address.append(input_address)
                day.append(today)
                phoneNumber.append(input_phone)
                email.append(input_email)
                print("\ncontact added.")
                break
            elif confirmation == "no":
                print("\n contact not made")
                break
            else:
                print("\nEnter either yes or no.\n")
                continue
        break


def getSection(section):
    #returning the list corresponding to the section of information 
    if section == "first name":
        return  contacts["first-name"]
    if section == "phone number":
        return contacts["phone_number"]
    if section == "last name":
        return  contacts["last-name"]
    if section == "address":
        return contacts["address"]
    if section == "email":
        return contacts["email_address"]

def getUpdate(section, title):
    #prompting the user for the updated info
    if section == contacts["email_address"]:
        while True:
            updated = getInput("Email")
            if checkEmail(updated) == False:
                continue
            break
    elif section == contacts["phone_number"]:
        updated = getNumber()
    else:
        updated = getInput(title)
    return updated

        

def showInfo(i):
    #Printing all contact information 
   print(f"""
*CONTACT INFORMATION*
First Name: {firstName[i]}
Last Name: {lastName[i]}
Address: {address[i]}
Phone Number: {phoneNumber[i]}
Email: {email[i]}
Date Added: {day[i]}\n""")
    


def updateContact():
    #update a contact already in the book 
    updating = True
    print("Enter the first and last name of the contact you would like to update")
    i = search()
    while updating == True: 
        choice = input("Which of the above would you like to update?\n").lower().strip()
        if choice not in sections:
            print("\nPlease enter from the above sections\nEx: first name\n")
            continue
        #grabbing the list that needs to be altered
        section = getSection(choice)
        print("\nEnter the updated information\n")
        #prompting the user for the updated version of the information
        updated = getUpdate(section, choice)
        #replacing the information in the contact book 
        print()
        section[i] = updated 
        day[i] = date.today()
        while True:
            repeat = input("Would you like to keep updating this contact?\n")
            if repeat == "yes":
                showInfo(i)
                break
            elif repeat == "no":
                print("Update finished.")
                updating = False
                break
            else: 
                print("\nPlease enter yes or no\n")
                continue



def deleteContact():
    #Deleting a contact made 
    print("Enter the first and last name of the contact you would like to delete.")
    i = search()
    #confirm the user would like to delete 
    confirmation = input("Are you sure you would like to proceed?\n: ")
    if confirmation == "yes":
        del firstName[i]
        del lastName[i]
        del address[i]
        del day[i]
        del phoneNumber[i]
        del email[i] 



def search():
    #searching for a contact the user would like to find 
    while True: 
        found = False
        input_first = getInput("First Name")
        input_last = getInput("Last Name")
        for i in range(len(firstName)):
            #if its in the contact bookm already
            if input_first == firstName[i] and input_last == lastName[i]:
                found = True
                showInfo(i)
        if found ==False :
            print("\nThis user was not in the contact book.\nPlease make sure to enter names correctly\n")
            continue
        break
    return i

def getNames(): 
    #Combining first and last names together in a list 
    fullNames = []
    for i in range(len(firstName)):
        fullNames.append(firstName[i] + " " + lastName[i])
    return fullNames


def displayAll():
    #Displaying all contacts 
    print("\n*ALL CONTACTS*")
    fullNames = getNames()
    fullNames.sort()
    for i in range(len(fullNames)):
        print(fullNames[i])
    print()
        

print("hi")


##RUN THE WHOLE PROGRAM yay!!
while True:
    user_response = showMenu()
    if user_response == 1:
        addContact()
    if user_response == 2:
        updateContact()
    if user_response == 3:
        deleteContact()
    if user_response == 4:
        displayAll()
    if user_response == 5:
        search()
    if user_response ==6:
        break
        

