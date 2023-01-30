print("hello")
#will talk to machin 
input("")
name= input("what's your good name? \n")
name = name.lower()

if name == "ben" or name == "hulk" or name == "loki":
    evil_status= input("are you evil?\n")
 #   evil_no= input("how many evil thing you did today?\n") 
 #   if evil_status == "yes" and int(evil_no) < 4:
    if evil_status == "yes":
        evil_no= input("how many evil thing you did today?\n")
        if int(evil_no) < 4: # >> used & logical operator for this condition
            print("come in")  
        else:
            print("you are not welcome here "+ name)
            exit()
else:
    wish= input("Hi "+ name + " what you wish for peace or happiness \n")
#use that variable to ask further
#print("veg= 50")
#print("nonveg= 100")
wish= input("Hi "+ name + " what you wish to have veg meal or non-veg \n")
if wish== "veg":
    print("veg= 50")
#else:
#    print("nonveg= 100")
elif wish == "non-veg":
    print("non-veg= 100")
    spicy= input("Do you want it spicy ?\n")
Quantity= input("how many meal you need \n")

if wish == "non-veg":
    if spicy == "yes":
        price= 150 * int(Quantity)
    else:
        price= 100 * int(Quantity)
    
else:
    price= 50 * int(Quantity)
print("your total = " + str(price))
print("Sounds great " + name +" we have your " + str(Quantity) + " " + wish + " ready in a monent")
