import random

class Game2048:
    def __init__(self):
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.add_new_tile()
        self.add_new_tile()
    
    def display(self):
        for row in self.board:
            print("\t".join(str(num) if num != 0 else '.' for num in row))
        print()
    
    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2
    
    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row
    
    def merge(self, row):
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row
    
    def move_left(self):
        new_board = []
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)
            new_board.append(new_row)
        self.board = new_board
    
    def move_right(self):
        self.board = [list(reversed(row)) for row in self.board]
        self.move_left()
        self.board = [list(reversed(row)) for row in self.board]
    
    def move_up(self):
        self.board = list(map(list, zip(*self.board)))
        self.move_left()
        self.board = list(map(list, zip(*self.board)))
    
    def move_down(self):
        self.board = list(map(list, zip(*self.board)))
        self.move_right()
        self.board = list(map(list, zip(*self.board)))
    
    def make_move(self, direction):
        try:
            prev_board = [row[:] for row in self.board]
            if direction == 'a':
                self.move_left()
            elif direction == 'd':
                self.move_right()
            elif direction == 'w':
                self.move_up()
            elif direction == 's':
                self.move_down()
            
            if prev_board != self.board:
                self.add_new_tile()
                return True
            return False
        except Exception as e:
            print(f"An error occurred during movement: {e}")
            return False
    
    def is_won(self):
        return any(2048 in row for row in self.board)
    
    def is_game_over(self):
        for row in self.board:
            for i in range(self.size - 1):
                if row[i] == row[i + 1] or row[i] == 0:
                    return False
        for col in zip(*self.board):
            for i in range(self.size - 1):
                if col[i] == col[i + 1] or col[i] == 0:
                    return False
        return True