#1md lets build a Robo Barista / Bouncer!!\n",
# "Building a coffe shop using some new py Prog. concepts"

#lets greet the customer frist
print("Hello, Welcom to NetworkChuck Coffeeeeeeeee - just a clone EP6 !!")

#Ask Customer that ther name is with the input() func and store that in the var name.
name = input("Name here pls?\n")

#2md if's, Or's, And's, Else's, Not's
#Greet the customer with thair name and thank them for coming in today using concatenation.
if name  == "ben" or name == "patricia" or name == "loki" or name != "" or name == "":
    evil_status = input("Up4Some Evil?\n")
    good_deeds = int(input("How many goodDeeds today Evil?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("NOOO-Not Welcome Evil " + name + ", Leave now pls - Nex!!")
        #print("then EvilKenivelBasterd?\n")
        exit()
    else:
        print("Hello " + name + ", and Welcome back, frien!!\n\n\n")
else:
    print("Hello " + name + ", thanks for serving EP4 today.\n\n\n")

#Caff menu
menu = "caseSensitivePls, Black Coffee, Espresso, Latte, 80C deg, Cappu, Frappu"

#Ask customer what they would like from the menu and store it in the var ORDER.
order = input(name + ", what like from menu today? Here is what are serving.\n" + menu + "\n")

#Ask customer how many coffees they would like and store it in the var QUANTITY
quantity = input("how many coffees would like?\n")


#3md if and else or newCon elif
#Set the price for coffee
if order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    wipped_cream = input("with wCream Sir?\n")
    if wipped_cream == "yes":
        price = 10
    else:
        price = 7
elif order == "80C deg":
    price = 0
elif order == "Cappu":
    price = 11
elif order == "Frappu":
    price = 13
else:
    print("Desolee, no have..")
    price = 0

print("Ok $ " + str(price))

#Calc the customer's total
total = price * int(quantity)

#Serve the customer's thier total
print("ThanX, Thee total will be: $" + str(total))

#Final statement
print("Perfecto " + name + ", Philips will have " + quantity + " " + order + " ready in 3min's boss.")