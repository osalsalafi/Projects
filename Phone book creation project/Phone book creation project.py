from glob import glob


phone_book = {"1111111111" : "Amal", \
 	        "2222222222" : "Mohammed",\
            "3333333333" : "Khadijah" ,\
            "4444444444" : "Abdullah" ,\
            "5555555555" : "Rawan",\
            "6666666666" : "Faisal" ,\
            "7777777777":"Layla"}
flag = True
def search_by_number(number) :
    if len(number) == 10 and number in phone_book.keys():
        print(f"The owner of this phone number is : {phone_book[number]}")
    elif len(number) != 10 :
        print("This is invalid number")
    else :
        print("Sorry, the number is not found")
def search_by_name(name) :
    if name in phone_book.items():
        print(f"THe phone number of this name is : {str(phone_book.keys())[name]}")
    else :
        print("Sorry, the name is not found")
def add_newcontact(new_name,new_number):
    phone_book[new_number] = new_name
def choose(choice) :
    if choice == 1 :
        # Search for contact
        typeofsearch = int(input("Enter type of search (1) Number (2) Name : "))
        
        if typeofsearch == 1 :
            # Search by number
            search_by_number(input("Enter Number : "))
        
        elif typeofsearch == 2 :
            # Search by name
            search_by_name(input("Enter Name : "))
        
        else :
            # not valid type of search
            print("not valid")
    elif choice == 2 :
        # Add new contact
        new_name = input("Enter the contact name : ")
        new_number = input("Enter the contact number : ")
        add_newcontact(new_name,new_number)
    elif choice == 3 :
        # Get the list of contacts
        print(f"Number     | Name")
        for i in phone_book :
            print(f"{i} | {phone_book[i]}")
    elif choice == 0 :
        # will quit from the app
        global flag
        flag = False
    else :
        print("The choice is not valid")

while flag :
    choose(int(input("Enter type of service : (1) Search (2) New Contact (3) Phone Book (0) Quit : ")))



        

