def game (compchoice,yourchoice) :
    if compchoice=='r':
        if yourchoice=='p':
            return True
        elif yourchoice=='s':
            return False
    elif compchoice=='p':
        if yourchoice == 's':
            return True
        elif yourchoice=='r':
            return False
    elif compchoice=='s':
        if yourchoice=='r':
            return True
        elif yourchoice=='p':
            return False
    elif compchoice==yourchoice:
        return None

import random

print("computer's turn : rock(r), paper(p) or scissor(s) ? ")
randomnumber = random.randint(1,3)
if randomnumber==1 :
    compchoice='r'
elif randomnumber==2 :
    compchoice='p'
elif randomnumber==3 :
    compchoice='s'

yourchoice=input("your turn : rock(r), paper(p) or scissor(s) ? ")

a= game (compchoice,yourchoice)

print(f"computer chose {compchoice}")
print(f"you chose {yourchoice}")

if a==True :
    print("you won! ")
elif a==False :
    print("you lost !")
elif a==None :
    print("match tied !")