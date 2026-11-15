class ModelBasedAgent:

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.position = start
        self.goal = goal

        # Internal state representation
        self.internal_state = {
            "current_position": start,
            "visited": [start]
        }

    def get_valid_moves(self):
        row, col = self.position

        moves = {
            "UP": (row - 1, col),
            "DOWN": (row + 1, col),
            "LEFT": (row, col - 1),
            "RIGHT": (row, col + 1)
        }

        valid_moves = []

        for action, (r, c) in moves.items():

            if (0 <= r < len(self.grid) and
                0 <= c < len(self.grid[0]) and
                self.grid[r][c] != 1):

                valid_moves.append((action, (r, c)))

        return valid_moves

    def navigate(self):

        print("Starting Position:", self.position)
        print("Goal Position:", self.goal)

        while self.position != self.goal:

            valid_moves = self.get_valid_moves()

            if not valid_moves:
                print("No valid moves available!")
                return

            moved = False

            for action, new_position in valid_moves:

                if new_position not in self.internal_state["visited"]:

                    self.position = new_position

                    self.internal_state["current_position"] = new_position

                    self.internal_state["visited"].append(new_position)

                    print("Action:", action)
                    print("New Position:", self.position)

                    moved = True
                    break

            if not moved:
                print("Goal cannot be reached!")
                return

        print("\nGoal Reached Successfully!")
        print("Final Position:", self.position)
        print("Visited Positions:",
              self.internal_state["visited"])


# 0 = Free Path
# 1 = Obstacle

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

agent = ModelBasedAgent(grid, start, goal)

agent.navigate()