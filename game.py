class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def play(self):
        # TODO: Implement main game logic
        pass

    def display_board(self):
        # TODO: Display game grid
        pass

    def make_move(self, column):
        # TODO: Place a token in the specified column
        pass

    def check_win(self):
        # TODO: Check if there's a winner
        pass

    def is_board_full(self):
        # TODO: Check if the grid is full
        pass

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_board_cell(self, row, col):
        return self.board[row][col]

    def get_current_player(self):
        return self.current_player