import pprint
import random
import copy
from __builtin__ import False, True


def drawBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or
            (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or
            (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or
            (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or
            (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le))
    
def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-, mid-, low-, & L, M, R')
        number = input()
        if number == 7:
            move = 'top-L'
        elif number == 8:
            move = 'top-M'
        elif number == 9:
            move = 'top-R'
        elif number == 4:
            move = 'mid-L'
        elif number == 5:
            move = 'mid-M'
        elif number == 6:
            move = 'mid-R'
        elif number == 1:
            move = 'low-L'
        elif number == 2:
            move = 'low-M'
        elif number == 3:
            move = 'low-R'
            
    return move

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i
            
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
            
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None:
        return move
    
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'
    
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L', 'mid-R'])

def isBoardFull(board):
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Wuuhuu! Congratulations, you have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
                    
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Unfortunately you have lost. AI is superior!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
                    
    if not playAgain():
        break
                    

    