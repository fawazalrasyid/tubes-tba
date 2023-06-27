def parser(tokens):
    # Inisialisasi variabel
    current_token = None  # Token saat ini
    index = -1  # Indeks token saat ini
    error = False  # Menyimpan status kesalahan

    # Pindah ke token berikutnya
    def advance():
        nonlocal index, current_token
        index += 1
        if index < len(tokens):
            current_token = tokens[index]
        else:
            current_token = None

    # Mem-parsing ekspresi
    def expression():
        term()
        while current_token in [3, 4]:
            advance()
            term()

    # Mem-parsing term
    def term():
        factor()
        while current_token in [5, 6, 7, 8]:
            advance()
            factor()

    # Mem-parsing faktor
    def factor():
        nonlocal error
        if current_token in [1, 2]:
            advance()
        elif current_token == 9:
            advance()
            expression()
            if current_token == 10:
                advance()
            else:
                error = True
        else:
            error = True

    # Memulai parsing
    advance()
    expression()

    # Memeriksa apakah formula valid atau tidak
    if not error and current_token is None:
        return "Formula valid"
    else:
        return "Formula tidak valid"
