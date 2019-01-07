def encrypt_caesar(plaintext):
    """
        Encrypts plaintext using a Caesar cipher.

        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
        """
    global z
    cliphertext = ''
    for ch in plaintext:
        if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
            z = ord(ch)+3
            if z > ord('Z') and z < ord('a') or z > ord('z'):
                z -= 26
        cliphertext += chr(z)
    return cliphertext



def decrypt_caesar(cliphertext):
    """
       Decrypts a ciphertext using a Caesar cipher.

       >>> decrypt_caesar("SBWKRQ")
       'PYTHON'
       >>> decrypt_caesar("sbwkrq")
       'python'
       >>> decrypt_caesar("Sbwkrq3.6")
       'Python3.6'
       >>> decrypt_caesar("")
       ''
       """
    global z
    plaintext = ''
    for ch in cliphertext:
        if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
            z = ord(ch) + 3
            if z > ord('Z') and z < ord('a') or z > ord('A'):
                z += 26
        plaintext += chr(z)
    return plaintext
