def isSubjek(word: str) -> bool:
    transitions = {
        0: {'a': 1, 'd': 4},
        1: {'k': 2, 'l': 5, 'n': 6},
        2: {'u': 3},
        4: {'i': 7},
        5: {'i': 3},
        6: {'i': 3},
        7: {'a': 8, 'n': 9},
        9: {'i': 10}
    }
    final_states = {3, 8, 10}
    currState = 0
    for letter in word:
        if currState in transitions and letter in transitions[currState]:
            currState = transitions[currState][letter]
        else:
            currState = -1
            break
    return currState in final_states

def isPredikat(word: str) -> bool:
    transitions = {
        0: {'m': 1},
        1: {'a': 2, 'i': 6},
        2: {'k': 3, 's': 14, 'n': 12, 'i': 18},
        3: {'a': 4},
        4: {'n': 5},
        6: {'n': 7},
        7: {'u': 8},
        8: {'m': 9},
        12: {'d': 20},
        14: {'a': 15},
        15: {'k': 16},
        18: {'n': 19},
        20: {'i': 13}
    }
    final_states = {5, 9, 13, 16, 19}
    currState = 0
    for letter in word:
        if currState in transitions and letter in transitions[currState]:
            currState = transitions[currState][letter]
        else:
            currState = -1
            break
    return currState in final_states

def isObjek(word: str) -> bool:
    transitions = {
        0: {'a': 1},
        1: {'p': 2, 'y': 6, 'i': 9, 'l': 13},
        2: {'e': 3, 'i': 10},
        3: {'l': 4},
        6: {'a': 7},
        7: {'m': 8},
        9: {'r': 10},
        13: {'a': 14},
        14: {'t': 15}
    }
    final_states = {4, 8, 10, 15}
    currState = 0
    for letter in word:
        if currState in transitions and letter in transitions[currState]:
            currState = transitions[currState][letter]
        else:
            currState = -1
            break
    return currState in final_states

def isKeterangan(word: str) -> bool:
    transitions = {
        0: {'d': 1},
        1: {'i': 2},
        2: {'_': 3},
        3: {'r': 4, 'k': 9, 's': 15, 'm': 22, 't': 26},
        4: {'u': 5},
        5: {'m': 6},
        6: {'a': 7},
        7: {'h': 8},
        9: {'a': 10},
        10: {'n': 11},
        11: {'t': 12},
        12: {'o': 13},
        13: {'r': 14},
        15: {'e': 16},
        16: {'k': 17},
        17: {'o': 18},
        18: {'l': 19},
        19: {'a': 20},
        20: {'h': 21},
        22: {'a': 23},
        23: {'l': 24},
        24: {'l': 25},
        26: {'a': 27},
        27: {'m': 28},
        28: {'a': 29},
        29: {'n': 30},
    }
    final_states = {8, 14, 21, 25, 30}
    currState = 0
    for letter in word:
        if currState in transitions and letter in transitions[currState]:
            currState = transitions[currState][letter]
        else:
            currState = -1
            break
    return currState in final_states
