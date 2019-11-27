#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:43:35 2019

@author: mazeyarmoeini
"""
import numpy as np

# state = [0,0,np.full((2,6), 4)]
# MancalaState(state)


class MancalaState:
    """
    This class defines the mechanics of the puzzle itself.  The
    task of recasting this puzzle as a search problem is left to
    the EightPuzzleSearchProblem class.
    """

    def __init__( self, state ):
        """
          Constructs a new Mancala Board
                    ---------------------------------
                   |    | 4 | 4 | 4 | 4 | 4 | 4 |    |
                   | AI ------------------------- PL |
                   |    | 4 | 4 | 4 | 4 | 4 | 4 |    |
                    ---------------------------------

        """
        
        self.aiScore = state[0]            # default 0
        self.plScore = state[1]            # default 0
        self.board = state[2]              # default np.full((2,6), 4)
        self.boardShape = self.board.shape  # default (2,6)

    def isTerminal(self):
        return not np.any(self.board)

    def legalMoves(self):
        """
          Returns an tuple of legal moves from the current state.
          
                    ---------------------------------
                   |    | 3 | 0 | 3 | 0 | 0 | 2 |    |
                   | AI ------------------------- PL |
                   |    | 0 | 1 | 0 | 0 | 1 | 2 |    |
                    ---------------------------------

        return -> [(0,0),(0,2),(0,5),(1,1),(1,4),(1,5)]             
        """
        return np.column_stack(np.nonzero(self.board))
        # free = []
        #
        # for y in range(self.boardShape[0]):
        #     for x in range(self.boardShape[1]):
        #         if self.board[y][x] > 0:
        #             free.append((x, y))
        #
        # return free

    def result(self, move, state = None):
        """
          Returns a new Mancala state with the move applied to it.


        NOTE: This function *does not* change the current object. Instead, it returns a new object.
        """
        amount = self.board[move[0]][move[1]]
        current = [move[0], move[1]]
        player = move[0]
        self.board[move[0]][move[1]] = 0
        
        while amount != 0:
            
            if current[0] == 1:
                if current[1] == 5:
                    self.plScore += 1
                    
                    if amount == 0:
                        current = [0,5]
                    else:
                        current = [0,6]
                else:
                    if amount == 1 and current[0] == move[0]:
                        
                        if self.board[current[0]][current[1] + 1] == 0 and self.board[0][current[1] + 1] != 0 :
                            self.plScore += 1 + self.board[0][current[1] + 1]
                            self.board[0][current[1] + 1] = 0
                        else:
                            self.board[current[0]][current[1] + 1] += 1
                            current[1] += 1
                    else:
                        self.board[current[0]][current[1] + 1] += 1
                        current[1] += 1
                
            elif current[0] == 0:
                
                if current[1] == 0:
                    self.aiScore += 1
                    current = [1,0]
                    
                    if amount == 0:
                        current = [1,0]
                    else:
                        current = [1,-1]
                else:
                    if amount == 1 and current[0] == move[0]:
                        if self.board[current[0]][current[1] - 1] == 0 and self.board[1][current[1] - 1] != 0 :
                            self.aiScore += 1 + self.board[1][current[1] - 1]
                            self.board[1][current[1] - 1] = 0
                        else:
                            self.board[0][current[1] - 1] += 1
                            current[0] -= 1
                            
                            
                    else:
                        self.board[current[0]][current[1] - 1] += 1
                        current[1] -= 1
            
            
            print(amount,current)
#            if amount == 1 and current[0] == move[0]:
#                print(previousState)
#                print(self.board)
                
           
            amount -= 1
        
        return self.board,self.plScore,self.aiScore

    # Utilities for comparison and display
    def __eq__(self, other):
        """
            Overloads '==' such that two eightPuzzles with the same configuration
          are equal.

          >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \
              EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')
          True
        """
        for row in range( 3 ):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (13))
        lines.append(horizontalLine)
        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + col.__str__() + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()
    
    
# leboard = np.array([[0,0,1,1,1,1],
#                     [1,1,0,1,1,0]])

leboard = np.zeros((2, 6))

#state = [0,0,np.full((2,6), 4)]
    
state = [0,0,leboard]

a = MancalaState(state)

np.count_nonzero(a.board, axis=1)

np.any(a.board)


print(a.legalMoves())

move = a.legalMoves()[0]

# if move[0] == 1:
#     lst = a.board[1] + a.plScore +


# print(a.result( (1,4), state))
print(a.result( (1,3), state))
# print(a.result( (0,2), state))
# print(a.result( (0,3), state))
# print(a.result( (0,2), state))
# #print(a.result( (1,0), state))
# print(a.result( (0,1), state))
