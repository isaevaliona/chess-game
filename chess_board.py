from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
    
    def setup_board(self):
        # Расстановка пешек
        for col in range(8):
            self.board[1][col] = Pawn('black')
            self.board[6][col] = Pawn('white')
        
        # Ладьи
        self.board[0][0] = Rook('black')
        self.board[0][7] = Rook('black')
        self.board[7][0] = Rook('white')
        self.board[7][7] = Rook('white')
        
        # Кони
        self.board[0][1] = Knight('black')
        self.board[0][6] = Knight('black')
        self.board[7][1] = Knight('white')
        self.board[7][6] = Knight('white')
        
        # Слоны
        self.board[0][2] = Bishop('black')
        self.board[0][5] = Bishop('black')
        self.board[7][2] = Bishop('white')
        self.board[7][5] = Bishop('white')
        
        # Ферзи
        self.board[0][3] = Queen('black')
        self.board[7][3] = Queen('white')
        
        # Короли
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')
    
    def display(self):
        print("\n   a b c d e f g h")
        print("  +-----------------+")
        for row in range(8):
            print(f"{8 - row} |", end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    print(piece, end=" ")
                else:
                    print(".", end=" ")
            print(f"| {8 - row}")
        print("  +-----------------+")
        print("   a b c d e f g h\n")
    
    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8
    
    def is_empty(self, position):
        x, y = position
        return self.is_valid_position(position) and self.board[x][y] is None
    
    def is_opponent(self, position, color):
        x, y = position
        return (self.is_valid_position(position) and 
                self.board[x][y] is not None and 
                self.board[x][y].color != color)
    
    def is_ally(self, position, color):
        x, y = position
        return (self.is_valid_position(position) and 
                self.board[x][y] is not None and 
                self.board[x][y].color == color)
    
    def move_piece(self, from_pos, to_pos):
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        
        piece = self.board[from_x][from_y]
        if piece:
            self.board[to_x][to_y] = piece
            self.board[from_x][from_y] = None
            piece.has_moved = True
            return True
        return False
    
    def get_piece(self, position):
        x, y = position
        return self.board[x][y] if self.is_valid_position(position) else None