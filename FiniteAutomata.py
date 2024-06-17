def isSubjek(word: str) -> bool:
    # Subjek = {aku, ali, ani, dia, dini}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'a': currState = 1
                elif letter == 'd': currState = 4
                else: currState = -1
            case 1:
                if letter == 'k': currState = 2
                elif letter == 'l': currState = 5
                elif letter == 'n': currState = 6
                else: currState = -1
            case 2: currState = 3 if letter == 'u' else -1
            case 3: break # FINAL STATE for 'aku'
            case 4: currState = 7 if letter == 'i' else -1
            case 5: currState = 3 if letter == 'i' else -1 # FINAL STATE for 'ali'
            case 6: currState = 3 if letter == 'i' else -1 # FINAL STATE for 'ani'
            case 7: 
                if letter == 'a': currState = 8
                elif letter == 'n': currState = 9
                else: currState = -1
            case 8: break # FINAL STATE for 'dia'
            case 9: currState = 10 if letter == 'i' else -1
            case 10: break # FINAL STATE for 'dini'
    return currState in {3, 8, 10}

def isPredikat(word: str) -> bool:
    # Predikat = {makan, minum, mandi, main, masak}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'm': currState = 1
                else: currState = -1
            case 1:
                if letter == 'a': currState = 2
                elif letter == 'i': currState = 6
                else: currState = -1
            case 2:
                if letter == 'k': currState = 3
                elif letter == 's': currState = 14
                elif letter == 'n': currState = 12
                elif letter == 'i': currState = 18
                else: currState = -1
            case 3: currState = 4 if letter == 'a' else -1
            case 4: currState = 5 if letter == 'n' else -1
            case 5: break # FINAL STATE for 'makan'
            case 6: currState = 7 if letter == 'n' else -1
            case 7: currState = 8 if letter == 'u' else -1
            case 8: currState = 9 if letter == 'm' else -1
            case 9: break # FINAL STATE for 'minum'
            case 12: currState = 20 if letter == 'd' else -1
            case 13: break # FINAL STATE for 'mandi'
            case 14: currState = 15 if letter == 'a' else -1
            case 15: currState = 16 if letter == 'k' else -1
            case 16: break # FINAL STATE for 'masak'
            case 18: currState = 19 if letter == 'n' else -1
            case 19: break # FINAL STATE for 'main'
            case 20: currState = 13 if letter == 'i' else -1
    return currState in {5, 9, 13, 16, 19}

def isObjek(word: str) -> bool:
    # Objek = {apel, ayam, air, api, alat}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'a': currState = 1
                else: currState = -1
            case 1:
                if letter == 'p': currState = 2
                elif letter == 'y': currState = 6
                elif letter == 'i': currState = 9
                elif letter == 'l': currState = 13
                else: currState = -1
            case 2:
                if letter == 'e': currState = 3
                elif letter == 'i': currState = 10
                else: currState = -1
            case 3: currState = 4 if letter == 'l' else -1
            case 4: break # FINAL STATE for 'apel'
            case 6: currState = 7 if letter == 'a' else -1
            case 7: currState = 8 if letter == 'm' else -1
            case 8: break # FINAL STATE for 'ayam'
            case 9: currState = 10 if letter == 'r' else -1
            case 10: break # FINAL STATE for 'air' and 'api'
            case 13: currState = 14 if letter == 'a' else -1
            case 14: currState = 15 if letter == 't' else -1
            case 15: break # FINAL STATE for 'alat'
    return currState in {4, 8, 10, 15}

def isKeterangan(word: str) -> bool:
    # Ket = {di_rumah, di_kantor, di_sekolah, di_taman, di_mall}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'd': currState = 1
                else: currState = -1
            case 1: currState = 2 if letter == 'i' else -1
            case 2: currState = 3 if letter == '_' else -1
            case 3:
                if letter == 'r': currState = 4
                elif letter == 'k': currState = 8
                elif letter == 's': currState = 15
                elif letter == 't': currState = 18
                elif letter == 'm': currState = 22
                else: currState = -1
            case 4: currState = 5 if letter == 'u' else -1
            case 5: currState = 6 if letter == 'm' else -1
            case 6: currState = 7 if letter == 'a' else -1
            case 7: currState = 7 if letter == 'h' else -1 # FINAL STATE for 'di_rumah'
            case 8: currState = 9 if letter == 'a' else -1
            case 9: currState = 10 if letter == 'n' else -1
            case 10: currState = 11 if letter == 't' else -1
            case 11: currState = 12 if letter == 'o' else -1
            case 12: currState = 13 if letter == 'r' else -1
            case 13: break # FINAL STATE for 'di_kantor'
            case 15: currState = 16 if letter == 'e' else -1
            case 16: currState = 25 if letter == 'k' else -1
            case 25: currState = 26 if letter == 'o' else -1
            case 26: currState = 27 if letter == 'l' else -1
            case 27: currState = 28 if letter == 'a' else -1
            case 28: currState = 29 if letter == 'h' else -1
            case 29: break # FINAL STATE for 'di_sekolah'
            case 18: currState = 19 if letter == 'a' else -1
            case 19: currState = 20 if letter == 'm' else -1
            case 20: currState = 21 if letter == 'a' else -1
            case 21: break # FINAL STATE for 'di_taman'
            case 22: currState = 23 if letter == 'a' else -1
            case 23: currState = 24 if letter == 'l' else -1
            case 24: currState = 30 if letter == 'l' else -1
            case 30: break # FINAL STATE for 'di_mall'
    return currState in {7, 13, 21, 29, 30}
