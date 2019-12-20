#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:43:35 2019

@author: mazeyarmoeini
"""
import numpy as np
import random

# state = [0,0,np.full((2,6), 4)]
# MancalaState(state)
traverse_log = list()


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
        aiboard = self.board[0].sum()
        plboard = self.board[1].sum()
        over = False
        if aiboard == 0 or plboard ==0:
            over = True
            self.aiScore += aiboard
            self.plScore += plboard
            self.board = np.zeros((2,6)).astype(int)
        return over

    def legalMoves(self, player):
        """
          Returns an tuple of legal moves for player from the current state.

                    ---------------------------------
                   |    | 3 | 0 | 3 | 0 | 0 | 2 |    |
                   | AI ------------------------- PL |
                   |    | 0 | 1 | 0 | 0 | 1 | 2 |    |
                    ---------------------------------

        return -> [(0,0),(0,2),(0,5)] for player 0
                  [(1,1),(1,4),(1,5)] for player 1
        """
        frees = np.nonzero(self.board[player])
        index = np.full((1, len(frees[0])), player)

        return np.column_stack((index[0], frees[0]))

    def result(self, move):
        """
          Returns a new Mancala state with the move applied to it as well as the player who has the next turn.
        NOTE: This function *does not* change the current object. Instead, it returns a new object.

        """
        newBoard = MancalaState([self.aiScore, self.plScore, np.copy(self.board)])

        amount = newBoard.board[move[0]][move[1]]
        current = [move[0], move[1]]
        original  = [move[0], move[1]]
        #        player = move[0]
        newBoard.board[move[0]][move[1]] = 0

        # player gets extra move if last pebble lands in the same player's mancala
        extraMove = False
        # nextMoveDict = {0: 1, 1: 0}
        # movesNext = nextMoveDict[move[0]]
        # print(f'movesNext initially set to: {movesNext}')

        while amount != 0:
            if current[0] == 1:
                if current[1] == 5:
                    # print(f'amount: {amount}')
                    newBoard.plScore += 1

                    # if amount == 0:
                    #     current = [0, 5]

                    if amount == 1 and current[0] == original[0]:
                        # movesNext = 1  # Since player 1's move ended in their Mancala, it's their turn again
                        # print('movesNext set to 1')
                        # print(current,original)
                        extraMove = True

                    else:
                        # movesNext = 1  # Since player 1's move ended in their Mancala, it's their turn again
                        # print('movesNext set to 1')
                        current = [0, 6]  # This index doesn't exist in the array??
                else:
                    if amount == 1 and current[0] == move[0]:

                        if newBoard.board[current[0]][current[1] + 1] == 0 and newBoard.board[0][
                            current[1] + 1] != 0:
                            newBoard.plScore += 1 + newBoard.board[0][current[1] + 1]
                            newBoard.board[0][current[1] + 1] = 0
                        else:
                            newBoard.board[current[0]][current[1] + 1] += 1
                            current[1] += 1
                    else:
                        newBoard.board[current[0]][current[1] + 1] += 1
                        current[1] += 1

            elif current[0] == 0:

                if current[1] == 0:
                    newBoard.aiScore += 1
                    current = [1, 0]

                    if amount == 0:
                        current = [1, 0]
                    if amount == 1 and current[0] == original[0]:
                        # print(current,original)
                        # movesNext = 0
                        extraMove = True
                    else:
                        current = [1, -1]
                else:
                    if amount == 1 and current[0] == move[0]:
                        if newBoard.board[current[0]][current[1] - 1] == 0 and newBoard.board[1][
                            current[1] - 1] != 0:
                            newBoard.aiScore += 1 + newBoard.board[1][current[1] - 1]
                            newBoard.board[1][current[1] - 1] = 0
                        else:
                            newBoard.board[0][current[1] - 1] += 1
                            current[0] -= 1


                    else:
                        newBoard.board[current[0]][current[1] - 1] += 1
                        current[1] -= 1

            amount -= 1

        return newBoard, extraMove

    def eval(self, max_player):
        if max_player == 1:
            return self.plScore - self.aiScore
        else:
            return self.aiScore - self.plScore
        # Return score if playerNo == 1. Return -score if playerNo == 0.
        # if playerNo == 1:
        #     return score
        # else:
        #     return -score


    # Utilities for comparison and display
    # def __eq__(self, other):
    #     """
    #         Overloads '==' such that two eightPuzzles with the same configuration
    #       are equal.
    #
    #       >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \
    #           EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')
    #       True
    #     """
    #     for row in range( 3 ):
    #         if self.cells[row] != other.cells[row]:
    #             return False
    #     return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        # lines = []
        # horizontalLine = ('-' * (13))
        # lines.append(horizontalLine)
        # for row in self.cells:
        #     rowLine = '|'
        #     for col in row:
        #         if col == 0:
        #             col = ' '
        #         rowLine = rowLine + ' ' + col.__str__() + ' |'
        #     lines.append(rowLine)
        #     lines.append(horizontalLine)
        # return '\n'.join(lines)
        return f'AI score: {self.aiScore}, Pl score: {self.plScore}.\n{self.board}'

    def __str__(self):
        return self.__getAsciiString()


