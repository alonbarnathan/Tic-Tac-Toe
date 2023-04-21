import pygame
import sys
# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True
dt = 0

w, h = 3, 3
resultArr = [['.' for x in range(w)] for y in range(h)]

global circleWin
global crossWin

circleWin = False
crossWin = False

#POSITIONS ON THE GRID FOR CROSS
OneCrossPosition = (20, 20)
TwoCrossPosition = (182, 20)
ThreeCrossPosition = (342, 20)

FourCrossPosition = (20, 180)
FiveCrossPosition = (182, 180)
SixCrossPosition = (342, 180)

SevenCrossPosition = (20, 340)
EightCrossPosition = (182, 340)
NineCrossPosition = (340, 340)

# POSITIONS ON THE GRID FOR CIRCLE
OneCirclePosition = (0, 0)
TwoCirclePosition = (162, 0)
ThreeCirclePosition = (324, 0)

FourCirclePosition = (0, 162)
FiveCirclePosition = (162, 162)
SixCirclePosition = (324, 162)

SevenCirclePosition = (0, 324)
EightCirclePosition = (162, 324)
NineCirclePosition = (324, 324)


def checkWin(resultArr):
    global crossWin
    global circleWin
    #left to right diagonal
    if all(resultArr[i][i] == 'x' for i in range(0, 3)) or all(resultArr[j][j] == 'o' for j in range(0, 3)):
        if (resultArr[0][0] == 'x'):
            crossWin = True
            return True
        else:

            circleWin = True
            return True
    # right to left diagonal
    if all(resultArr[i][2-i] == 'x' for i in range(0, 3)) or all(resultArr[j][2-j] == 'o' for j in range(0, 3)):
        if (resultArr[0][2] == 'x'):
            crossWin = True
            return True
        else:
            circleWin = True
            return True
    #Checking for a win in the rows
    for i in range(3):
        if all(resultArr[i][j] == 'x' for j in range(0, 3)) or all(resultArr[i][j] == 'o' for j in range(0, 3)):
            curr =resultArr[i][0]
            if (curr == 'x'):

                crossWin = True
                return True
            else:

                circleWin = True
                return True

    #checking for a win in the columns
    for i in range(3):
        if all(resultArr[j][i] == 'x' for j in range(0, 3)) or all(resultArr[j][i] == 'o' for j in range(0, 3)):
            curr = resultArr[0][i]
            if (curr == 'x'):
                crossWin = True
                return True
            else:
                circleWin = True
                return True


image_pos = None
screen.fill("white")
pygame.draw.rect(screen, "black", pygame.Rect(10, 166, 480, 6))
pygame.draw.rect(screen, "black", pygame.Rect(10, 322, 480, 6))

pygame.draw.rect(screen, "black", pygame.Rect(166, 10, 6, 480))
pygame.draw.rect(screen, "black", pygame.Rect(322, 10, 6, 480))

cross = pygame.image.load("/Users/alon2712/Desktop/XforTicTacToe.png")
cross = pygame.transform.scale(cross, (130, 130))

circle = pygame.image.load("/Users/alon2712/Desktop/Circle.png")
circle = pygame.transform.scale(circle, (170, 170))



