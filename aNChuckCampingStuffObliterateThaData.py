#1md Let's go on a camping trip - a nChuck pyEp9 clone!!
# here is the stuff needed :)

print("Let's go on a camping trip - a nChuck py Ep9 - clone!!\n")
print("here is the stuff needed :) below\n")

#tent, sleeping bags, water, raspberryPi, coffee, knife, ethernetCable, flashDrv, beardOil, marshmallows
campingStuff = "tent, sleeping bags, water, raspberryPi, coffee, knife, ethernetCable, flashDrv, beardOil, marshmallows"

print(campingStuff+"\n")

#pyList #aka supplies = the tent...
campingList = ["tent", "sleeping bags", "water", "raspberryPi", "coffee", "knife", "ethernetCable", "flashDrv", "beardOil", "marshmallows"]

#print(type(campingList))
#camp_site = ["crystal lake", 404, 89.3, True]
camp_site = ["crystal lake", 404, 95.5, 10, False]

#2md
# list.appEnd("singleItem"), 
# listExtend (["multiple", "items"]), 
# list = list + ["multiple", "items"], 
# list.insErt (0, "indexItems"),
# list.clear() == intire list..
# list.reMove("singleItem") 
# list.pop(single-index-nr)

# campingList -> supplies.append
#campingList.append("toilet paper")
#campingList.append("bidet")
campingList.extend (["toilet paper", "bidet"])
#campingList = campingList + ["toilet paper", "bidet"]
#campingList.insert (2, "toilet paper") or nex w negetive index below
#campingList.insert (-8, "toilet paper")
#campingList.clear()
#campingList.remove("tent") and 
#campingList.remove("sleeping bags")
#pop or obliterate tent + sleeping bags below, doble pop :)
print("This item was just deleted/poped/obliterated: " + campingList.pop(0))
campingList.pop(0)

#nChuck = campingList[4] cous inserted item in to index 2
nChuck = campingList[3]

#me = campingList[6] cous inserted item in to index 2
me = campingList[5]

#print(nChuck + me)
print("nChuck will add a: "+ nChuck)
print("and I'll' add a: "+ me+"\n")

print(campingList)