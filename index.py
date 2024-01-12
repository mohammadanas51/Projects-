# Stone Paper Scissor game using python
# this is a sample comment to modify this file 
# Function to decide wether the user wins or not 
def gamewin(comp, you) :
    if comp == you :
        return None
    if comp == "st" and you == "pa" :
        return True
    elif comp == "pa" and you == "sc" :
        return True
    elif comp == "sc" and you == "st" :
        return True
    elif comp == "pa" and you == "st" :
        return False
    elif comp == "sc" and you == "pa" :
        return False
    elif comp == "st" and you == "sc" :
        return False

# Showing the computer's choice 
import random
print("Computer's turn Stone Paper or Scissor") 
x = random.randint(1,3)  
# Assigning stone paper or scissor to computer based on random number 
if x == 1 :
    comp = "st"
elif x == 2 :
    comp = "pa"
elif x == 3 :
    comp = "sc"
 
 # Taking user's input
you = input("Your choice Stone (st) Paper (pa) or Scissor (sc) : ")

# to display what the user has chosen
if you == "st" :
    print("You have chosen STONE")
elif you == "sc" :
    print("You have chosen SCISSOR")
elif you == "pa" :
    print("You have chosen PAPER")
# to display what the computer has chosen
if comp == "st" :
    print("Computer has chosen STONE")
elif comp == "sc" :
    print("Computer has chosen SCISSOR")
elif comp == "pa" :
    print("Computer has chosen PAPER")

# to display the results 
res =  gamewin(comp,you) 
if res == None :
    print("Game is a draw")
elif res == True :
    print("You Win !!!")
elif res == False :
    print("You Loosu !!!")