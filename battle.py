import random 
import time
players_hp = 35
goblins_hp = 33
print("whlie walking through the dense forest u come across a wild goblin")
while players_hp>0 and goblins_hp>0:
    print("-"*20)
    print("Your HP=",players_hp ,"|Goblin Hp=",goblins_hp)
    choice=input("Type 1 to attact or 2 to heal:")
    if choice =="1":
        damage=random.randint(8,15)
        goblins_hp=goblins_hp-damage
        print("You slashed the goblin!",damage,"damage done!!")
    elif choice =="2":
        heal=random.randint(8,15)
        players_hp=players_hp+heal
        print("You drank a potion and recoverd",heal,"HP")
    else:
        print("You panicked and missed ur turn!")
    time.sleep(1)
    if goblins_hp>0:
        goblins_dmg=random.randint(8,15)
        players_hp=players_hp-goblins_dmg
        print("The goblin has attacked you got",goblins_dmg,"Damage!")
        time.sleep(1)
print("-"*20)
if players_hp>0:
    print("victory you have won")
else:
    print("Game Over,..You got eaten")
