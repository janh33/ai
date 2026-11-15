from collections import deque

# 0 = Free path, 1 = Obstacle

grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# BFS function
def bfs():

    queue = deque([[start]])
    visited = [start]

    while queue:

        path = queue.popleft()
        x, y = path[-1]

        # Check goal
        if (x, y) == goal:
            print("Path Found:", path)
            print("Shortest Path Length:", len(path) - 1)
            return

        # Possible movements
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

            if (0 <= nx < 4 and 0 <= ny < 4 and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                visited.append((nx, ny))
                queue.append(path + [(nx, ny)])

    print("No path found!")


# Run BFS
bfs()