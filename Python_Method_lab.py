# Going on camp :)
Camping_stuff= "tent, sleeping bag, water,knife, torch"
print(Camping_stuff)

# Python list
Camping_list= ["tent","sleeping bag","water","knife","torch"]



Camp_envi= ["kodur", 32 , 13.5 , True]

# Method concept in python
#adding toilet paper to our list
#append can add one item
Camping_list.append("toilet paper")

#extend will help to add multiple item, extend method

Camping_list.extend(["pencil","pen"]) 

#Another methon to add multiple item to list

Camping_list = Camping_list + ["soap","soup"]
# If I want to add item specific position, insert method

Camping_list.insert(0,"band")
Camping_list.insert(-4,"rope")

#deleting one item from the list, remove method

Camping_list.remove("tent")

#deleting multiple item from the list, remove method

Camping_list.pop(0)
# we can make what got delted to print 
print("We delete this "+ Camping_list.pop(2))

#Clearing all list,clear method

#Camping_list.clear()





print(Camping_list)