import random

# Maze dimensions
width = 20
height = 10

# Maze generation
def generate_maze(width, height):
    maze = [[0] * width for _ in range(height)]

    def create_maze(x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                maze[y][x] |= 1 << directions.index((dx, dy))
                maze[ny][nx] |= 1 << directions.index((-dx, -dy))
                create_maze(nx, ny)

    create_maze(0, 0)
    return maze

maze = generate_maze(width, height)

# A* algorithm for solving the maze
def solve_maze(maze):
    start = (0, 0)
    goal = (width - 1, height - 1)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    open_list = [(0, start)]
    came_from = {}

    g_score = {pos: float('inf') for row in maze for pos in row}
    g_score[start] = 0

    f_score = {pos: float('inf') for row in maze for pos in row}
    f_score[start] = heuristic(start, goal)

    while open_list:
        current = min(open_list, key=lambda pos: f_score[pos])
        if current == goal:
            return reconstruct_path(came_from, current)
        
        open_list.remove(current)
        for dx, dy in directions:
            x, y = current
            neighbor = (x + dx, y + dy)
            tentative_g_score = g_score[current] + 1

            if 0 <= x + dx < width and 0 <= y + dy < height and maze[y][x] & (1 << directions.index((dx, dy))) == 0:
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    if neighbor not in open_list:
                        open_list.append(neighbor)
    
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

solution = solve_maze(maze)

# Displaying the maze and solution
if solution:
    for y in range(height):
        for x in range(width):
            if (x, y) in solution:
                print("X", end=" ")
            else:
                print("#", end=" ")
        print()
else:
    print("No solution found.")
