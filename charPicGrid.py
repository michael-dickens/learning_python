grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

grid2 = [
['.', '.', '0', '0', '.', '0','0','.','.'],
['.', '0', '0', '0', '0', '0', '0', '0','.'],
['.', '0', '0', '0', '0', '0', '0', '0','.'],
['.', '.', '0', '0', '0', '0', '0', '.', '.'],
['.', '.', '.', '0', '0', '0', '.', '.','.'],
['.', '.', '.', '.', '0', '.','.','.','.'],
]

def characterPictureGrid(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            print (g[i][j], end='')
        print('')

characterPictureGrid(grid)
characterPictureGrid(grid2)