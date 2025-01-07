import random
from math import gcd

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primeGenerator():
    p = [int for int in range(100, 1001) if isPrime(int)]
    return p

def mod(A, M):
    m1, x1, x2 = M, 0, 1
    if M == 1:
        return 0
    while A > 1:
        Q = A // M
        M, A = A % M, M
        x1, x2 = x2 - Q * x1, x1
    if x2 < 0:
        x2 += m1
    return x2

def KeyGen(primeList):
    prime1, prime2 = random.sample(primeList, 2)
    print("Chosen Prime: ",prime1,",",prime2)

    modulus = prime1 * prime2
    phN = (prime1 - 1) * (prime2 - 1)

    public_exp = random.choice([int for int in range(2, phN) if gcd(int, phN) == 1])
    private_exp = mod(public_exp, phN)

    Public_Key = (public_exp, modulus)
    Private_Key= (private_exp, modulus)

    print("Public Key: ", Public_Key)
    print("Private Key: ", Private_Key)
    
    return Public_Key, Private_Key

def RSA_Algorithm(M, key):
    exp, N = key
    return pow(M, exp, N)

def StrToAscii(s):
    return [ord(character) for character in s]

def asciiToStr(a):
    return ''.join(chr(character) for character in a)

p = primeGenerator()
Public_Key, Private_Key = KeyGen(p)

String = input("String: ")
ascii = StrToAscii(String)

encrypt = [RSA_Algorithm(code, Public_Key) for code in ascii]
decrypt = [RSA_Algorithm(code, Private_Key) for code in encrypt]

decryption = asciiToStr(decrypt)

print("Encrypt :", encrypt)
print("Decrypt :", decryption)