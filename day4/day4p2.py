def find_adjacent_tiles(grid, x_idx, y_idx, width, height, condition_adjacent=lambda a,x,y:True, condition_tile=lambda a,x,y:True):
    if not condition_tile(grid, x_idx, y_idx):
        return None 
    adjacent_tiles = []
    for y in range(y_idx-1, y_idx+2):
        for x in range(x_idx-1, x_idx+2):
            if (x == x_idx and y == y_idx) or x < 0 or y < 0 or x >= width or y >= height:
                continue

            if condition_adjacent(grid, x, y):
                adjacent_tiles.append(grid[y][x])
    return adjacent_tiles


input_lines = []
with open("input.txt", "r") as f:
    for line in f:
        input_lines.append(line.strip())

total_forklift = 0
running = True
while running:
    width = len(input_lines[0])
    height = len(input_lines)
    num_forklift = 0
    for y in range(width):
        for x in range(height):
            adjacent_tiles = find_adjacent_tiles(input_lines, x, y, width, height, condition_adjacent=lambda a,x,y: (a[y][x]=='@'), condition_tile=lambda a,x,y:a[y][x]=='@')
            if adjacent_tiles is not None and len(adjacent_tiles) < 4:
                num_forklift += 1
                print(f" we will forklift tile: {y}, {x}")
                new_string = input_lines[y][0:x] + '.' + input_lines[y][x+1:width]
                input_lines[y] = new_string

    print(f"num forklift: {num_forklift}")
    total_forklift += num_forklift
    if num_forklift == 0:
        running = False
print(f'Final forklift: {total_forklift}')