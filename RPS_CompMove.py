import itertools
from RPS_Semantics import resetUtility
from RPS_Semantics import maxUtility
from RPS_Semantics import updateTable
from random import randint


class RPS_Game:

    def __init__(self, k):
        self.k = k
        self.condTable = {}
        self.combinations = itertools.product([0,1,2],repeat=k)
        for combo in self.combinations:
            self.condTable[(combo,0)]=.1
            self.condTable[(combo,1)]=.1
            self.condTable[(combo,2)]=.1
        self.kMoves = ()

        self.utility={
            0:0,
            1:0,
            2:0
        }

    def computeMove(self, gameLog, move):

        cpuChoice = 0


        #Get the total moves made with rock/paper/scissors
        #or the total moves made with count
        rockCount = gameLog[0]
        paperCount = gameLog[1]
        scissorCount = gameLog[2]
        rounds = gameLog["count"]

        if(len(self.kMoves)==self.k and rounds!=0):

            rock = self.condTable[self.kMoves,0]*(float(rockCount)/rounds)
            paper = self.condTable[self.kMoves,1]*(float(paperCount)/rounds)
            scissor = self.condTable[self.kMoves,2]*(float(scissorCount)/rounds)

            divisor = rock+paper+scissor

            probRock = rock/divisor
            probPaper = paper/divisor
            probScissor = scissor/divisor

            self.utility[0] = probScissor - probPaper
            self.utility[1] = probRock - probScissor
            self.utility[2] = probPaper - probScissor

            self.condTable = updateTable(self.condTable,move,self.kMoves)

            cpuChoice = maxUtility(self.utility)
            self.utility = resetUtility()

        else:
            cpuChoice = maxUtility({
                0:rockCount,
                1:paperCount,
                2:scissorCount
            })

        return cpuChoice





    def updateMoveHistory(self,newMove):
        if(len(self.kMoves)==self.k):
            self.kMoves=self.kMoves[1:]+(newMove,)
        else:
            self.kMoves=self.kMoves+(newMove,)
        return
