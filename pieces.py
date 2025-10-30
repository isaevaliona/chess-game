class Piece:
    def __init__(self, color, symbol):
        self.color = color  # 'white' или 'black'
        self.symbol = symbol
        self.has_moved = False
    
    def __str__(self):
        return self.symbol
    
    def get_possible_moves(self, board, position):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

class Pawn(Piece):
    def __init__(self, color):
        symbol = '♙' if color == 'white' else '♟'
        super().__init__(color, symbol)
    
    def get_possible_moves(self, board, position):
        moves = []
        x, y = position
        direction = -1 if self.color == 'white' else 1
        
        # Ход вперед
        if board.is_empty((x + direction, y)):
            moves.append((x + direction, y))
            # Двойной ход с начальной позиции
            if not self.has_moved and board.is_empty((x + 2 * direction, y)):
                moves.append((x + 2 * direction, y))
        
        # Взятие по диагонали
        for dy in [-1, 1]:
            capture_pos = (x + direction, y + dy)
            if board.is_valid_position(capture_pos) and board.is_opponent(capture_pos, self.color):
                moves.append(capture_pos)
        
        return moves

class Rook(Piece):
    def __init__(self, color):
        symbol = '♖' if color == 'white' else '♜'
        super().__init__(color, symbol)
    
    def get_possible_moves(self, board, position):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:
            for i in range(1, 8):
                new_pos = (position[0] + dx * i, position[1] + dy * i)
                if not board.is_valid_position(new_pos):
                    break
                if board.is_empty(new_pos):
                    moves.append(new_pos)
                elif board.is_opponent(new_pos, self.color):
                    moves.append(new_pos)
                    break
                else:
                    break
        return moves

class Knight(Piece):
    def __init__(self, color):
        symbol = '♘' if color == 'white' else '♞'
        super().__init__(color, symbol)
    
    def get_possible_moves(self, board, position):
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for dx, dy in knight_moves:
            new_pos = (position[0] + dx, position[1] + dy)
            if board.is_valid_position(new_pos) and not board.is_ally(new_pos, self.color):
                moves.append(new_pos)
        
        return moves

class King(Piece):
    def __init__(self, color):
        symbol = '♔' if color == 'white' else '♚'
        super().__init__(color, symbol)
    
    def get_possible_moves(self, board, position):
        moves = []
        king_moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        for dx, dy in king_moves:
            new_pos = (position[0] + dx, position[1] + dy)
            if board.is_valid_position(new_pos) and not board.is_ally(new_pos, self.color):
                moves.append(new_pos)
        
        return moves