item=[5,2,3,1,4]
for x in range(len(item)):
    for y in range(x+1,len(item)):
        if item[x]>item[y]:
            print(item[x],item[y])
            big = item[y]
            item[y]=item[x]
            item[x]=big
            print(item)
                   
print(item, "sorted")
    