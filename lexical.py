import string

def lexical(str):
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 
                  'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15']
    transition_table = {}

    # Transition definitions
    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
            transition_table[(state, "#")] = "error"
            transition_table[(state, " ")] = "error"

    transition_table[("q0", " ")] = "q0"
    transition_table[("q14", "#")] = "accept"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "#")] = "accept"
    transition_table[("q15", " ")] = "q15"

    transition_table[("q0", "i")] = "q1"
    transition_table[("q1", "n")] = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "i")] = "q1"

    transition_table[("q0", "k")] = "q1"
    transition_table[("q1", "a")] = "q2"
    transition_table[("q2", "t")] = "q3"
    transition_table[("q3", "a")] = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "k")] = "q1"

    transition_table[("q0", "a")] = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "a")] = "q14"

    transition_table[("q0", ":")]  = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", ":")] = "q14"

    transition_table[("q0", "p")] = "q4"
    transition_table[("q4", "r")] = "q5"
    transition_table[("q5", "i")] = "q6"
    transition_table[("q6", "n")] = "q7"
    transition_table[("q7", "t")] = "q8"
    transition_table[("q8", "(")] = "q9"
    transition_table[("q9", "k")] = "q10"
    transition_table[("q10", "a")] = "q11"
    transition_table[("q11", "t")] = "q12"
    transition_table[("q12", "a")] = "q13"
    transition_table[("q13", ")")] = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "p")] = "q4"

    transition_table[("q0", "f")] = "q7"
    transition_table[("q7", "o")] = "q8"
    transition_table[("q8", "r")] = "q14"
    transition_table[("q14", " ")] = "q15"
    transition_table[("q15", "f")] = "q7"

    #Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    for current_char in (str.lower()+'#'):
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q14':
            print('CURRENT TOKEN: ', current_token, ', VALID')
            current_token = ''
        if state == 'error':
            print('ERROR')
            break
        idx_char = idx_char + 1

    #Conclusion || state yang di accept
    if state == "accept":
        result = 'Semua token yang di input valid'
    else:
        result = 'Token yang di input tidak valid'

    return result