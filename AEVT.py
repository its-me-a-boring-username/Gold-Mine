import random
import time

########################
###-Text & Variables-###
########################
your_debt = random.randint(2510,5000)

sg = "small gold ore"
mg = "medium gold ore"
lg = 'large gold ore'
di = 'a blue diamond'

mine_supply = [sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,
sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,sg,
sg,sg,sg,sg,sg,sg,sg,sg,sg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,mg,
mg,mg,mg,mg,mg,mg,mg,mg,lg,lg,lg,lg,lg,di] #65% small ore, 30% medium ore, 5% lare ore

###test data#### mine_supply = ['apple','orange','strawberry','watermelon','banana','rambutan'] 
ore_value = {
    sg:100,
    mg:200,
    lg:500
}

sack = []
stamina = 5
mined_ore = random.choice(mine_supply)
shop_items = ["", "house"]
balance = 10

###-Wake Up Text-###
wakeup = ["You wake up to the sounds of birds chirping","You wake up to the sounds of squirels eating", 
"You wake up to the sound of racoons fighting", "You wake up to your cat crying for food", 
"You wake up to the smell of roses","You wake up to your neighbors fighting about the laundry"]

###-Weather Text-###
sunny = "\nWhen you leave the house, it's a normal, sunny, day.\n"

rainy = "\nWhen you leave the house, it's raining cats and dogs, literally. You narrowly miss a terrier on your way to the mine.\n"

cloudy = '''\nWhen you leave the house, it is foggy, and the clouds are a soft, hazy, purple as the sun rises.
This has absolutely nothing to do with the chemical weapons facility down the street.\n'''

snowy = '''\nWhen you leave the house, you are met with the harsh glow of sunlight on snow. It is bright, and cold.
Your breath winds into smoky spirals as you walk through the snow.\n'''

icy = '''\nWhen you leave the house, you walk outside to a continuous sheet of ice. Everything is shiny, slick, and sharp.
If there was ever a day to stay home, this is it. You decided strap on an old pair of ice skates instead. Duty calls.\n'''

windy = '''\nWhen you leave the house, you open the door and are nearly blown over by fierce gusts of wind.
They whip by you with enough force to take your clothes with them. You lose your hat, then your coat.
You grip your remaining clothes and hope to arrive at your destination before the wind disrobes you completely.'''

dream = ["a very large melon","becoming a gilded cage", "your teeth falling out", "giving birth to triplets", 
"a house made of stars", "trying to escape a handsome stranger", "moving in with a small goat"]

###-Greeting Shopkeep-###
greet_a = "waves hello"
greet_b = "does't seem to notice"
greet_c = "smiles brightly"
greeting = [greet_a, greet_b, greet_c]


###-Story Text-###

welcome ='''\nWelcome To Gold Mine!\n
In order to play this game, type out your choice when presented with a set of options.
You can quit by typing 'quit' when asked to make a choice, but your progress won't be saved.\n
Let's test this out by choising a backstory for your character\n'''

choose_class = "Are you: \n\nan orphan\na retiree\na student\n"

student_description = (f'''\nYou're a poor college student. In addition to your $1,570,300 in student loans,
you managed to rack up parents ${your_debt} in extremely high interest credit card debt paying
for premium ramen. The ramen was worth it, but, unless you want to pay 3000% interest on your purchase 
after the special introductory rate ends this month, you need a way to quickly make some cash.''')

orphan_description = (f'''\nYou were orphaned tweleve years a go after your parents died in a myserious accident
that involved an abandoned factory, fake rubies, and expired cherry jello. No one will tell you what really 
happened that night, and you've spent thousands of dollars trying to find out. You currently owe ${your_debt} 
to a very agressive PI who knows where you live (of course they do), and you need to pay them back asap''')

retiree_description = (f'''\nAfter decades of hard work and expert money management, you managed to save several million dollars for your retirement.
Unfortuately for you inflation has been bad. Like, really, really bad. The value of your savings has plummeted over the past few years, 
and you may have compunded your money issues by borrowing {your_debt} from a loan shark to pay for the completion of your brekfast nook. 
It was worth it, but you need a way to pay him back as soon as possible''')

