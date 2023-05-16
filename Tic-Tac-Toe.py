xo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
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


def ww(p, w):
    for nn in u:
        if len(p) >= 3:
            if w[nn[0]] == w[nn[1]] == w[nn[2]]:
                aa = w[nn[0]]
                return ['Winner', aa]
        else:
            return [f'Game is in Early Stage only {len(p)} Squares Token ', len(p)]
    else:
        return ['No Winner Yet', len(p)]


def gg():
    """ XO Game
    Input = "X" or "O"
    Output = "Your Turn" or "Winner" or "Draw" or "Exit"
     """
    b = ['X', 'O', 'F', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rxo = f"""{xo[0]} | {xo[1]} | {xo[2]}
{xo[3]} | {xo[4]} | {xo[5]}
{xo[6]} | {xo[7]} | {xo[8]}"""
    ww(a, xo)
    print(rxo)
    if ww(a, xo)[0] == 'Winner':
        print(f'{rxo}' + '\n'+f'The Winner is \6 {ww(a,xo)[1]} \6')
        pass
    else:
        inp = input(
            'Make Your Move as   letter,location ?').strip().upper().split(',')
        if len(inp) == 2 and inp[0] in b and 0 < int(inp[1]) <= 9 and type(xo[int(inp[1])-1]) != str:
            while len(a) != 0 and len(a) < 8:
                if inp[0] == 'F':
                    print(f'{ww(a, xo)[0]}'+'\n'+'Exit')
                    break
                elif ww(a, xo)[0] == "Winner":
                    print(f'{rxo}' + '\n'+f'The Winner is \6{ww(a,xo)[1]}\6')
                elif a[-1] != inp[0]:
                    a.append(inp[0])
                    xo[int(inp[1])-1] = inp[0]
                    ww(a, xo)
                    print(f'{ww(a, xo)[0]}')
                    return gg()
                else:
                    return print(f"Worng Sellection last player was \'{a[-1]}\' "), gg()
            else:
                if inp[0] != 'F' and len(a) == 0:
                    a.append(inp[0])
                    xo[int(inp[1])-1] = inp[0]
                    ww(a, xo)
                    print(f'{ww(a, xo)[0]}')
                    return gg()
                elif inp[0] == "F":
                    print(f"{rxo} \n Exit")
                elif len(a) == 8:
                    a.append(inp[0])
                    xo[int(inp[1])-1] = inp[0]
                    ww(a, xo)
                    if ww(a, xo)[0] == "Winner":
                        print(f'{rxo}' + '\n' +
                              f'The Winner is \6{ww(a,xo)[1]}\6')
                    else:
                        print(f'{rxo}'+'\n'+'Draw')
                else:
                    print(f'{rxo}'+'\n'+'Draw')
        else:
            if inp[0] == 'F':
                print(f"{rxo} \n Exit ")
            elif len(inp) < 2:
                print(f"Missing input {inp} Should be ['X'or'O','num'] ")
                return gg()
            elif inp[0] not in b or int(inp[1]) > 9 or int(inp[1]) == 0:
                print(
                    f"Its only [ 'X' or 'O' , '1:9' ] Your input [ {inp[0]} , {inp[1]} ]to play and \"F\" to Exit".title())
                return gg()
            elif type(xo[int(inp[1])-1]) == str:
                print('Token Square!')
                return gg()
            else:
                print(f"Something Wrong in your input you input is {inp} ")
                return gg()


gg()
