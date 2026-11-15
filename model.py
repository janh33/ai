#1 is obstacle 0 is free way
grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0]
]

#start positiom of agent
agent = [0,0]

# define goal
goal = [2,2]

internal_state = []

#display start pos
print(f"Agent starts at: {agent}")

# continue moving until agent reaches goal
while agent!=goal:

  # store curr in internal state 
  internal_state.append(agent.copy())

  # get curr row and col
  row = agent[0]
  col = agent[1]

  # try tp move right 
  if col+1 < 3 and grid[row][col+1] == 0:
    agent[1] = agent[1]+1

  # if right is blocked try to move down 
  elif row +1 < 3 and grid[row+1][col] == 0:
    agent[0] = agent[0]+1

  # cannot move right and down then 
  else:
    print("Agent is blocked ")
    break

  print(f"Agent moved to: {agent}")
if agent == goal:
  print("Goal reached")
print(f"Internal states: {internal_state}")  
