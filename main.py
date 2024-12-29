def create_board():
    x = 8
    y = 8
    board = {}
    for i in range(1, x+1):
        for j in range(1, y+1):
            square = (i, j)
            if j == 2:
                board[square] = "wp"  # White pawns on row 2
            elif j == 1:
                # White pieces row
                if i == 1 or i == 8:
                    board[square] = "wR"  # Rooks
                elif i == 2 or i == 7:
                    board[square] = "wN"  # Knights
                elif i == 3 or i == 6:
                    board[square] = "wB"  # Bishops
                elif i == 4:
                    board[square] = "wQ"  # Queen
                elif i == 5:
                    board[square] = "wK"  # King
            elif j == 7:
                board[square] = "bp"  # Black pawns on row 7
            elif j == 8:
                # Black pieces row
                if i == 1 or i == 8:
                    board[square] = "bR"  # Rooks
                elif i == 2 or i == 7:
                    board[square] = "bN"  # Knights
                elif i == 3 or i == 6:
                    board[square] = "bB"  # Bishops
                elif i == 4:
                    board[square] = "bQ"  # Queen
                elif i == 5:
                    board[square] = "bK"  # King
            else:
                board[square] = 0  # Empty square
    
    return board

class Piece:
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, pos, board):

        raise NotImplementedError("This method should be implemented by subclasses")
        
class Pawn(Piece):
    def get_valid_moves(self, pos, board):
        moves = []
        row, col = pos[0], pos[1]

        if self.color == 'w':
            # Move up one square
            if board.get((row, col+1)) == 0:
                moves.append((row, col+1))
            # Move two squares if on starting square
            if board.get((row, col+2)) == 0 and col == 2:
                moves.append((row, col+2))
            # Diagonally take
            if (row + 1, col + 1) in board and str(board.get((row + 1, col + 1), ''))[0] == 'b':
                moves.append((row + 1, col + 1))
            if (row - 1, col + 1) in board and  str(board.get((row - 1, col + 1), ''))[0] == 'b':
                moves.append((row - 1, col + 1))
        else:
            # Move up one square
            if board.get((row, col - 1)) == 0:
                moves.append((row, col - 1))
            # Move two squares if on starting square
            if board.get((row, col - 2)) == 0 and col == 7:
                moves.append((row, col - 2))
            # Diagonally take
            if (row + 1, col - 1) in board and str(board.get((row + 1, col - 1), ''))[0] == 'b':
                moves.append((row + 1, col - 1))
            if (row - 1, col - 1) in board and  str(board.get((row - 1, col - 1), ''))[0] == 'b':
                moves.append((row - 1, col - 1))            

        return moves

class Rooks(Piece):
    def get_valid_moves(self, pos, board):
        def tranverse_direction(delta_row, delta_col):
            row, col = pos[0], pos[1]
            while True:
                row += delta_row
                col += delta_col
                if (row, col) not in board:
                    break
                if board[(row, col)] == 0:
                    moves.append((row, col))
                elif board[(row, col)][0] != self.color:
                    moves.append((row, col))
                    break
                else:
                    break

        moves = []

        tranverse_direction(1,0) # up
        tranverse_direction(-1, 0) # down
        tranverse_direction(0, 1) # right
        tranverse_direction(0, -1) # left       

        return moves


class Knights(Piece):
        def get_valid_moves(self, pos, board):
            moves = []
            row, col = pos[0], pos[1]

            if self.color == 'w':
                return

class Bishop(Piece):
        def get_valid_moves(self, pos, board):
            moves = []
            row, col = pos[0], pos[1]

class Queen(Piece):
        def get_valid_moves(self, pos, board):
            moves = []
            row, col = pos[0], pos[1]

class King(Piece):
        def get_valid_moves(self, pos, board):
            moves = []
            row, col = pos[0], pos[1]



board = create_board()

#pawn = Pawn('b')

rook = Rooks('w')

moves = rook.get_valid_moves((4,4), board)

print(board)
print(moves)