def plotPhoto(turn, x, y):
    global duplicate
    duplicate = False
    piece = cross
    if (turn != True):
        piece = circle

    #top left
    if x <= 166 and y <= 160:
        if (resultArr[0][0] == 'x' or resultArr[0][0] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, OneCrossPosition if piece != circle else OneCirclePosition)
            if (piece == circle):
                resultArr[0][0] = 'o'
            else:
                resultArr[0][0] = 'x'

    #top middle
    if x >= 166 and x <= 322 and y <= 160:
        if (resultArr[0][1] == 'x' or resultArr[0][1] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, TwoCrossPosition if piece != circle else TwoCirclePosition)
            if (piece == circle):
                resultArr[0][1] = 'o'
            else:
                resultArr[0][1] = 'x'
    # top right
    if x >= 322 and y <= 160:
        if (resultArr[0][2] == 'x' or resultArr[0][2] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, ThreeCrossPosition if piece != circle else ThreeCirclePosition)
            if (piece == circle):
                resultArr[0][2] = 'o'
            else:
                resultArr[0][2] = 'x'
    # middle left
    if x <= 166 and y < 322 and y >= 166:
        if (resultArr[1][0] == 'x' or resultArr[1][0] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, FourCrossPosition if piece != circle else FourCirclePosition)
            if (piece == circle):
                resultArr[1][0] = 'o'
            else:
                resultArr[1][0] = 'x'
    # middle middle
    if x >= 166 and x <= 322 and y <= 322 and y >= 166:
        if (resultArr[1][1] == 'x' or resultArr[1][1] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, FiveCrossPosition if piece != circle else FiveCirclePosition)
            if (piece == circle):
                resultArr[1][1] = 'o'
            else:
                resultArr[1][1] = 'x'


    # middle right
    if x >= 322 and y <= 322 and y >= 166:
        if (resultArr[1][2] == 'x' or resultArr[1][2] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, SixCrossPosition if piece != circle else SixCirclePosition)
            if (piece == circle):
                resultArr[1][2] = 'o'
            else:
                resultArr[1][2] = 'x'


    # bottom left
    if x <= 166 and y >= 332:
        if (resultArr[2][0] == 'x' or resultArr[2][0] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, SevenCrossPosition if piece != circle else SevenCirclePosition)
            if (piece == circle):
                resultArr[2][0] = 'o'
            else:
                resultArr[2][0] = 'x'


    #bottom middle
    if x >= 166 and x < 322 and y >= 322:
        if (resultArr[2][1] == 'x' or resultArr[2][1] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, EightCrossPosition if piece != circle else EightCirclePosition)
            if (piece == circle):
                resultArr[2][1] = 'o'
            else:
                resultArr[2][1] = 'x'
    #bottom right
    if x >= 322 and y >= 322:
        if (resultArr[2][2] == 'x' or resultArr[2][2] == 'o'):
            duplicate = True
        else:
            screen.blit(piece, NineCrossPosition if piece != circle else NineCirclePosition)
            if (piece == circle):
                resultArr[2][2] = 'o'
            else:
                resultArr[2][2] = 'x'




pygame.display.set_caption("Text Demo")

# Create a font object
font = pygame.font.Font(None, 36)
winFont = pygame.font.Font(None, 80)


# Create a text surface
xText = font.render("It's X's turn", True, (255, 0, 0))
oText = font.render("It's o's turn", True, "blue")

xWins = winFont.render("X WINS !!!", True, "black")
oWins = winFont.render("o WINS !!!", True, "black")

def mainloop():
    xTurn = True
    while running:
        # poll for events

        # pygame.QUIT event means the user clicked X to close your window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.flip()

            # if (checkWin(resultArr) != True):
            if (xTurn):
                pygame.draw.rect(screen, "white", (180, 500, 150, 60))
                screen.blit(xText, (180, 500))
            else:
                pygame.draw.rect(screen, "white", (180, 500, 150, 60))
                screen.blit(oText, (180, 500))

            if pygame.mouse.get_pressed()[0]:

                # Get the position of the mouse cursor
                (x, y) = pygame.mouse.get_pos()
                plotPhoto(xTurn, x, y)


                if (duplicate):
                    xTurn = xTurn
                else:
                    xTurn = not xTurn

            if (checkWin(resultArr)):

                if (crossWin):

                    pygame.draw.rect(screen, "white", (180, 500, 150, 60))
                    pygame.draw.rect(screen, "dark gray", (45, 150, 400, 200))
                    screen.blit(xWins, (110, 220))

                elif (circleWin == True):
                    pygame.draw.rect(screen, "white", (180, 500, 150, 60))
                    pygame.draw.rect(screen, "dark gray", (45, 150, 400, 200))
                    screen.blit(oWins, (110, 220))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

mainloop()

pygame.quit()





