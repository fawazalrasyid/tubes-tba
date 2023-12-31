import re

# Pola regex untuk setiap token
lexical_dict = {
    r"-?\d+\.\d+": ("Operan", 2),   # Bilangan riil
    r"-?\d+": ("Operan", 1),        # Bilangan bulat
    r"\+": ("Operator", 3),         # Operator penjumlahan
    r"-": ("Operator", 4),          # Operator pengurangan
    r"x": ("Operator", 5),          # Operator perkalian
    r":": ("Operator", 6),          # Operator pembagian
    r"\^": ("Operator", 7),         # Operator pemangkatan
    r"\|": ("Operator", 8),         # Operator absolut
    r"\(": ("Grouping", 9),         # Kurung buka
    r"\)": ("Grouping", 10),        # Kurung tutup
}

def lexical_analyzer(formula):
    tokens = []
    lexems = re.findall(r"-?\d+\.\d+|-?\d+|\S", formula)
    
    # Memproses setiap leksem dalam formula
    for lexem in lexems:
        matched = False
        # Memeriksa pola regex untuk setiap leksem dan menambahkan token ke dalam daftar
        for pattern, (lex_type, token) in lexical_dict.items():
            if re.match(pattern, lexem):
                tokens.append(token)
                matched = True
                break
        # Jika leksem tidak cocok dengan pola regex, tambahkan "error" ke dalam daftar
        if not matched:
            tokens.append("error")
    
    return tokens
