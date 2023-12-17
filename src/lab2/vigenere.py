def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    alf = 'abcdefghijklmnopqrstuvwxyz' * 10
    ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 10
    ciphertext = ""

    if len(keyword) == 1:
        for index in range(len(plaintext)):
            if plaintext[index] in '-,. ':
                ciphertext = ciphertext + plaintext[index]
            if plaintext[index] in alf:
                ciphertext = ciphertext + alf[alf.find(plaintext[index]) + ALF.find(keyword.upper())]
            if plaintext[index] in ALF:
                ciphertext = ciphertext + ALF[ALF.find(plaintext[index]) + ALF.find(keyword.upper())]
    elif len(keyword) > 1:
        keyword = keyword * 10
        for index in range(len(plaintext)):
            if plaintext[index] in '-,. ':
                ciphertext = ciphertext + plaintext[index]
            if plaintext[index] in alf:
                ciphertext = ciphertext + alf[alf.find(plaintext[index]) + ALF.find(keyword[index].upper())]
            if plaintext[index] in ALF:
                ciphertext = ciphertext + ALF[ALF.find(plaintext[index]) + ALF.find(keyword[index].upper())]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    alf = 'abcdefghijklmnopqrstuvwxyz' * 10
    ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 10
    plaintext = ""

    if len(keyword) == 1:
        for index in range(len(ciphertext)):
            if ciphertext[index] in '-,. ':
                plaintext = plaintext + ciphertext[index]
            elif ciphertext[index] in alf:
                plaintext = plaintext + alf[alf.find(ciphertext[index]) - ALF.find(keyword.upper())]
            elif ciphertext[index] in ALF:
                plaintext = plaintext + ALF[ALF.find(ciphertext[index]) - ALF.find(keyword.upper())]
    elif len(keyword) > 1:
        keyword = keyword * 10
        for index in range(len(ciphertext)):
            if ciphertext[index] in '-,. ':
                plaintext = plaintext + ciphertext[index]
            elif ciphertext[index] in alf:
                plaintext = plaintext + alf[alf.find(ciphertext[index]) - ALF.find(keyword[index].upper())]
            elif ciphertext[index] in ALF:
                plaintext = plaintext + ALF[ALF.find(ciphertext[index]) - ALF.find(keyword[index].upper())]
    return plaintext