story_context_1 = '''\nFortunately for you, something unusual and very lucky has happened:

After months of struggling with your finances, you decide to move back to your childhood home. 
It's been empty for a while, but a kind neighbor, Abigail, has maintained the property as a favor 
to you and your family.

At first, noting seems to have changed: the kitchen is still covered in yellow paisley wallpaper,
the bathroom sink still drains one drop at a time, and the giant cavern in the far corner of the yard (
next to your mother's rosebushes) remains untouched. Everything seems to be in order except...
you don't recall there being a giant hole in the garden. '''

story_context_2 = '''\nYou decide to ask Abigail about it, and apparently it is new. She claims to have sent you several emails about it.

She requested a survery after taking some samples to a local geologist, and apparently your yard has collapsed 
into an old gold mine. Normally it would take years of inspections and tens of thousands of dollars in permits 
before you could start excavation, but she slipped someone at the land bureau $20 to leave you alone. 
You'll be able to excavate, so long as you do it by hand. You thank Abigail profusely for her kindness, 
and set off to inspect the mine more closely'''

meet_shopkeeper_1 = f'''\nAs you head toward the mine, you notice a man waving at you next to a makeshift booth.
You have no clue what he's doing in your backyard, but you don't think you can avoid him.

Before you can ask what he's doing on your property, he quickly approcahes and starts talking at you:'''

meet_shopkeeper_2 = f'''\n"You're finally here! Thank goodness I've been waiting for months! I'm Tom, newest member of the shopkeeper's guild. 
I've been sent here to make sure you have a place to buy and sell things and to repay your debt whenever you are ready. 
Oh, don't look so shocked. We buy everyone's data. Didn't you get our postcard about your cat?

Let's not dwell on that too much. It looks like you have ${your_debt} in high interst debt you need to take care of 
right away. I'm happy to help you with that. I'll buy any gold you can dig up, but I pay based on ore size. I'll give
you $100 for anything small, $200 for medium ore, and $500 fore the large ones. You might also find a very rare diamond,
but those are useless in this version of the game."''' 

meet_shopkeeper_3 ='''\n"I won't often have things to sell you, but I do currently have a Porsche Taycan I am willing to part with for only $300.
Pease do not ask how I got it.

Oh, before you go, please take these mining tools with you. Don't forget to come back tomorrow!"
'''

mine_descirption = '''\nTom spins you around and gently pushes you in the direction of the mine before returning to his work.

A few seconds later you approah it. The ground is muddy and slopes down towards the curved walls of the cavern.
It is dark and intimidating, but you remember that Tom gave you several items before he sent you on your way. 
You look through the bag he handed you to find a pair of thick traction boots, a helmet with a built in light, and a pickaxe.

You could go home, but you have nothing else to do today. You put on the equipment, and start to dig'''

end_paragraph = "the end"


##############
###-Events-###
##############

###############
###-Minning-###
###############

def mine(cycles, old_list, new_list):

    while cycles > 0:
        list_item = random.choice(old_list)
        new_list.append(list_item)
        print (f"You mine a {list_item} and put it in your sack")
        old_list.remove(list_item)
        cycles -=1
        time.sleep(1)

########################
###-Buying & Selling-###
########################

#####-Sell One User Specified Item-#####

def sell(list, item, cost):
    global balance
    pay_item = list.count(item)*(cost)

    balance = (pay_item + balance)
    
    print(f"\nYou sell {list.count(item)} {item} for {pay_item} dollars")
    time.sleep(1)
    print(f"The Shopkeeper pays you {pay_item} dollars")
    time.sleep(1)
    print(f"You now have {balance} dollars")
    #print(list)

    while item in list:
        list.remove(item)

    #print(list)

############-Sell Three Items-################

def sellall(list, item1, item2, item3,cost1, cost2, cost3):
    global balance
    
    pay_item_1 = list.count(item1)*(cost1)
    pay_item_2 = list.count(item2)*(cost2)
    pay_item_3 = list.count(item3)*(cost3)

    total_payment = (pay_item_1+pay_item_2+pay_item_3)
    balance = (total_payment + balance)
    
    print(f"You sell {list.count(item1)} {item1} for {pay_item_1} dollars")
    time.sleep(1)
    print(f"You sell {list.count(item2)} {item2} for {pay_item_2} dollars")
    time.sleep(1)
    print(f"You sell {list.count(item3)} {item3} for {pay_item_3} dollars")
    time.sleep(1)
    print(f"The Shopkeeper pays you {total_payment} dollars")
    print(f"You now have {balance} dollars")
    list.clear()

