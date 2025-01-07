def feistel_round(bits, k):
    assert len(bits) == 8
    assert len(k) == 4

    L = int(bits[:4], 2)
    R = int(bits[4:], 2)
    key = int(k, 2)
    
    Rwithk = (2 * (R ^ key)) % 16
    
    L1 = R
    R1 = L ^ Rwithk
    
    L1binary = format(L1, '04b')
    R1binary = format(R1, '04b')
    
    return R1binary + L1binary

def strtobin(t):
    return ''.join(format(ord(c), '08b') for c in t)

def bintostr(binstr):
    char = [chr(int(binstr[i:i+8], 2)) for i in range(0, len(binstr), 8)]
    return ''.join(char)


def feistelcipher(t, k):
    bin = strtobin(t)
    result = ""

    for i in range(0, len(bin), 8):
        bit = bin[i:i+8]
        result += feistel_round(bit, k)
    return bintostr(result)

plaintext = input("String: ")
key = input("4-bit Key: ")
ciphertext = feistelcipher(plaintext, key)
print("Ciphertext:", ciphertext)
