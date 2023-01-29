name= input("what's your good name? \n")

# Using IF ELSE statment & logical operator or to avoid Ben inside the program

if name == "ben" or name == "hulk" or name == "loki":
    evil_status= input("are you evil?\n")
    evil_no= input("how many evil thing you did today?\n") 
    if evil_status == "yes" and int(evil_no) < 4:
#        evil_no= input("how many evil thing you did today?\n")
#        if int(evil_no) < 4: >> used & logical operator for this condition
            print("come in")  
    else:
        print("you are not welcome here "+ name)
        exit()
else:
    wish= input("Hi "+ name + " what you wish for peace or happiness \n")