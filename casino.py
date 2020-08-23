#roulette
from random import *
#import winsound
#winsound.PlaySound("1.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
import time
cash = 100

print("welcome")
print("in my casino you can win ClootCoinsTM")
print("you have:"+str(cash)+" ClootCoinsTM")
print("have fun!")
motd = ["WINNING!","SUPREME!","EPIC!","POGGERS!","WINNER!","LIT!","SEXY!","PENG!","BELLE WOULD BE PROUD!"]

while True:
    RANDMOTD = randint(0,8)

    if cash <= 0:
        print("U POOR LUL")
        print("GAME OVER!")
        break    
    choice =input("red, black or green? ")
    wager =int(input("how much you want to bet? "))
    if wager > cash:
        print("YOU GOT NOTHING TO BET WITH! ")
        break

    prize = wager * 2
    green_prize = wager * 5
    roll = randint(0,100)

    if roll <= 49:
        print("ITS RED! ")
        if choice == "red":
            print("YOU WIN!")
            print(motd[RANDMOTD])    
           
            cash = cash + wager + prize
        else:
            print("YOU LOSE!")
            cash = cash - wager
        pass
    if roll >= 49:
        print("ITS BLACK! ")
        if choice == "black":
            print("YOU WIN!")
            print(motd[RANDMOTD])   
            cash = cash + wager + prize
        else:
            print("YOU LOSE!")
            cash = cash - wager
        pass
    if roll == 1:
        print("ITS GREEN!")
        if choice == "green":
            print("YOU WIN!")
            cash = cash + wager + prize + green_prize
            greenwin = 0
            while greenwin < 20:
                print("GREEN IS YOUR NEW FAVOURITE COLOUR! ")
                time.sleep(1)
                greenwin = greenwin + 1
                pass
        else:
            print("YOU LOSE!")   
            cash = cash - wager
    print("\n")   
    print("\n")  
    print("\n")  
    print("\n")  
  
    print("you have:"+str(cash)+" ClootCoinsTM")






