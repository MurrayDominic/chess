def create_board():
    x = 9
    y = 9
    board = {}
    for i in range(1, x):
        for j in range(1, y):
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
        moves = []
        row, col = pos[0], pos[1]

        if self.color == 'w':
        # Move forward
            for i in range(col+1, 9):
                if board.get((row, i)) == 0:
                    moves.append((row, i))
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'b':
                    moves.append((row, i))
                    break
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'w':
                    break               
        # Move backward
            for i in range(col-1, 0, -1):
                if board.get((row, i)) == 0:
                    moves.append((row, i))
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'b':
                    moves.append((row, i))
                    break
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'w':
                    break    
        # Move right
            for i in range(row+1, 9):
                if board.get((i, col)) == 0:
                    moves.append(( i, col))
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'b':
                    moves.append((i, col))
                    break
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'w':
                    break               
        # Move left
            for i in range(row-1, 0, -1):
                if board.get((i, col)) == 0:
                    moves.append(( i, col))
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'b':
                    moves.append((i, col))
                    break
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'w':
                    break   
        
        else:
      # Move forward
            for i in range(col+1, 9):
                if board.get((row, i)) == 0:
                    moves.append((row, i))
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'w':
                    moves.append((row, i))
                    break
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'b':
                    break               
        # Move backward
            for i in range(col-1, 0, -1):
                if board.get((row, i)) == 0:
                    moves.append((row, i))
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'w':
                    moves.append((row, i))
                    break
                if (row, i) in board and str(board.get((row, i), ''))[0] == 'b':
                    break    
        # Move right
            for i in range(row+1, 9):
                if board.get((i, col)) == 0:
                    moves.append(( i, col))
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'w':
                    moves.append((i, col))
                    break
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'b':
                    break               
        # Move left
            for i in range(row-1, 0, -1):
                if board.get((i, col)) == 0:
                    moves.append(( i, col))
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'w':
                    moves.append((i, col))
                    break
                if (i, col) in board and str(board.get((i, col), ''))[0] == 'b':
                    break   


        return moves


class Knights(Piece):
        def get_valid_moves(self, pos, board):
            moves = []
            row, col = pos[0], pos[1]

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