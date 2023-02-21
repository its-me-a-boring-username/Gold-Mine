###///GOLDMINE\\\###
#### A TEST GAME ###
#py AE.py

import time
import AEVT

play = 0
print(AEVT.welcome)
time.sleep(7)

while play == 0:
    character = input(AEVT.choose_class)
    if character.lower() == "a student":
        input(f"{AEVT.student_description}\n\nhit ENTER to continue")
        play += 1
        continue
    elif character.lower() == "an orphan":
        input(f"{AEVT.orphan_description}\n\nhit ENTER to continue")
        play += 1
        continue
    elif character.lower() == "a retiree":
        input(f"{AEVT.retiree_description}\n\nhit ENTER to continue")
        play += 1
        continue
    elif character.lower() == "quit":
        play +=1
        quit()
    else:
        print("If you enter text that doesn't match an existing option,\nyou'll get a weird message like this\nLet's try again")
        time.sleep(3)
        continue
while play == 1:
    input(f"{AEVT.story_context_1}\n\nhit ENTER to continue")
    pass
    input(f"{AEVT.story_context_2}\n\nhit ENTER to continue")
    pass
    input(f"{AEVT.meet_shopkeeper_1}\n\nhit ENTER to continue")
    pass
    input(f"{AEVT.meet_shopkeeper_2}\n\nhit ENTER to continue")
    pass
    input(f"{AEVT.meet_shopkeeper_3}\n\nhit ENTER to continue")
    pass
    input(f"{AEVT.mine_descirption}\n\nhit ENTER to continue\n")
    play += 1

AEVT.mine(AEVT.stamina,AEVT.mine_supply,AEVT.sack)
AEVT.go_home()
AEVT.core_loop()

#in the backyard of your childhood home. 
#I grew up in an apartment
#That seems awfully convenient
#look, we're trying to wrap up this apprenticeship application, and unlike some people we have a day job. Just roll with it.