############-Buy An Item From a List/Dictionary-############
def buy(old_list,new_list,item,cost):
    global balance

    if cost < balance:
        print(f"You paid {cost} for {item}")
        time.sleep(1)
        balance = (balance - cost)
        print(f"Your new balance is {balance}")
        print(f"You now have a {item}")
        new_list.append(item)
        old_list.remove(item)
        #print(old_list)
        #print(new_list)

    else:
        print("You don't have enough money for this")

########################-Shopping Experience-########################
def go_shopping():
    global balance
    
    stuff_for_sale = {
        "Porsche Taycan": 300,}
    #-menu persistence and options-#
    view_menu = True
    if balance > your_debt:
        print("It looks like you have enough money to repay your debt now.")
        print(f"Your balance is {balance}, and you owe {your_debt}")
        balance = (balance - your_debt)
        print(f"You've repaid your debt and have {balance} to spare!")
        print(end_paragraph)
        quit()
    while view_menu == True:
        offer_menu = input('\nbuy something \nsell ore \nsell all ore \ngo home\n')
    #-quit-#    
        if offer_menu.lower() == 'quit':
            quit()
    #-repay debt-#
        
    #-buying things-#
        elif offer_menu.lower() == 'buy something':
            while stuff_for_sale =={}:
                print("There is nothing for sale right now")
                break
            else:
                print("The following items are for sale")
                print(stuff_for_sale)
                want = input("What would you like to buy?")
                if want.lower() not in stuff_for_sale:
                    print("We don't have that item in stock")
                else:
                    print(f"This {want} costs {stuff_for_sale.get(want)}")
                    if stuff_for_sale.get(want)> balance:
                        print("You don't have enough money for that, sorry.")
                    else:
                        balance = (balance - stuff_for_sale.get(want))
                        print(f"You now own a {want}")
                        print(f"Your new balance is now {balance}")
                        stuff_for_sale.pop(want)
                        leave = print("Go home, or do something else?") 
    #-selling some ore-#
        elif offer_menu.lower() == 'sell ore':
            x = input(f"What are you selling: \n{sg} \n{mg} \n{lg}")
            if x.lower() == (f"{sg}"):
                sell(sack,sg,ore_value.get(sg))
            elif x.lower() == (f"{mg}"):
                sell(sack,mg,ore_value.get(mg))
            elif x.lower() == (f"{lg}"):
                sell(sack,lg,ore_value.get(lg))
            else:
                print("You can't sell that")
    #-selling all ore-#
        elif offer_menu.lower() == 'sell all ore':
            if sack.count(sg) + sack.count(sg) + sack.count(sg) == 0:
                print("You've already sold all of your ore")
            else:
                sellall(sack,sg,mg,lg,ore_value.get(sg),ore_value.get(mg),ore_value.get(lg))
    #-go home-#    
        elif offer_menu.lower() == 'go home':
            #mine(stamina,mine_supply,sack)
            break
    #-Error Message-#    
        else:
            print("I don't know what you mean by that, choose something else")
#########################################################################################


########################
###-Debt & Repayment-###
########################

#############
###-Other-### 
#############

#################
###-Core Loop-### 
#################
def go_home():
    input(f'''\nYou're too tired to continue.\nHaving exhausted yourself in the mine and already visited the shop, you finally make your way home.\nYou crawl into bed and sleep soudly. You dream about {random.choice(dream)}\n\nhit ENTER to continue\n''')


def core_loop():
    global your_debt

    while your_debt > 0:
        weather = [sunny, rainy, cloudy, snowy, windy, icy]
        print(f"{random.choice(wakeup)}\n")
        input(f"{random.choice(weather)}\n\nhit ENTER to continue\n")
        pass
        mine(stamina,mine_supply,sack)
        time.sleep(1)
        input(f"\nYou walk to the shopkeepers makeshift booth. He {random.choice(greeting)} as you approach him\n\nhit ENTER to continue\n")
        pass
        go_shopping()
        time.sleep(1)
        go_home()
        #input("\n\nhit ENTER to continue\n")
        continue
