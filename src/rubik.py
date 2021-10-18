import random

# number of moves used in scramble
MAX_RAND = 100

# total amount of squares in face
faceSize = 4

# total amount of squares in cube
size = 24

# color in every square
cube = []

# all the colors
colors = ['y','g','o','b','r','w']

# all the sizes
sizes = ['Up', 'Front', 'Right', 'Back', 'Left', 'Down']

# list of moves possible
moveName = ['U','Ui','F','Fi','R','Ri']

# Stores how the pieces will move with every possible move
moves = {
# Rotate Up layer clockwise
'U': [2,0,3,1,8,9,6,7,12,13,10,11,16,17,14,15,4,5,18,19,20,21,22,23],
# Rotate Up layer counter clockwise
'Ui': [1,3,0,2,16,17,6,7,4,5,10,11,8,9,14,15,12,13,18,19,20,21,22,23],

# Rotate Front layer clockwise
'F': [0,1,19,17,6,4,7,5,2,9,3,11,12,13,14,15,16,20,18,21,10,8,22,23],
# Rotate Up layer counter clockwise
'Fi': [0,1,8,10,5,7,4,6,21,9,20,11,12,13,14,15,16,3,18,2,17,19,22,23],

# Rotate Right layer clockwise
'R': [0,5,2,7,4,21,6,23,10,8,11,9,3,13,1,15,16,17,18,19,20,14,22,12],
# Rotate Right layer counter clockwise
'Ri': [0,14,2,12,4,1,6,3,9,11,8,10,23,13,21,15,16,17,18,19,20,5,22,7],
}

def createCube():
    """
        Generate solved cube
    """
    cube = []
    for i in range(size):
        cube.append( colors[int(i/faceSize)])
    return tuple(cube)

def printCube(cube):
    """
        Print cube in console
    """
    for i,sizeName in enumerate(sizes):
        print(sizeName)
        for j in range(faceSize):
            if j % 3 == 2:
                print()
            print(cube[j + i*faceSize], end = ' ')
        print()

def applyMove(cube, move):
    """
        Apply a move to cube
        
        Parameters:
                move: Move using F(Front), U(Up), R(Right), B(Back), L(Left), D(Down) notation.
                i after move indicates counter clockwise move
        Returns:
                Cube after move
    """
    newCube = []
    for i in range(size):
        newCube.append(cube[moves[move][i]])
    return tuple(newCube)

def generateRandomScramble():
    """
        Generate a random scramble with MAX_RAND moves

        Returns:
                List of moves
    """
    scramble = []
    for i in range(MAX_RAND):
        randMove = random.choice(moveName)
        scramble.append(randMove)
    return scramble

def applyScramble(cube, scramble):
    """
        Apply list of moves

        Returns:
                Cube after moves
    """
    for move in scramble:
        cube = applyMove(cube, move)
    return tuple(cube)

def isSolved(cube):
    for i,sizeName in enumerate(sizes):
        color = cube[i*faceSize]
        for j in range(faceSize):
            if cube[j + i*faceSize] != color:
                return False
    return True

def inverseMove(move):
    if 'i' in move:
        return move[0]
    else:
        return move + 'i'