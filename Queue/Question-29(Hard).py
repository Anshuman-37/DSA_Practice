# Question 29: Use queue-based BFS to find the shortest path in a maze.
from collections import deque

def find_shortest_path_bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current_pos, path = queue.popleft()
        row, col = current_pos

        if current_pos == end:
            return path

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and \
               maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                new_path = list(path)
                new_path.append(new_pos)
                queue.append((new_pos, new_path))

    return None

def find_start_end(maze):
    start = None
    end = None
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '#'],
    ['#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

start, end = find_start_end(maze)

if start and end:
    shortest_path = find_shortest_path_bfs(maze, start, end)

    if shortest_path:
        print("Shortest Path:")
        for row, col in shortest_path:
            print(f"({row}, {col})")

        maze_with_path = [list(row) for row in maze]
        for i, (row, col) in enumerate(shortest_path):
            if maze_with_path[row][col] not in ['S', 'E']:
                maze_with_path[row][col] = str(i + 1)

        print("\nMaze with Shortest Path:")
        for row in maze_with_path:
            print(' '.join(row))
    else:
        print("No path found.")
else:
    print("Start or End position not found in the maze.")