from chess_board import ChessBoard

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'
    
    def start_game(self):
        print("🎯 Добро пожаловать в консольные шахматы!")
        print("=========================================")
        print("♟️  Полная версия со всеми фигурами!")
        
        print("🎮 Игра началась! Белые ходят первыми.")
        print("📝 Формат хода: e2 e4 (откуда куда)")
        print("❌ Для выхода введите 'quit'")
        
        while True:
            self.board.display()
            print(f"Ход {'белых' if self.current_player == 'white' else 'черных'} ({self.current_player})")
            
            move = input("Ваш ход: ").strip().lower()
            
            if move == 'quit':
                print("Игра завершена.")
                break
            
            if not self.process_move(move):
                print("❌ Неверный ход! Попробуйте снова.")
                continue
            
            # Смена игрока
            self.current_player = 'black' if self.current_player == 'white' else 'white'
    
    def process_move(self, move_input):
        try:
            parts = move_input.split()
            if len(parts) != 2:
                return False
            
            from_pos = self.parse_position(parts[0])
            to_pos = self.parse_position(parts[1])
            
            if not from_pos or not to_pos:
                return False
            
            piece = self.board.get_piece(from_pos)
            if not piece or piece.color != self.current_player:
                return False
            
            # Проверка допустимости хода
            possible_moves = piece.get_possible_moves(self.board, from_pos)
            if to_pos not in possible_moves:
                return False
            
            # Выполнение хода
            return self.board.move_piece(from_pos, to_pos)
            
        except Exception as e:
            return False
    
    def parse_position(self, pos_str):
        if len(pos_str) != 2:
            return None
        
        col_char, row_char = pos_str[0], pos_str[1]
        
        if col_char not in 'abcdefgh' or row_char not in '12345678':
            return None
        
        col = ord(col_char) - ord('a')
        row = 8 - int(row_char)
        
        return (row, col)
    
    def is_checkmate(self):
        return False