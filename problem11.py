def check_direction(grid, i, j, dir = "up", reach = 4):
    product = grid[i][j]
    for x in range(1,reach):
        if dir == "up" and i-x >= 0:
            product *= grid[i-x][j]
        elif dir == "down" and i+x < len(grid):
            product *= grid[i+x][j]
        elif dir == "left" and j-x >= 0:
            product *= grid[i][j-x]
        elif dir == "right" and j+x < len(grid[i]):
            product *= grid[i][j+x]
        elif dir == "diag_left" and i-x >= 0 and j-x >= 0:
            product *= grid[i-x][j-x]
        elif dir == "diag_right" and i-x >= 0 and j+x < len(grid[i]):
            product *= grid[i-x][j+x]
    return product

txt = open("problem11grid.txt", 'r')
grid = [list(map(int,line.rstrip('\n').split(' '))) for line in txt]
products = []
for i, line in enumerate(grid):
    for j, num in enumerate(line):
        for dir in ["up", "down", "left", "right", "diag_left", "diag_right"]:
            products.append((i,j,dir,check_direction(grid, i, j, dir)))

print("Maximum = {}".format(max(products,key=lambda item:item[3])))
