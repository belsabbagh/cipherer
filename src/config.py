from cryptexia.cryptexia.ciphers.classic import Caesar, Playfair, Hill, Vigenere, Vernam


CIPHERS = {
    "Caesar": {
        "class": Caesar,
        "hint": "Key is a number between 0 and 25",
    },
    "Playfair": {
        "class": Playfair,
        "hint": "Key is a string of letters. Preferably 5-10 unique letters.",
    },
    "Hill": {
        "class": Hill,
        "hint": "Key is a square matrix of numbers written in CSV format.",
    },
    "Vigenere": {
        "class": Vigenere,
        "hint": "Key is a string of letters.",
    },
    "Vernam": {
        "class": Vernam,
        "hint": "Key is a string of letters.",
    },
}