def print_mm_log(move, depth, value): #Print log for minimax
    global traverse_log
    traverse_log.append(move + "," + str(depth) + "," + str(value) + "\r\n")


# Min Max
def minimax(state, depth_limit, max_player):
    return maxM(state, depth_limit, 0, max_player, False)  # return board, val


def maxM(state, depth_limit, depth, max_player, extra_move):
    if state.isTerminal() or (depth == depth_limit and not extra_move):
        # print(f'Returned max move {state}, {state.eval()} at depth {depth} ')
        return state, state.eval(max_player)

    best_state, best_val = state, -np.Inf # Should this be state.eval?
    depth_next = depth + 1 if not extra_move else depth
    # print(f'maxM called at depth {depth} with best val {best_val}')

    for move in state.legalMoves(max_player):
        # print('Max evaluating move: ', move)

        next_board, next_extra = state.result(move)

        if next_extra:
            b, v = maxM(next_board, depth_limit, depth_next, max_player, next_extra)
        else:
            b, v = minM(next_board, depth_limit, depth_next, max_player, next_extra)
        if v > best_val:
            best_state = next_board if not next_extra else b
            best_val = v
            # print('max move: ', move, depth, best_val)

    return best_state, best_val


def minM(state, depth_limit, depth, max_player, extra_move):  # extra_move boolean tells if it has free move available

    if state.isTerminal() or (depth == depth_limit and not extra_move):
        # print_mm_log(board.move_name, depth, boardval)
        return state, state.eval(max_player)

    best_state, best_val = state, np.Inf  # Should this be state.eval?
    depth_next = depth + 1 if not extra_move else depth
    # print(f'minM called at depth {depth} with best val {best_val}')

    for move in state.legalMoves(1 - max_player):
        next_board, next_extra = state.result(move)

        if next_extra:
            b, v = maxM(next_board, depth_limit, depth_next, max_player, next_extra)
        else:
            b, v = minM(next_board, depth_limit, depth_next, max_player, next_extra)
        if best_val == np.Inf or v < best_val:
            best_state = next_board if not next_extra else b
            best_val = v
            # print(move, depth, best_val)
        # print_mm_log(board.move_name, depth, optimumVal)

    return best_state, best_val


def moveRandom(state,player):
    board = [state,True]
    while not(a.isTerminal()) and board[1]:
        moves = state.legalMoves(player)
        move = random.choice(moves)
        board = state.result(move)
        
        if board[0].isTerminal() or len(moves) == 1:
            break
    # print(board[0].board)
    return board

# Alpha Beta
def alphabeta(state, depth_limit, max_player):
    return maxAB(state, depth_limit, 0, max_player, False, -np.Inf, np.Inf)  # return board, val


