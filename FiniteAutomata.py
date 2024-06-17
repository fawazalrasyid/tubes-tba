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
        3: {'r': 4, 'k': 8, 's': 15, 't': 18, 'm': 22},
        4: {'u': 5},
        5: {'m': 6},
        6: {'a': 7},
        7: {'h': 7},
        8: {'a': 9},
        9: {'n': 10},
        10: {'t': 11},
        11: {'o': 12},
        12: {'r': 13},
        15: {'e': 16},
        16: {'k': 25},
        18: {'a': 19},
        19: {'m': 20},
        20: {'a': 21},
        22: {'a': 23},
        23: {'l': 24},
        24: {'l': 30},
        25: {'o': 26},
        26: {'l': 27},
        27: {'a': 28},
        28: {'h': 29}
    }
    final_states = {7, 13, 21, 29, 30}
    currState = 0
    for letter in word:
        if currState in transitions and letter in transitions[currState]:
            currState = transitions[currState][letter]
        else:
            currState = -1
            break
    return currState in final_states
