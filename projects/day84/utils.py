from random import choice

def __excel_col(n):
    s = ''
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def render_grid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    cells = [[str(c) for c in row] for row in grid]
    colnames = [__excel_col(i + 1) for i in range(cols)]
    maxc = max((len(c) for r in cells for c in r), default=1)
    maxl = max((len(l) for l in colnames), default=0)
    w = max(maxc, maxl)

    print( ' +' + '+'.join('-' * (w + 2) for _ in range(cols)) + '+')
    for i, row in enumerate(cells, 1):
        line =  ' ' + '|' + ''.join(' ' + c.center(w) + ' |' for c in row)
        print(line)
        print( ' +' + '+'.join('-' * (w + 2) for _ in range(cols)) + '+')

def alternate():
    switch = choice([1,0])
    while True:
        yield switch
        yield switch ^ 1

if '__main__' == __name__:
    render_grid([['','',''],['','',''],['','','']])
    render_grid([['X','X','X'],['O','O','O'],['O','X','']])

    alternator = alternate()
    print(next(alternator))
    print(alternator.__next__())

