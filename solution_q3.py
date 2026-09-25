def astar_heuristic_1():
    """
    In this part, you will extend UCS to A* search using Cost Model A.
    Heuristic 1 — Passenger Weight Remaining
    ℎ1(𝑠) = 2𝑀left + 1𝐶left
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

    # A* structure: each queue entry has tuple (f cost, g cost, current state, path)
    # f = g + h

    queue = []

    initial_g = 0
    initial_h = heuristic_1(initial_state)
    initial_f = initial_g + initial_h

    queue.append((initial_f, initial_g, initial_state, [initial_state]))

    # stores lowest g cost found for each state
    lowest_g_cost = {}
    lowest_g_cost[tuple(initial_state)] = 0

    expansions = 0

    # implement A*
    while len(queue) > 0:

        # main difference from UCS: find state with lowest f = g + h

        lowest_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[lowest_index][0]:
                lowest_index = i

        current_f, current_g, current_state, current_path = queue.pop(lowest_index)

        # ignore this node if a cheaper route to this state has been found previously

        if current_g > lowest_g_cost[tuple(current_state)]:
            continue

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            print("The solution of Q3.1 (Heuristic 1) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", current_g)
            print("Number of node expansions = ", expansions)

            return current_path

        # if goal not reached, expand this node
        expansions += 1

        # generate possible next states (nodes) from action set
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

                    # calculate cost for model A (M = 2, C = 1)
                    # use the name of each action to find number of M and C, skipping first letter used for boat
                    action_cost = 0
                    
                    m_moved = abs(actions[key][0]) #Get how many of each group moved
                    c_moved = abs(actions[key][1])
                    action_cost = 2 * m_moved + c_moved

                    # we use g as it is actual cost to reach new state
                    new_g = current_g + action_cost

                    new_state_tuple = tuple(new_state)

                    # ensure this state is not visited already and no cheaper path has been found
                    if new_state_tuple not in lowest_g_cost or new_g < lowest_g_cost[new_state_tuple]:
                        lowest_g_cost[new_state_tuple] = new_g

                        new_h = heuristic_1(new_state)

                        # f(n) = g(n) + h(n)
                        new_f = new_g + new_h

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_f, new_g, new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q3.1 (Heuristic 1) is:")
    print("No solution found.")
    return None

def astar_heuristic_2():
    """
    Heuristic 2 — Trip-Packing Lower Bound
    ℎ2(𝑠) = ⌈2𝑀lef t + 1𝐶left⌉
                    3
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

    # A* structure: each queue entry has tuple (f cost, g cost, current state, path)
    # f = g + h

    queue = []

    initial_g = 0
    initial_h = heuristic_2(initial_state)
    initial_f = initial_g + initial_h

    queue.append((initial_f, initial_g, initial_state, [initial_state]))

    # stores lowest g cost found for each state
    lowest_g_cost = {}
    lowest_g_cost[tuple(initial_state)] = 0

    expansions = 0

    # implement A*
    while len(queue) > 0:

        # main difference from UCS: find state with lowest f = g + h

        lowest_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[lowest_index][0]:
                lowest_index = i

        current_f, current_g, current_state, current_path = queue.pop(lowest_index)

        # ignore this node if a cheaper route to this state has been found previously

        if current_g > lowest_g_cost[tuple(current_state)]:
            continue

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            print("The solution of Q3.1 (Heuristic 2) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", current_g)
            print("Number of node expansions = ", expansions)

            return current_path

        # if goal not reached, expand this node
        expansions += 1

        # generate possible next states (nodes) from action set
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

                    # calculate cost for model A (M = 2, C = 1)
                    # use the name of each action to find number of M and C, skipping first letter used for boat
                    action_cost = 0
                    
                    m_moved = abs(actions[key][0]) #Get how many of each group moved
                    c_moved = abs(actions[key][1])
                    action_cost = 2 * m_moved + c_moved

                    # we use g as it is actual cost to reach new state
                    new_g = current_g + action_cost

                    new_state_tuple = tuple(new_state)

                    # ensure this state is not visited already and no cheaper path has been found
                    if new_state_tuple not in lowest_g_cost or new_g < lowest_g_cost[new_state_tuple]:
                        lowest_g_cost[new_state_tuple] = new_g

                        new_h = heuristic_2(new_state)

                        # f(n) = g(n) + h(n)
                        new_f = new_g + new_h

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_f, new_g, new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q3.1 (Heuristic 2) is:")
    print("No solution found.")

    return None


def astar_heuristic_3():
    return None
    """
    Heuristic 2 — Trip-Packing Lower Bound
    ℎ2(𝑠) = ⌈2𝑀lef t + 1𝐶left⌉
                    3
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

    # A* structure: each queue entry has tuple (f cost, g cost, current state, path)
    # f = g + h

    queue = []

    initial_g = 0
    initial_h = heuristic_3(initial_state)
    initial_f = initial_g + initial_h

    queue.append((initial_f, initial_g, initial_state, [initial_state]))

    # stores lowest g cost found for each state
    lowest_g_cost = {}
    lowest_g_cost[tuple(initial_state)] = 0

    expansions = 0

    # implement A*
    while len(queue) > 0:

        # main difference from UCS: find state with lowest f = g + h

        lowest_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[lowest_index][0]:
                lowest_index = i

        current_f, current_g, current_state, current_path = queue.pop(lowest_index)

        # ignore this node if a cheaper route to this state has been found previously

        if current_g > lowest_g_cost[tuple(current_state)]:
            continue

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            print("The solution of Q3.1 (Heuristic 3) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", current_g)
            print("Number of node expansions = ", expansions)

            return current_path

        # if goal not reached, expand this node
        expansions += 1

        # generate possible next states (nodes) from action set
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

                    # calculate cost for model A (M = 2, C = 1)
                    # use the name of each action to find number of M and C, skipping first letter used for boat
                    action_cost = 0
                    
                    m_moved = abs(actions[key][0]) #Get how many of each group moved
                    c_moved = abs(actions[key][1])
                    action_cost = 2 * m_moved + c_moved

                    # we use g as it is actual cost to reach new state
                    new_g = current_g + action_cost

                    new_state_tuple = tuple(new_state)

                    # ensure this state is not visited already and no cheaper path has been found
                    if new_state_tuple not in lowest_g_cost or new_g < lowest_g_cost[new_state_tuple]:
                        lowest_g_cost[new_state_tuple] = new_g

                        new_h = heuristic_3(new_state)

                        # f(n) = g(n) + h(n)
                        new_f = new_g + new_h

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_f, new_g, new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q3.1 (Heuristic 2) is:")
    print("No solution found.")

    return None

def heuristic_1(state):
    # h1(s) = 2 * M_left + C_left
    m_left = state[0]
    c_left = state[1]
    weight_remaining = 2 * m_left + c_left
    return weight_remaining

def heuristic_2(state):
    # h2(s) = ceil(2 * M_left + C_left) / 3)
    m_left = state[0]
    c_left = state[1]
    weight_remaining = 2 * m_left + c_left
    return (weight_remaining // 3)

def heuristic_3(state):
    pass

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
    astar_heuristic_1()
    print("")
    astar_heuristic_2()
    print("")
    astar_heuristic_3()