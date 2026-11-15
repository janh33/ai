# Goal Stack Planning - Blocks World

# Initial State
blocks = {
    'A': 'TABLE',
    'B': 'A',
    'C': 'TABLE'
}

# Goal State
goal = {
    'A': 'TABLE',
    'B': 'TABLE',
    'C': 'B'
}

# Find clear blocks
def clear(block):
    for b in blocks:
        if blocks[b] == block:
            return False
    return True


# Move block
def move(block, destination):

    if clear(block):

        old = blocks[block]

        if destination == 'TABLE' or clear(destination):

            print("Move", block, "from", old, "to", destination)

            blocks[block] = destination

            return True

    return False


# Goal Stack Planning
def solve():

    for block in goal:

        destination = goal[block]

        if blocks[block] != destination:

            if destination == 'TABLE':

                move(block, 'TABLE')

            else:

                if not clear(destination):
                    for b in blocks:
                        if blocks[b] == destination:
                            move(b, 'TABLE')

                move(block, 'TABLE')
                move(block, destination)


# Execute
print("Initial State:", blocks)

solve()

print("Final State:", blocks)
print("Goal Achieved!")