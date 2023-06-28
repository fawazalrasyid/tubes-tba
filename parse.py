def parser(tokens):
    # Inisialisasi variabel
    index = 0  # Indeks token saat ini
    current_token = None  # Token saat ini
    error = False  # Menyimpan status kesalahan

    # Fungsi untuk mencocokkan token saat ini dengan token yang diharapkan
    def match(expected_token):
        nonlocal current_token, error
        if current_token == expected_token:
            consume()  # Consume token saat ini
        else:
            error = True  # Kesalahan jika token tidak cocok dengan yang diharapkan

    # Fungsi untuk consume token saat ini dan pindah ke token berikutnya
    def consume():
        nonlocal index, current_token
        index += 1  # Meningkatkan indeks
        if index < len(tokens):
            current_token = tokens[index]  # Mendapatkan token berikutnya
        else:
            current_token = None  # Jika sudah mencapai akhir, set token saat ini ke None

    # Fungsi untuk meng-handle operasi dalam formula
    def operasi():
        term()
        operasi_loop()

    # Fungsi rekursif untuk meng-handle loop operasi dalam formula
    def operasi_loop():
        if current_token in [3, 4, 5, 6, 7]:
            operator()
            term()
            operasi_loop()

    # Fungsi untuk meng-handle term dalam formula
    def term():
        faktor()
        term_loop()

    # Fungsi rekursif untuk meng-handle loop term dalam formula
    def term_loop():
        if current_token == 4:
            operator_minus()
            faktor()
            term_loop()

    # Fungsi untuk meng-handle faktor dalam formula
    def faktor():
        nonlocal error
        if current_token in [1, 2]:
            operan()
        elif current_token == 9:
            grup()
        elif current_token == 8:
            absolut()
        else:
            error = True  # Kesalahan jika token tidak dikenali

    # Fungsi untuk meng-handle operan dalam formula
    def operan():
        match(current_token)

    # Fungsi untuk meng-handle grup dalam formula
    def grup():
        match(9)
        operasi()
        match(10)

    # Fungsi untuk meng-handle operasi absolut dalam formula
    def absolut():
        match(8)
        operasi()
        match(8)

    # Fungsi untuk meng-handle operator dalam formula
    def operator():
        nonlocal error
        if current_token in [3, 4, 5, 6, 7]:
            match(current_token)
        else:
            error = True  # Kesalahan jika token operator tidak dikenali

    # Fungsi untuk meng-handle operator minus dalam formula
    def operator_minus():
        match(4)

    current_token = tokens[index]
    operasi()

    # Memeriksa apakah formula valid atau tidak
    if not error and current_token is None:
        return "Formula valid"
    else:
        return "Formula tidak valid"
