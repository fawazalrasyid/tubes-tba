from FiniteAutomata import isSubjek, isPredikat, isObjek, isKeterangan

def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if isSubjek(word): return 'S'
        elif isPredikat(word): return 'P'
        elif isObjek(word): return 'O'
        elif isKeterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'
