def generate_key_matrix(k):
    k =k.upper()
    mat = [[0 for i in range (5)] for j in range(5)]
    alphabetsIn = []
    r = 0
    c = 0

    for alphabet in k:
        if alphabet not in alphabetsIn:
            mat[r][c] = alphabet
            alphabetsIn.append(alphabet)
        else:
            continue
        if (c==4):
            c = 0
            r += 1
        else:
            c += 1

    for alphabet in range(65,91):
        if alphabet==74:# Replace 'j' with 'i'
            continue
        if chr(alphabet) not in alphabetsIn:
            alphabetsIn.append(chr(alphabet))
            

    a = 0
    for i in range(5):
        for j in range(5):
            mat[i][j] = alphabetsIn[a]
            a+=1
    return mat
    

def x_generater(str):
    i = 0
    while (i<len(str)):
        firLetter = str[i]
        if i == len(str)-1:
            str = str + 'X'
            i += 2
            continue
        secLetter = str[i+1]
        if firLetter==secLetter:
            str = str[:i+1] + "X" + str[i+1:]
        i +=2   
    return str
    

def find_position(alphabet,mat):
    for i in range (5):
        try:
            num = mat[i].index(alphabet)
            return (i,num)
        except:
            continue

def Encrypt(Plaintext,mat):
    Plaintext = Plaintext.upper()
    Plaintext = Plaintext.replace(' ','')    
    Plaintext = x_generater(Plaintext)
    encrypted=''
    for (firLetter, secLetter) in zip(Plaintext[0::2], Plaintext[1::2]):
        r1,c1 = find_position(firLetter,mat)
        r2,c2 = find_position(secLetter,mat)
        if r1==r2: # Same row: move right
            encrypted += mat[r1][(c1+1)%5] + mat[r2][(c2+1)%5]
        elif c1==c2:# Same column: move down
            encrypted += mat[(r1+1)%5][c1] + mat[(r2+1)%5][c2]
        else: # Rectangle swap
            encrypted += mat[r1][c2] + mat[r2][c1]
    
    print(encrypted)
    
def Decrypt(Ciphertext,key):
    mat = generate_key_matrix(key)
    Ciphertext = Ciphertext.upper()
    Ciphertext = Ciphertext.replace(' ','')    
    Ciphertext = x_generater(Ciphertext)
    decrypted=''
    for (firLetter, secLetter) in zip(Ciphertext[0::2], Ciphertext[1::2]):
        r1,c1 = find_position(firLetter,mat)
        r2,c2 = find_position(secLetter,mat)
        if r1==r2: # Same row: move left
            decrypted += mat[r1][(c1-1)%5] + mat[r2][(c2-1)%5]
        elif c1==c2:# Same column: move up
            decrypted += mat[(r1-1)%5][c1] + mat[(r2-1)%5][c2]
        else: # Rectangle swap
            decrypted += mat[r1][c2] + mat[r2][c1]
    
    print(decrypted)
    

def test_playfiar():
    k = input("Keyword: ")
    #k = "binary"
    k_mat = generate_key_matrix(k)
    print("Key Matrix:")
    for r in k_mat:
        print(r)
    
    Plaintext = str(input("Plain text:"))
    Plaintext = Plaintext.lower()
    Encrypt(Plaintext,k_mat)
    
    Ciphertext = str(input("Cipher text:"))
    Ciphertext = Ciphertext.lower()
    Decrypt(Ciphertext,k)

test_playfiar()