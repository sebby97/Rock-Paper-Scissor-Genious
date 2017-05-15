from RPS_CompMove import RPS_Game
from RPS_Semantics import whoWon
from RPS_Semantics import updateGameLog

gameLog = {
    "count" : 0,
    0 : 0,
    1 : 0,
    2 : 0,
    "userScore" : 0,
    "cpuScore" : 0
}


k=1

game = RPS_Game(k)
playGame = True

while(playGame):
    userMove = raw_input()
    userMove = int(userMove)
    #increment the number of times this move has been made
    gameLog[userMove] += 1
    #Call CPU move to get his next move!
    CPUmove = game.computeMove(gameLog,userMove)
    #Using the cpu and user entries find the winner of the round.
    winVal = whoWon(CPUmove,userMove)
    #update the game log with the appropriate scores!
    gameLog = updateGameLog(gameLog,winVal)
    #update the list of k last moves
    game.updateMoveHistory(userMove)
    print(CPUmove)
