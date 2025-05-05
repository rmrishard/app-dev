# File: game.py
#Name : Rishard Mohamed
#Student Number : 2495235

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'




    def play(self):
        while True:
            self.display_board()

            try:
                col = int(input(f"Player {self.current_player}, choose column (0–6): "))
            except ValueError:
                print("Enter a number between 0 and 6.")
                continue

            if not self.make_move(col):
                print("Invalid move. Try again.")
                continue

            #check if there is a winner
            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check if its draw
            if self.is_board_full():
                self.display_board()
                print("It's a draw!")
                break
            #switch players
            self.switch_player()





            #creating the board

    def display_board(self):
        print(' ' + ' '.join(str(i) for i in range(len(self.board[0]))))
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print()

    def make_move(self, column):
        if column < 0 or column >= len(self.board[0]):
            return False

            #check botton row
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True

            #if column is full
        return False








    def check_win(self):
        P = self.current_player
        rows = len(self.board)
        cols = len(self.board[0])

        #check for win horizontal
        for row in range(rows):
            for col in range(cols - 3):
                if all(self.board[row][col + i] == P for i in range(4)):
                    return True

        #check for win  vertical
        for col in range(cols):
            for row in range(rows - 3):
                if all(self.board[row + i][col] == P for i in range(4)):
                    return True

        #check for win diagonal down right
        for row in range(rows - 3):
            for col in range(cols - 3):
                if all(self.board[row + i][col + i] == P for i in range(4)):
                    return True

        #check for win diagonal up right
        for row in range(3, rows):
            for col in range(cols - 3):
                if all(self.board[row - i][col + i] == P for i in range(4)):
                    return True
        return False



    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_board_cell(self, row, col):
        return self.board[row][col]

    def get_current_player(self):
        return self.current_player