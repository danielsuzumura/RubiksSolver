import random

class Rubik:
    # number of moves used in scramble
    MAX_RAND = 10

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
    moveName = ['U','Ui','F','Fi','R','Ri','B','Bi','L','Li','D','Di']

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
    
    # Rotate Back layer clockwise
    'B': [9,11,2,3,4,5,6,7,8,23,10,22,14,12,15,13,1,17,0,19,20,21,16,18],
    # Rotate Back layer counter clockwise
    'Bi': [18,16,2,3,4,5,6,7,8,0,10,1,13,15,12,14,22,17,23,19,20,21,11,9],
    
    # Rotate Left layer clockwise
    'L': [15,1,13,3,0,5,2,7,8,9,10,11,12,22,14,20,18,16,19,17,4,21,6,23],
    # Rotate Left layer counter clockwise
    'Li': [4,1,6,3,20,5,22,7,8,9,10,11,12,2,14,0,17,19,16,18,15,21,13,23],
    
    # Rotate Down layer clockwise
    'D': [0,1,2,3,4,5,10,11,8,9,14,15,12,13,18,19,16,17,6,7,21,23,20,22],
    # Rotate Down layer counter clockwise
    'Di': [0,1,2,3,4,5,18,19,8,9,6,7,12,13,10,11,16,17,14,15,22,20,23,21]
    }

    def __init__(self):
        self.createCube()

    def createCube(self):
        """
            Generate solved cube

        """
        for i in range(self.size):
            self.cube.append( self.colors[int(i/self.faceSize)])
    
    def printCube(self):
        """
            Print cube in console

        """
        for i,sizeName in enumerate(self.sizes):
            print(sizeName)
            for j in range(self.faceSize):
                if j % 3 == 2:
                    print()
                print(self.cube[j + i*self.faceSize], end = ' ')
            print()

    def applyMove(self, move):
        """
            Apply a move to cube
            
            Parameters:
                    move: Move using F(Front), U(Up), R(Right), B(Back), L(Left), D(Down) notation.
                    i after move indicates counter clockwise move

        """
        newCube = []
        for i in range(self.size):
            newCube.append(self.cube[self.moves[move][i]])
        self.cube = newCube
    
    def generateRandomScramble(self):
        """
            Generate a random scramble with MAX_RAND moves
    
            Returns:
                    List of moves
        """
        scramble = []
        for i in range(self.MAX_RAND):
            randMove = random.choice(self.moveName)
            self.applyMove(randMove)
            scramble.append(randMove)
        return scramble