def maxAB(state, depth_limit, depth, max_player, extra_move, alpha, beta):
    if state.isTerminal() or (depth == depth_limit and not extra_move):
        # print(f'Returned max move {state}, {state.eval()} at depth {depth} ')
        return state, state.eval(max_player)

    best_state, best_val = state, -np.Inf  # Should this be state.eval?
    depth_next = depth + 1 if not extra_move else depth
    # print(f'maxAB called at depth {depth} with best val {best_val}')

    for move in state.legalMoves(max_player):
        # print('MaxAB evaluating move: ', move)

        next_board, next_extra = state.result(move)

        if next_extra:
            b, v = maxAB(next_board, depth_limit, depth_next, max_player, next_extra, alpha, beta)
        else:
            b, v = minAB(next_board, depth_limit, depth_next, max_player, next_extra, alpha, beta)
        if best_val == -np.Inf or v > best_val:
            best_state = next_board if not next_extra else b
            best_val = v
            # print('max move: ', move, depth, best_val)

        # if v >= beta and beta != np.Inf:
        #     print(f'max, alpha: {alpha}, beta: {beta}')
        #     if beta <= alpha:
        #         print(f'alpha: {alpha}, beta: {beta}')
        #     return best_state, v

        if v > alpha or alpha == -np.Inf:
            # print(f'updating alpha', v, 'depth', depth, 'alpha', alpha)
            alpha = v  # change to max

        # print(f'MAX alpha: {alpha}, beta: {beta}')
        if beta <= alpha:
            print(f'alpha: {alpha}, beta: {beta}')
            return best_state, v

    return best_state, best_val


def minAB(state, depth_limit, depth, max_player, extra_move, alpha, beta):  # extra_move boolean tells if it has free move available
    if beta <= alpha:
        print(f'aaaalpha: {alpha}, beta: {beta}')

    if state.isTerminal() or (depth == depth_limit and not extra_move):
        # print_mm_log(board.move_name, depth, boardval)
        return state, state.eval(max_player)

    best_state, best_val = state, np.Inf  # Should this be state.eval?
    depth_next = depth + 1 if not extra_move else depth

    for move in state.legalMoves(1 - max_player):
        next_board, next_extra = state.result(move)

        if next_extra:
            b, v = minAB(next_board, depth_limit, depth_next, max_player, next_extra, alpha, beta)
        else:
            b, v = maxAB(next_board, depth_limit, depth_next, max_player, next_extra, alpha, beta)
        if best_val == np.Inf or v < best_val:
            best_state = next_board if not next_extra else b
            best_val = v
            # print(move, depth, best_val)

    # if alpha >= v and alpha != -np.Inf:
    #     # print(f'returning min early, alpha: {alpha}, beta: {beta}')
    #     if beta <= alpha:
    #         print(f'aalpha: {alpha}, beta: {beta}')
    #     return best_state, v

    if beta == np.Inf or v < beta:
        # print(f'updating beta', v, 'depth', depth, 'alpha', alpha)
        beta = v

    # print(f'MIN alpha: {alpha}, beta: {beta}')
    if beta <= alpha:
        # print(f'aalpha: {alpha}, beta: {beta}')
        return best_state, v

    return best_state, best_val











# leboard = np.array([[3,2,1,1,1,1],
#                      [,0,0,1,1,0]])

# leboard = np.zeros((2, 6))

state = [0,0,np.full((2,6), 1)]

# initial
initial = [0,0,np.full((2,6), 4)]
# tie
tie = [23,23,np.array([[0,0,0,0,0,1],[0,0,0,0,0,1]])]
# p1 win
win = [18,26,np.array([[0,0,0,1,1,1],[0,0,0,0,1,0]])]
# AI win
lose = [26,20,np.array([[0,0,0,0,0,1],[0,0,0,0,0,1]])]


testing = [11,6,np.array([[0,9,9,0,0,0],[0,5,1,0,0,7]])]


lose = [26,20,np.array([[1,0,0,0,0,0],[0,0,0,0,1,0]])]

# state = [0,0,leboard]
#
a = MancalaState(initial)
print(a)
#
# print(a.legalMoves(1))
#
# move = a.legalMoves()[0]

# if move[0] == 1:
#     lst = a.board[1] + a.plScore +


# print(a.result( (1,4)))
# print(a.result( (1,3)))
# print(a.result( (0,2)))
# print(a.result( (0,3)))
# print(a.result( (0,2)))
# print(a.result( (1,0)))
# print(a.result( (0,1)))
# print(a.result( (1,1)))

# result = a.result((1, 2))
# print(result[0])
# print(result[1])

# result = minimax(a, 4, 0)
# print("MINMAX RETURNED: ", result[0], result[1])
