import pygame
import sys
# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True

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

cross = pygame.image.load("XforTicTacToe.png")
cross = pygame.transform.scale(cross, (130, 130))

circle = pygame.image.load("Circle.png")
circle = pygame.transform.scale(circle, (170, 170))



def plotPhoto(turn, x, y):
    global duplicate
    duplicate = False
    piece = cross
    if (turn != True):
        piece = circle

    if x <= 166:
        col = 0
    elif x >= 166 and x <= 322:
        col = 1
    else:
        col = 2

    if y <= 160:
        row = 0
    elif y <= 322 and y >= 166:
        row = 1
    else:
        row = 2

    positions = [
        (0, 0, OneCrossPosition, OneCirclePosition),
        (1, 0, TwoCrossPosition, TwoCirclePosition),
        (2, 0, ThreeCrossPosition, ThreeCirclePosition),
        (0, 1, FourCrossPosition, FourCirclePosition),
        (1, 1, FiveCrossPosition, FiveCirclePosition),
        (2, 1, SixCrossPosition, SixCirclePosition),
        (0, 2, SevenCrossPosition, SevenCirclePosition),
        (1, 2, EightCrossPosition, EightCirclePosition),
        (2, 2, NineCrossPosition, NineCirclePosition)
    ]
    #pos = (col, row)
    for i in range(0, 9):
        if(positions[i][0] == col and positions[i][1] == row):
            break
    if resultArr[row][col] in ['x', 'o']:
        duplicate = True
    else:
        screen.blit(piece, positions[i][2] if piece == cross else positions[i][3])
        resultArr[row][col] = 'o' if piece == circle else 'x'


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





