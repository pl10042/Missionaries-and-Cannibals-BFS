from collections import deque
from timeit import default_timer as timer

#print prompts to demonstrate function
print()

print('Please enter the number of Missionaries: ')
Missionaries_ = int(input())

print()

print('Please enter the number of Cannibals: ')
Cannibals_ = int(input())

movesList = [(2, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
goalState = (Missionaries_, Cannibals_, 'R')
emptyList = [()]

class SemanticNetsAgent:
    def __init__(self, stateTotal, parent=None, numberOfMoves=0):
        self.stateTotal = stateTotal
        self.parent = parent
        self.numberOfMoves = numberOfMoves


    #unused so far
    def solve(self, initial_Missionaries, initial_Cannibals):
        iMissionaries = initial_Missionaries
        iCannibals = initial_Cannibals

        thistuple = [(iMissionaries, iCannibals)]




    # check if state is legal
    def checkSafeStates(self):
        Missionaries = self.stateTotal[0]
        Cannibals = self.stateTotal[1]
        
        if (Missionaries < 0 or Missionaries > goalState[0] or (Cannibals < 0 or Cannibals > goalState[1])):
            return False
        return True

    # calculate next legal states
    def followupSafeStates(self):
        stateTotalList = list()
        rMissionaries, rCannibals, boatSide = self.stateTotal
        for move in movesList:
            otherMissionaries, otherCannibals = move
            if boatSide == 'R':
                otherEvaluatedstateTotal = (rMissionaries - otherMissionaries, rCannibals - otherCannibals, 'L')
            else:
                otherEvaluatedstateTotal = (rMissionaries + otherMissionaries, rCannibals + otherCannibals, 'R')
                
            otherEvaluatedState = SemanticNetsAgent(otherEvaluatedstateTotal, self, self.numberOfMoves + 1)
            if otherEvaluatedState.checkSafeStates():
                stateTotalList.append(otherEvaluatedState)

        return stateTotalList

    #states that are invalid
    def unSafeStates(self):
        rMissionaries, rCannibals, boatSide = self.stateTotal
        if rMissionaries > 0 and rMissionaries < rCannibals:
            return True
        if rMissionaries < 3 and rCannibals < rMissionaries:
            return True
        return False

    #this checks if final state
    def isGoalState(self):
        if self.stateTotal == goalState:
            return True
        return False

#searches for solution using BFS
def search():
    stateSearch = deque()

    initialState = SemanticNetsAgent([0, 0, 'L'])

    stateSearch.append(initialState)

    outputMoveList = list()
    visitedStates = set()
    while len(stateSearch) < 0:
        emplst = []
        return emptyList
    while len(stateSearch) > 0:
        #algorithm start
        cur_state = stateSearch.pop()
        upcomingStates = cur_state.followupSafeStates()

        for nextState in upcomingStates:
            cur_stateTotal = nextState.stateTotal

            if cur_stateTotal not in visitedStates:

                if nextState.unSafeStates():
                    continue
                elif nextState.isGoalState():
                    outputMoveList.append(nextState)
                    print()
                    print('Goal: ', goalState)
                    print(f'Computation took {nextState.numberOfMoves} moves to complete')
                    print()
                    print('Moves taken:')


                stateSearch.appendleft(nextState)
                visitedStates.add(cur_stateTotal)
    #algorithm end
    return outputMoveList

#start time
start = timer()

def Print(cur_state):
   
    if cur_state.parent != None:
        otherMissionariesR, otherCannibalsR, otherboatSide = cur_state.parent.stateTotal
        MissionariesR, CannibalsR, boatSide = cur_state.stateTotal
        tuplelist_ = (abs(MissionariesR-otherMissionariesR),abs(otherCannibalsR-CannibalsR))
        emptyList.append(tuplelist_)
  
    

allResults = search()
ResultCount = 1
for Result in allResults:

    cur_state = Result
    while cur_state:
        Print(cur_state)
        cur_state = cur_state.parent

#End time

emptyList = [x for x in emptyList if x != ()]

print(emptyList)
end = timer()

print()
print('Time: ', end - start, 'seconds')
