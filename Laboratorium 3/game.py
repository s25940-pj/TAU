import random

class MoveError(Exception):
    pass

class BoardGame:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.board = [['.' for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.stop = None
        self.generate_start_and_stop()
        self.place_obstacles()

    def generate_start_and_stop(self):
        edges = [(i, 0) for i in range(self.rows)] + \
                [(i, self.cols - 1) for i in range(self.rows)] + \
                [(0, j) for j in range(self.cols)] + \
                [(self.rows - 1, j) for j in range(self.cols)]
        
        self.start = random.choice(edges)
        edges.remove(self.start)
        
        self.stop = random.choice(edges)
        # Prevents both starting points to be located next to each other
        while abs(self.start[0] - self.stop[0]) <= 1 and abs(self.start[1] - self.stop[1]) <= 1:
            self.stop = random.choice(edges)
        
        self.board[self.start[0]][self.start[1]] = 'A'
        self.board[self.stop[0]][self.stop[1]] = 'B'

    def place_obstacles(self, obstacle_count=5):        
        placed = 0
        while placed < obstacle_count:
            x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.board[x][y] == '.':
                self.board[x][y] = 'X'
                placed += 1

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_move_valid(self, x, y):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            raise MoveError(f"Move to ({x}, {y}) is out of bounds.")
        if self.board[x][y] == 'X':
            raise MoveError(f"Move to ({x}, {y}) is blocked by an obstacle.")
        if self.board[x][y] in ('A', 'B'):
            raise MoveError(f"Move to ({x}, {y}) targets an invalid position (START or STOP).")
        return True

    def move(self, position, direction):
        x, y = position
        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        if direction in moves:
            dx, dy = moves[direction]
            new_x, new_y = x + dx, y + dy
            if self.is_move_valid(new_x, new_y):
                return new_x, new_y
        # Move is not possible
        return x, y

game = BoardGame(6, 6)
game.display_board()

current_position = game.start
print(f"Starting at: {current_position}")

for direction in ["right", "down", "left", "up"]:
    print(f"Current direction: {direction}")
    try:
        new_position = game.move(current_position, direction)
        print(f"Moved {direction} to: {new_position}")
        current_position = new_position
    except MoveError as e:
        print(e)
        