"""Implement DFS algorithm that works with starting state that is read in from an input file called
input.txt. The format of the state should be the same as what we mention above.
• Output: path of states returned, total cost (where cost is defined in terms of number of
actions),and number of node expansions."""

"""The program must read from input.txt, which specifies the initial state of the puzzle
• The state will be represented as: M_left,C_left,M_right,C_right,Boat (Ex: 3, 3, 0, 0, L)"""

def depth_fs():
    """
    • Implement DFS algorithm that works with starting state that is read in from an input file called
        input.txt. The format of the state should be the same as what we mention above.
    • Output: path of states returned, total cost (where cost is defined in terms of number of
        actions),and number of node expansions.
        
    Example Terminal Output:
    The solution of Q1.1.a (DFS) is:
    Solution Path: <Path>
    Total cost = <number>
    Number of node expansions = <number>\n\n"""
    with open("input.txt", "r") as file:
        contents = file.read()

    m_left, c_left, m_right, c_right, boat = contents.split(",")
    initial_state = [
        int(m_left.strip()), 
        int(c_left.strip()), 
        int(m_right.strip()),
        int(c_right.strip()),
        boat.strip()
    ]
    
    # set of possible actions with changes to numbers of missionaries/cannibals per side
    actions = {
        "LCC": [0, -2, 0, 2],
        "LC":  [0, -1, 0, 1],
        "LCM": [-1, -1, 1, 1],
        "LM":  [-1, 0, 1, 0],
        "LMM": [-2, 0, 2, 0],
    
        "RCC": [0, 2, 0, -2],
        "RC":  [0, 1, 0, -1],
        "RCM": [1, 1, -1, -1],
        "RM":  [1, 0, -1, 0],
        "RMM": [2, 0, -2, 0]
    }
    
    # set up for DFS using a stack, with structure = (current state, [path to get there]) as a tuple

    stack = []

    stack.append((initial_state, [initial_state]))

    visited = []
    visited.append(initial_state)

    expansions = 0

    # implement the DFS (always remove most recent non-visited state)
    while len(stack) > 0:
        current_state, current_path = stack.pop()

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            total_cost = len(current_path) - 1
            print("The solution of Q1.1.a (DFS) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", total_cost)
            print("Number of node expansions = ", expansions)

            return current_path

        # if goal not reached, expand this node
        expansions += 1

        # generate possible next states from action set
        for key in actions:
            # only need to look at actions from current boat side
            if key[0] == current_state[4]:

                new_state = []
                # calculates new values from current action
                for j in range(4):
                    new_state.append(current_state[j] + actions[key][j])

                # move boat
                if current_state[4] == "L":
                    new_state.append("R")
                else:
                    new_state.append("L")

                #check new state for validity

                if valid_state(new_state):

                    # ensure this state is not visited already
                    if new_state not in visited:
                        visited.append(new_state)

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        stack.append((new_state, new_path))

    # empty stack -> no solution
    
    print("The solution of Q1.1.a (DFS) is:")
    print("No solution found.")

    return None

def breadth_fs():
    """
    • Implement a BFS that works with starting state that is read in from an input file called input.txt.
        The format of the state should be the same as what we mention above.
    • Output: path of states returned, total cost (where cost is defined in terms of number of actions),
        and number of node expansions.

    Example Terminal Output:
    The solution of Q1.1.b (BFS) is:
    Solution Path: <Path>
    Total cost = <number>
    Number of node expansions = <number>
    """
    with open("input.txt", "r") as file:
        contents = file.read()
    m_left, c_left, m_right, c_right, boat = contents.split(",")
    initial_state = [
        int(m_left.strip()), 
        int(c_left.strip()), 
        int(m_right.strip()),
        int(c_right.strip()),
        boat.strip()
    ]

    # set of possible actions with changes to numbers of missionaries/cannibals per side
    actions = {
        "LCC": [0, -2, 0, 2],
        "LC":  [0, -1, 0, 1],
        "LCM": [-1, -1, 1, 1],
        "LM":  [-1, 0, 1, 0],
        "LMM": [-2, 0, 2, 0],

        "RCC": [0, 2, 0, -2],
        "RC":  [0, 1, 0, -1],
        "RCM": [1, 1, -1, -1],
        "RM":  [1, 0, -1, 0],
        "RMM": [2, 0, -2, 0]
    }

    # set up for BFS using a queue, with structure = (current state, [path to get there]) as a tuple

    queue = []

    queue.append((initial_state, [initial_state]))

    visited = []
    visited.append(initial_state)

    expansions = 0

    # implement the BFS (always remove oldest state)
    while len(queue) > 0:
        current_state, current_path = queue.pop(0)

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            total_cost = len(current_path) - 1
            print("The solution of Q1.1.b (BFS) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", total_cost)
            print("Number of node expansions = ", expansions)

            return current_path

        # if goal not reached, expand this node
        expansions += 1

        # generate possible next states from action set
        for key in actions:
            # only need to look at actions from current boat side
            if key[0] == current_state[4]:

                new_state = []
                # calculates new values from current action
                for j in range(4):
                    new_state.append(current_state[j] + actions[key][j])

                # move boat
                if current_state[4] == "L":
                    new_state.append("R")
                else:
                    new_state.append("L")

                #check new state for validity

                if valid_state(new_state):

                    # ensure this state is not visited already
                    if new_state not in visited:
                        visited.append(new_state)

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q1.1.b (BFS) is:")
    print("No solution found.")

    return None

def valid_state(state):
    # Returns true if the input state follows all rules in the situation
    m_left = state[0]
    c_left = state[1]
    m_right = state[2]
    c_right = state[3]

    # Cannot have a negative number of people
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    # Cannibals cannot outnumber missionaries on the left unless there are no missionaries on that side
    if m_left > 0 and c_left > m_left:
        return False

    # Cannibals cannot outnumber missionaries on the right unless there are no missionaries on that side
    if m_right > 0 and c_right > m_right:
        return False

    return True

if __name__ == "__main__":
    depth_fs()
    breadth_fs()