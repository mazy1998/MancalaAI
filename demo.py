from p5 import *

from gameClasses import *

pots = []
turn = 1
gameOver = False
mouseIndex = 0
pebblePosVar = 20
baseSeed = 0
winner = 0

# index 6 of board is AI score i.e LHS and index 13 is P1 score i.e. RHS
def setup():
    size(1000, 300)
    # frameRate(30)
    title("Mancala AI")
    baseSeed = random_uniform(100)

    board = convert_state([a.aiScore,a.plScore,a.board])
    # Initializing pots.
    for i in range(14):

        if i < 7:
            print(i)
            pots.append(Pots(i, 6 - i, 0, board[i]))
        else:
            pots.append(Pots(i, i - 6, 1, board[i]))
    for i in range(14):
        pots[i].update()
    print(pots)
    print("-=:SETUP COMPLETE:=-")


def draw():
    background(108, 91, 123)
    global gameOver
    global turn
    global mouseIndex
    global baseSeed
    global winner
    
    # background(108,91,123)
    background(53, 92, 125)
    pebbleSum = 0
    
    board = convert_state([a.aiScore,a.plScore,a.board])
    # # updating pots and drawing pebbles
    for i in range(14):
        pots[i].count = board[i]
        pots[i].update()
        pebbleSum += pots[i].count

        # if our pot
        if pots[i].isBig and pots[i].index == 6:
            drawPebbles(pots[i].index * baseSeed, pots[i].count, pots[i].x + 50, pots[i].y + 100, True, False)
    #     # if opponent pot
        elif pots[i].isBig and pots[i].index == 13:
            drawPebbles(pots[i].index * baseSeed, pots[i].count, pots[i].x + 50, pots[i].y + 0, True, False)
    #     # other pots
        else:
            drawPebbles(pots[i].index * baseSeed, pots[i].count, pots[i].x + 50, pots[i].y + 50, False, False)

    # pebbleSUM allows us to check that the number of pebbles is what it should be
    if pebbleSum != 48:
        print("MANUAL ERROR: Uneven sum of pebbles: {}".format(pebbleSum))

    namecards()
        # black outline
    no_fill()
    stroke(0)
    stroke_weight(4)
    rect((90, 50), 820, 200)

    if gameOver:
        # print("Game Over")
        if (a.aiScore < a.plScore):
            winner = 1
        elif (a.aiScore > a.plScore):
            winner = 2
        else:
            winner = 0
        endgame(winner)
    else:
        # Highlighting cursor
        if (not pots[mouseIndex].isBig and pots[mouseIndex].indexY == turn and not gameOver):
            no_fill()
            stroke_weight(6)
            rect((pots[mouseIndex].x - 3, pots[mouseIndex].y - 3), 106, 106)
        
        # Checks to see if game is over
        gameOver = a.isTerminal()
        
#        p1 = 0
#        p2 = 0
#        for i in range(6):
#            p1 += pots[i + 7].count
#            p2 += pots[i].count
#
#        if (p1 == 0 or p2 == 0) and not gameOver:
#            gameOver = True
#            a.plScore += p1
#            a.aiScore += p2
#            a.board = np.zeros((2,6)).astype(int)
#            print("The AI score is {}, the Player score is {}".format(a.aiScore,a.plScore))



class Pots():

    def __init__(self, index, x, y, count=4):
        self.index = index
        self.indexX = x
        self.indexY = y

        # coordinates on screen
        self.x = x * 100 + 100
        self.y = y * 100 + 50
        self.count = count
        self.isBig = False

        if self.index == 6 or self.index == 13:
            self.isBig = True
        self.mouseHover = False
        print("Pot created at {}:{} with index {}".format(self.x, self.y, self.index))

    def update(self):
        global mouseIndex
        if mouse_x > self.x and mouse_x < self.x + 100 and mouse_y < self.y + 100 and mouse_y > self.y and not self.isBig:
            self.mouseHover = True
        elif mouse_x < self.x + 100 and mouse_x > self.x and mouse_y < self.y + 200 and mouse_y > self.y and self.index == 6:
            self.mouseHover = True
        elif mouse_x < self.x + 100 and mouse_x > self.x and mouse_y < self.y + 100 and mouse_y > self.y - 100 and self.index == 13:
            self.mouseHover = True
        else:
            self.mouseHover = False
        if self.mouseHover:
            mouseIndex = self.index
        self.create_pot()

    def create_pot(self):
        if not self.isBig:

            fill(108, 91, 123)
            # fill(192,108,132)
            no_stroke()
            rect((self.x, self.y), 100, 100)

            no_stroke()
            # fill(53,92,125)
            fill(192, 108, 132)
            ellipse((self.x + 50, self.y + 50), 80, 80)

        elif self.index == 6:
            None
            fill(108, 91, 123)
            no_stroke()
            rect((self.x - 10, self.y), 110, 200)

            no_stroke()
            fill(192, 108, 132)
            rect((self.x + 10, self.y + 10), 80, 180)

        elif self.index == 13:

            fill(108, 91, 123)
            no_stroke()
            rect((self.x, self.y - 100), 110, 200)

            no_stroke()
            fill(192, 108, 132)
            rect((self.x + 10, self.y - 90), 80, 180)

        if (self.index == 6):

            no_stroke()
            fill(192, 108, 132)
            ellipse((self.x - 28, self.y + 100), 40, 40)

            fill(0)
            no_stroke()
            #text_size(5)
            text_align("CENTER","CENTER")
            text(str(self.count), (self.x - 28, self.y + 100))

        elif (self.index == 13):
            no_stroke()
            fill(192, 108, 132)
            ellipse((self.x + 128, self.y), 40, 40)

            fill(0)
            no_stroke()
            #text_size(25)
            text_align("CENTER","CENTER")
            text(str(self.count), (self.x + 128, self.y))
        elif (self.indexY == 0):
            no_stroke()
            fill(192, 108, 132)
            ellipse((self.x + 50, self.y - 18), 30, 30)

            fill(0)
            no_stroke()
            # text_size(25)
            text_align("CENTER", "BOTTOM")
            text(str(self.count), (self.x + 50, self.y - 5))

        elif (self.indexY == 1):
            no_stroke()
            fill(192, 108, 132)
            ellipse((self.x + 50, self.y + 118), 30, 30)

            fill(0)
            no_stroke()
            # text_size(25)
            text_align("CENTER","TOP")
            text(str(self.count), (self.x + 50, self.y + 105))


