list_fruit=["lemon","apple","watermelon","durian","strawberry"]

for fruit in list_fruit:
    if fruit=="apple":
        print ("I found it")
        
list_fruit.append("lychee")
list_fruit.append("custard-apple")

list_num=[];

for fruit in list_fruit:
    list_num.append(len(fruit))
    print (fruit," has ",len(fruit)," letters")
