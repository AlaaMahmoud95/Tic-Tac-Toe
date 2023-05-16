import numpy as np


class player():
    all = ['X', 'O']

    def __init__(self, pl, po):
        self.pl = pl
        self.po = po

    def pl_valid(self):
        """ Return [Bool, Str , Player , Postion] """
        if self.pl in player(self.pl, self.pl).all and type(self.po) is int and self.po <= 9:
            return True, 'Right Keep Focus', self.pl, self.po
        else:
            if self.pl not in player(self.pl, self.pl).all:
                return False, 'Its only \"X\" or \"O\"', self.pl, self.po
            elif type(self.po) is not int:
                return False, 'Postion is numerical', self.pl, self.po
            elif self.po > 9:
                return False, 'Board has only 9 Squares ', self.pl, self.po
            else:
                return False, 'Wrong Player or Movement', self.pl, self.po


class pad():

    def __init__(self):
        self.board = np.array(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
        self.moves = np.array([])

    def cur_game(self):
        """ Print Current Game Stage """
        self.cu_board = f"""{self.board[0]} | {self.board[1]} | {self.board[2]}\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n{self.board[6]} | {self.board[7]} | {self.board[8]}"""
        print(f'\n{self.cu_board}\n')

    def wr_move(self, last, loc):
        """Check Movement Right , overlapping or Wrong """
        if len(self.moves) == 0:
            self.moves = np.append(self.moves, last)
            self.board[loc-1] = last
            return self.moves, 'Next Move'
        else:
            if len(self.moves) == 9:
                return 'Draw', False
            elif self.moves[-1] != last and len(self.moves) < 9 and self.board[loc-1] not in player(last, loc).all and len(self.moves) != 9:
                self.moves = np.append(self.moves, last)
                self.board[loc-1] = last
                print('\nNext Move')
                return 'Next Move', True
            elif self.board[loc-1] in player(last, loc).all:
                print('\nSquare is Token')
                return 'Square is Token', False
            else:
                print(f'\nWrong Move {self.moves}\n')
                return f'Wrong Move {self.moves}', False

    def Winner(self):
        """Create Filter to Check Win , Draw"""
        x = [0, 1, 2]
        y = [0, 3, 6]

        def winx(w):
            c = [d+3 for d in w]
            return c

        def winy(w):
            c = [d+1 for d in w]
            return c
        u = [x, winx(x), winx(winx(x)), y, winy(
            y), winy(winy(y)), [0, 4, 8], [2, 4, 6]]
        for nn in u:
            if len(self.moves) >= 3 and len(self.moves) <= 9:
                if self.board[nn[0]] == self.board[nn[1]] == self.board[nn[2]] != '_':
                    won = self.board[nn[0]]
                    return ['Winner', won, f" {won} ".center(7, '\6'), " You Won The Game"]
        else:
            if len(self.moves) == 9:
                return ['Draw', len(self.moves)]
            elif len(self.moves) < 4:
                return [f'Game is in Early Stage only {len(self.moves)}', len(self.moves)]
            else:
                return ['No Winner Yet', len(self.moves)]

    def Ex(self, ex, el):
        """To Quit Game"""
        if ex == 'F' and el == 0:
            print('\tExit,See U Soon\t'.center(30, '\4'))
            return True


pd = pad()


def XO():
    """Game Function gets input for player letter and location"""
    if pd.Winner()[0] not in ['Winner', 'Draw']:
        al = np.array(
            input(f"Lets Play ... \n['{player.all}', '[1:9]' ]\t").upper().split(','))
        ply = player(al[0], int(al[1]))
        out = pd.Ex(ply.pl, ply.po)
        while len(pd.moves) <= 8:
            if ply.pl_valid()[0]:
                pd.wr_move(ply.pl, ply.po)
                pd.cur_game()
                pd.Winner()
                print('\n[F,0] To Exit')
                return pd.Winner()[0], XO(), pd.moves
            elif out:
                break
            else:
                print(ply.pl_valid()[1])
                XO()
        else:
            print(pd.Winner())
    else:
        print(f" {pd.Winner()[2]}  {pd.Winner()[3]}")


XO()
