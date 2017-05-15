import random
import itertools
###################################################
###################################################
###################################################

### THESE ARE HELPER METHODS FOR THE GAME CLASS ###

###################################################
###################################################
###################################################

def maxUtility(utility):
    max = 0
    if(utility[0] == utility[1] and utility[1] == utility[2]):
        max = random.choice([0,1,2])
    elif(utility[0]==utility[1] and utility[1] > utility[2]):
        max = random.choice([0,1])
    elif(utility[1]==utility[2] and utility[1] > utility[0]):
        max = random.choice([1,2])
    elif(utility[0]==utility[2] and utility[0] > utility[1]):
        max = random.choice([0,2])
    if(utility[max]<utility[1]):
        max = 1
    if(utility[max]<utility[2]):
        max = 2
    return max

def resetUtility():
    return {
        0:0,
        1:0,
        2:0
    }

def updateTable(condTable,move,kMoves):
    condTable[(kMoves,move)]+=1
    return condTable



###################################################
###################################################
###################################################

###THESE ARE HELPER METHODS FOR THE DRIVER CLASS###

###################################################
###################################################
###################################################
def whoWon(cMove,uMove):
    if(cMove == uMove):
        return 0
    elif( (cMove==1 and uMove==0) or (cMove==2 and uMove==1) or (cMove==0 and uMove==2)):
        return 1
    else:
        return -1


def updateGameLog(gameLog, winVal):
    gameLog["count"]+=1
    if(winVal==0):
        return gameLog
    if(winVal==-1):
        gameLog["userScore"]+=1
        return gameLog
    if(winVal==1):
        gameLog["cpuScore"]+=1
        return gameLog
