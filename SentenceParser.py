from LexicalAnalyzer import tokenRecognizer

def parser(sentence):
    ERR = Exception('ParsingError')
    words = sentence.split()
    words.append('')
    res = []
    stack = []
    state = 0
    print("Stack:")
    print(stack)
    stack.append('#')
    state = 1
    print(stack)
    stack.append('X')
    state = 2
    i = 0
    try:
        while stack[-1] != '#':
            print(stack)
            word = words[i]
            if word != '': token = tokenRecognizer(word)
            match stack[-1]:
                case 'X':
                    if token == 'S':
                        stack.pop()
                        stack.append('Y')
                        stack.append('P')
                        stack.append('S')
                    else: raise ERR
                case 'Y':
                    if word == '': stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: raise ERR
                case 'Z':
                    if word == '': stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: raise ERR
                case 'S':
                    if token == 'S':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'P':
                    if token == 'P':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'O':
                    if token == 'O':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case 'K':
                    if token == 'K':
                        res.append(stack.pop())
                        stack.append(word)
                    else: raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: raise ERR
        print(stack)
        stack.pop()
        print(stack)

        print("Struktur: ", end='')
        for i in res[:-1]:
            print(f"{i} - ", end='')
        print(res[-1], "\n")

        return True, res 
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" tidak memiliki struktur yang sesuai\n")
        return False, res
