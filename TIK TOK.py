# Constants
BOARD_EMPTY = 0
BOARD_PLAYER_X = 1
BOARD_PLAYER_O = -1

# Helper functions
def terminal(s):
    for i in range(3):
        if s[3 * i] == s[3 * i + 1] == s[3 * i + 2] != BOARD_EMPTY:
            return s[3 * i]
        if s[i] == s[i + 3] == s[i + 6] != BOARD_EMPTY:
            return s[i]
    if s[0] == s[4] == s[8] != BOARD_EMPTY:
        return s[0]
    if s[2] == s[4] == s[6] != BOARD_EMPTY:
        return s[2]
    if empty_cells(s) == 0:
        return BOARD_EMPTY
    return None

def empty_cells(s):
    return sum(1 for i in s if i == BOARD_EMPTY)

def utility(s, cost):
    term = terminal(s)
    if term is not None:
        return (term, cost)
    action_list = actions(s)
    utils = []
    for action in action_list:
        new_s = result(s, action)
        utils.append(utility(new_s, cost + 1))
    score = utils[0][0]
    idx_cost = utils[0][1]
    play = player(s)
    if play == BOARD_PLAYER_X:
        for i in range(len(utils)):
            if utils[i][0] > score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    else:
        for i in range(len(utils)):
            if utils[i][0] < score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    return (score, idx_cost)

# Main functions
def result(s, a):
    s_copy = s.copy()
    s_copy[a] = -s_copy[a]
    return s_copy

def player(s):
    counter = counter(s)
    x_places = counter[1]
    o_places = counter[-1]
    if x_places + o_places == 9:
        return None
    elif x_places > o_places:
        return BOARD_PLAYER_O
    else:
        return BOARD_PLAYER_X

def actions(s):
    play = player(s)
    actions_list = [(play, i) for i in range(len(s)) if s[i] == BOARD_EMPTY]
    return actions_list

def minimax(s):
    action_list = actions(s)
    utils = []
    for action in action_list:
        new_s = result(s, action)
        utils.append((action, utility(new_s, 1)))
    if len(utils) == 0:
        return ((0, 0), (0, 0))
    sorted_list = sorted(utils, key=lambda l : l[0][1])
    action = min(sorted_list, key = lambda l : l[1])
    return action

# Example usage
s = [BOARD_EMPTY for _ in range(9)]
best_move = minimax(s)
print(best_move)