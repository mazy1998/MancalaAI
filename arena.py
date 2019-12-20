

from gameClasses import *
import time
from datetime import datetime

def combination():
    final = 0
    count = 0 
    for ai in range(1,6):
        for pl in range(1,6):
            print(ai,pl,end = " ")
            initial = [0,0,np.full((2,6), 4)]
            a = MancalaState(initial)
            while not(a.isTerminal()):
                count += 1
                '''
                Change player 1 here
                '''
                a = minimax(a, ai, 0)[0]
                # print(a)
                if a.isTerminal():
                    break
                '''
                Change player 2 here
                '''
                a = alphabeta(a, pl, 1)[0]
                # print(a)

            print(str(a.aiScore)+"-"+str(a.plScore))
            del a
    print(count)

def timings():
    final = 0
    count = 0 
    for ai in range(1,8):
        pl = 1
        now =  time.time()
        print(ai,pl,end = " ")
        initial = [0,0,np.full((2,6), 4)]
        a = MancalaState(initial)
        while not(a.isTerminal()):
            count += 1
            '''
                Change player 1 here
            '''
            a = minimax(a, ai, 0)[0]
            
            if a.isTerminal():
                break
            '''
                Change player 2 here
            '''
            a = minimax(a, pl, 1)[0]
            

        print(str(a.aiScore)+"-"+str(a.plScore), time.time()-now)
        del a

    print(count)


combination()
# timings()


