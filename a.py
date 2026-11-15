import heapq

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate misplaced tiles
def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# A* Search Algorithm
def astar(start):

    pq = []
    heapq.heappush(pq, (0, start))

    visited = set()

    while pq:

        cost, state = heapq.heappop(pq)

        if state == goal:
            print("Goal Reached!")
            print(state)
            return

        if state in visited:
            continue

        visited.add(state)

        zero = state.index(0)

        moves = [-3, 3, -1, 1]

        for move in moves:

            new = zero + move

            if 0 <= new < 9:

                if abs(zero % 3 - new % 3) <= 1:

                    new_state = list(state)

                    new_state[zero], new_state[new] = new_state[new], new_state[zero]

                    new_state = tuple(new_state)

                    if new_state not in visited:

                        g = cost + 1
                        h = heuristic(new_state)

                        heapq.heappush(pq, (g + h, new_state))


# Run the algorithm
astar(start)