def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, ch in enumerate(plaintext):
        ch1 = ord(ch)
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            x = index % len(keyword)
            shift = ord(keyword[x])
            if 'a' <= ch <= 'z':
                shift -= ord('a')
            else:
                shift -= ord('A')
            ch1 = ord(ch) + shift
            if 'a' <= ch <= 'z' and ch1 > ord('z'):
                ch1 -= 26
            if 'A' <= ch <= 'Z' and ch1 > ord('Z'):
                ch1 -= 26
        ciphertext += chr(ch1)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for index, ch in enumerate(ciphertext):
        ch1 = ord(ch)
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            x = index % len(keyword)
            shift = ord(keyword[x])
            if 'a' <= ch <= 'z':
                shift -= ord('a')
            else:
                shift -= ord('A')
            ch1 = ord(ch) - shift
            if 'a' <= ch <= 'z' and ch1 > ord('z'):
                ch1 += 26
            if 'A' <= ch <= 'Z' and ch1 > ord('Z'):
                ch1 += 26
        plaintext += chr(ch1)
    return plaintext
