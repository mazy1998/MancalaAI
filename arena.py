

from gameClasses import *

def combination():
    count = 0 
    for ai in range(1,6):
        for pl in range(1,6):
            print(ai,pl,end = " ")
            initial = [0,0,np.full((2,6), 4)]
            a = MancalaState(initial)
            while not(a.isTerminal()):
                count += 1
                # print(a.isTerminal())
                #ai
                a = minimax(a, ai, 0)[0]
                # print(a)
                if a.isTerminal():
                    break
                # a = minimax(a,1,1)[0]
                # print("random")
                #pl1
                a = minimax(a, pl, 1)[0]
                # print(a)

            print(str(a.aiScore)+"-"+str(a.plScore))
            del a
    print(count)

count = 0
initial = [0,0,np.full((2,6), 4)]
a = MancalaState(initial)
while not(a.isTerminal()):
    count += 1
    a = minimax(a,3, 0)[0]
    print(a)
    if a.isTerminal():
        break
    #pl1
    a = moveRandom(a,1)[0]
    print(a)

print(str(a.aiScore)+"-"+str(a.plScore))
del a



# combination()
