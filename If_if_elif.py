print("hello")
#will talk to machin 
input("")
name= input("what's your good name? \n")

# Using IF ELSE statment  to avoid Ben inside the program

if name == "ben":
    evil_status= input("are you evil? \n")
    # nested if 
    if evil_status== "yes":
        print("you are not welcome here")
        exit()
    else:
        print("you are one of those good ben")
else:
    wish= input("Hi "+ name + " what you wish for peace or happiness \n")