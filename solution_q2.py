def uniform_cost_a():
    """
    Missionaries carry heavy books and supplies, while cannibals travel light. Every
    missionary on the boat adds more rowing effort. Hence, it is twice as costly to carry a missionary as
    compared to a cannibal.
    Cost = 2 units per missionary + 1 unit per cannibal.
    Examples:
    • Move {M, M} → cost 4
    • Move {C, C} → cost 2
    • Move {M, C} → cost 3"""
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
    #! IS the L or R dictating what side the boat is currently on before the move (the two letters that follow)
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

    # UCS structure: each queue entry has tuple (total cost, current state, path to current state)

    queue = []

    queue.append((0, initial_state, [initial_state]))

    # stores cheapest cost found for each state so far
    best_cost = {}
    best_cost[tuple(initial_state)] = 0

    expansions = 0

    # implement UCS
    while len(queue) > 0:

        # main difference from BFS: find node with lowest total cost

        lowest_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[lowest_index][0]:
                lowest_index = i

        current_cost, current_state, current_path = queue.pop(lowest_index)

        # ignore this node if a cheaper route to this state has been found previously

        if current_cost > best_cost[tuple(current_state)]:
            continue

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            print("The solution of Q2.1 (UCS, cost model A) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", current_cost)
            print("Number of node exansions = ", expansions)

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
                    # calculate cost for model A ({M, M} = 4, {C, C} = 2, {M, C} = 3)
                    m_moved = abs(actions[key][0]) #Get how many of each group moved
                    c_moved = abs(actions[key][1])

                    action_cost = 2 * m_moved + c_moved

                    new_cost = current_cost + action_cost
                    new_state_tuple = tuple(new_state)

                    # ensure this state is not visited already and no cheaper path has been found
                    if new_state_tuple not in best_cost or new_cost < best_cost[new_state_tuple]:
                        best_cost[new_state_tuple] = new_cost

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_cost, new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q2.1 (UCS, cost model A) is:")
    print("No solution found.")

    return None

def uniform_cost_b():
    """
    The river current flows right → left. Going against the current (left → right) is harder,
    while coming back (right → left) is easier.
    • Left → Right trip = cost 2
    • Right → Left trip = cost 1"""
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

    # UCS structure: each queue entry has tuple (total cost, current state, path to current state)

    queue = []

    queue.append((0, initial_state, [initial_state]))

    # stores cheapest cost found for each state so far
    best_cost = {}
    best_cost[tuple(initial_state)] = 0

    expansions = 0

    # implement UCS
    while len(queue) > 0:

        # main difference from BFS: find node with lowest total cost

        lowest_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[lowest_index][0]:
                lowest_index = i

        current_cost, current_state, current_path = queue.pop(lowest_index)

        # ignore this node if a cheaper route to this state has been found previously

        if current_cost > best_cost[tuple(current_state)]:
            continue

        #check for success condition (all on right bank)
        if current_state[0] == 0 and current_state[1] == 0:
            print("The solution of Q2.1 (UCS, cost model B) is:")
            print("Solution Path:")

            for state in current_path:
                print(state)

            print("Total cost = ", current_cost)
            print("Number of node exansions = ", expansions)

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

                    # calculate cost for model B (L = 2, R = 1)
                    if current_state[4] == "L":
                        action_cost = 2
                    else:
                        action_cost = 1

                    new_cost = current_cost + action_cost

                    new_state_tuple = tuple(new_state)

                    # ensure this state is not visited already and no cheaper path has been found
                    if new_state_tuple not in best_cost or new_cost < best_cost[new_state_tuple]:
                        best_cost[new_state_tuple] = new_cost

                        # add action/state to path 
                        new_path = current_path + [new_state]
                        #add the new tuple to the queue
                        queue.append((new_cost, new_state, new_path))

    # empty queue -> no solution
    
    print("The solution of Q2.1 (UCS, cost model B) is:")
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
    uniform_cost_a()
    uniform_cost_b()