def drawPebbles(seed, count, x, y, isBig, isHand):
    global pebblePosVar
    stroke(0)
    stroke_weight(4)
    fill(53, 92, 125)
    random_seed(seed)
    for i in range(count):
        if ((i + floor(seed)) % 4 == 0):

            xVar = random_uniform(5, pebblePosVar)
            yVar = random_uniform(-pebblePosVar, -5)

        elif ((i + floor(seed)) % 4 == 1):

            xVar = random_uniform(5, pebblePosVar)
            yVar = random_uniform(5, pebblePosVar)
        elif ((i + floor(seed)) % 4 == 2):

            xVar = random_uniform(-pebblePosVar, -5)
            yVar = random_uniform(5, pebblePosVar)
        elif ((i + floor(seed)) % 4 == 3):

            xVar = random_uniform(-pebblePosVar, -5)
            yVar = random_uniform(-pebblePosVar, -5)

        if (isBig):
            yVar = yVar * 3
        if (isHand):
            ellipse((x + xVar, y + yVar), 35, 35)
        else:
            ellipse((x + xVar, y + yVar), 30, 30)


indexmap = {0: (0, 5), 1: (0, 4), 2: (0, 3), 3: (0, 2), 4: (0, 1), 5: (0, 0),
            7: (1, 0), 8: (1, 1), 9: (1, 2), 10: (1, 3), 11: (1, 4), 12: (1, 5)}


def mouse_pressed():
    """
    I should call the function result and then update the pots accordingly
    """
    global indexmap
    global mouseIndex
    global winner
    global gameOver
    global turn
    global a
    print(mouseIndex)
    if mouseIndex != 6 and mouseIndex != 13:
        move = indexmap[mouseIndex]
        if turn == move[0] and pots[mouseIndex].count != 0:
            print("Valid move")

            result = a.result(move)
            a = result[0]
            # board = convert_state([a.aiScore, a.plScore, a.board])
#            print(result[0].board)
            board = convert_state([result[0].aiScore, result[0].plScore, result[0].board])
            print(board)
            print("AI score is {}".format(result[0].aiScore))
            print("P1 score is {}".format(result[0].plScore))
            for i in range(14):
                pots[i].count = board[i]
            if result[1] == False:
                turn = int(not(turn))
                if turn == 1:
                    print("Player 1 turn")
                else:
                    print("AI/Player 2 turn")
                
            
                
                
    

        else:
            """
            This needs to change so that it works correctly for AI
            """
            print("Invalid Move")


    # if mouseIndex == 2:
    #
    #     for i in range(pots[mouseIndex].count):
    #         pots[mouseIndex + i + 1].count += 1
    #     pots[mouseIndex].count = 0
    #     winner = 1
    #     gameOver = True


def convert_state(s):

    temp = list(s[2].flatten())
#    print(temp[0:6])
    temp[0:6] = temp[0:6][::-1]
    # player on right
    temp.insert(6, s[0])
    # player on left
    temp.append(s[1])
    return temp


def namecards():
    fill(192, 108, 132)
    stroke(0)
    stroke_weight(5)
    rect((0, -15), 125, 45)
    rect((width - 125, -15), 125, 45)

    fill(0)
    no_stroke()
    # text_size(25)
    text_align("CENTER", "TOP")
    text("Player 2", (125 / 2, 1))
    text("Player 1", (width - (125 / 2), 1))


def endgame(winner):
    if (winner == 1):

        stroke(0)
        stroke_weight(5)
        fill(248, 177, 149)
        rect(((width / 2) - 150, (height / 2) - 37.5), 300,75)

        fill(0)
        no_stroke()
        # text_size(45)
        text_align("CENTER", "CENTER")
        text("Player 1 Wins!", (width / 2, height / 2))

    elif (winner == 2):
        stroke(0)
        stroke_weight(5)
        fill(248, 177, 149)
        rect(((width / 2) - 150, (height / 2) - 37.5), 300, 75)

        fill(0)
        no_stroke()
        # text_size(45)
        text_align("CENTER", "CENTER")
        text("Player 2/ AI Wins!", (width / 2, height / 2))
    else:

        stroke(0)
        stroke_weight(5)
        fill(248, 177, 149)
        rect(((width / 2) - 75, (height / 2) - 37.5), 150,75)

        fill(0)
        no_stroke()
        # text_size(55)
        text_align("CENTER", "CENTER")
        text("Tie!", (width / 2, height / 2))


run()
