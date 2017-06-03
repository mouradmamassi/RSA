import random
dico = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", " ", ".", ",", "'", "!", "?"]
list_prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# fonction permettant de transformer un caractere du dico en un nombre binaire a 5 digits contenu dans une liste
def encrypt_binaire(lettre : str) :

    # initialisation des variables

    resInt = 0
    resList = []

    # si l'entree n'est pas dans le dico on renvoie un message d'erreur

    if lettre not in dico :
        return print('Erreur, caractere non autorise')

    # parcours de dico et conversion en binaire

    for element in dico :
        if element == lettre:
            resInt = bin(dico.index(element))[2:]

    # stockage du nombre binaire dans une liste

    for i in range(5) :
        resList = [int(i) for i in resInt]

    # on verifie que notre reultat est bien compose de 5 digits

    while len(resList) !=5 :
        resList = [0] + resList

    # renvoie de la liste d'entiers contenant le nombre binaire voulu

    return resList

def decrypt_binaire(aDecrypter : list) :

    # conversion de aDecrypter en chaine de caracteres

    chaine=''.join(str(digit) for digit in aDecrypter)

    # conversion en decimal de chaine

    indice = int(chaine,2)

    # test si aDecrypter appartient a la liste

    if indice > 31 :
        return print("Erreur, le caractere a crypter n'est pas un caractere")
    else :
        return dico[indice]

# fonction qui effectue un decalage binaire a gauche de Msg puis un XOR avec la cle Key
def function(Msg : str, Key : str) :
    bin = encrypt_binaire(Msg[0]) + encrypt_binaire(Msg[1])
    for i in range (len(bin)-1) :
        temp = bin[i]
        bin[i] = bin[i+1]
        bin[i+1] = temp

    binKey = encrypt_binaire(Key[0]) + encrypt_binaire(Key[1])
    l=[0*j for j in range (len(bin))]
    for i in range (len(bin)) :
        l[i] = bin[i] ^ binKey[i]

    return l

# Crypter 2 caracteres en binaire contenu dans une liste de 10 entiers
def encrypt_2_char(msg:str):
    return encrypt_binaire(msg[0]) + encrypt_binaire(msg[1])

#Decrypter  une liste de 10 entiers binaires en 2 caracteres
def decrypt_list_bin(l:list):
    j = 0
    # deux listes [0,0,0,0,0]
    bin1, bin2 = [0*k for k in range (5)], [0*k for k in range (5)]
    for i in range (10): #parcourir la liste d'entree
        if i <= 4 :
            bin1[i] = l[i] #recuperer les 5 premiers elements
        elif i > 4 :
            bin2 [j] = l [i] #recuperer les 5 derniers elements
            j= j + 1
    return decrypt_binaire(bin1) + decrypt_binaire(bin2)


#fonction de cryptage Feistel
def encrypt_Feistel(Msg:str, Key:str):
    k1, k2, k3, k4 = Key[:2], Key[1:3], Key[2:], Key[3] + Key[0]
    g0, d0 = Msg[:2], Msg[2:]
    bin1, bin2 = [0 * w for w in range(5)], [0 * w for w in range(5)]
    bin = [0 * w for w in range(10)]


    #Tour 1
    x1 = d0
    y1 = g0
    bin1 = encrypt_2_char(y1)
    bin2 = function(x1,k1)
    for i in range (10):
        bin[i] = bin1[i] ^ bin2[i]

    #Tour 2
    x2 = decrypt_list_bin(bin)
    y2 = x1
    bin1 = encrypt_2_char(y2)
    bin2 = function(x2,k2)
    for j in range (10):
        bin[j] = bin1[j] ^ bin2[j]

    #Tour 3
    x3 = decrypt_list_bin(bin)
    y3 = x2
    bin1 = encrypt_2_char(y3)
    bin2 = function(x3,k3)
    for k in range (10):
        bin[k] = bin1[k] ^ bin2[k]

    #Tour 4
    x4 = decrypt_list_bin(bin)
    y4 = x3
    bin1 = encrypt_2_char(y4)
    bin2 = function(x4,k4)
    for l in range (10):
        bin[l] = bin1[l] ^ bin2[l]
    x5 = decrypt_list_bin(bin)

    return x4+x5

#fonction de decryptage Feistel
def decrypt_Feistel(Msg:str, Key:str):
    k4, k3, k2, k1 = Key[:2], Key[1:3], Key[2:], Key[3] + Key[0]
    g0, d0 = Msg[:2], Msg[2:]
    bin1, bin2 = [0 * w for w in range(5)], [0 * w for w in range(5)]
    bin = [0 * w for w in range(10)]


    #Tour 1
    y1 = d0
    x1 = g0
    bin1 = encrypt_2_char(y1)
    bin2 = function(x1,k1)
    for i in range (10):
        bin[i] = bin1[i] ^ bin2[i]

    #Tour 2
    x2 = decrypt_list_bin(bin)
    y2 = x1
    bin1 = encrypt_2_char(y2)
    bin2 = function(x2,k2)
    for j in range (10):
        bin[j] = bin1[j] ^ bin2[j]

    #Tour 3
    x3 = decrypt_list_bin(bin)
    y3 = x2
    bin1 = encrypt_2_char(y3)
    bin2 = function(x3,k3)
    for k in range (10):
        bin[k] = bin1[k] ^ bin2[k]

    #Tour 4
    x4 = decrypt_list_bin(bin)
    y4 = x3
    bin1 = encrypt_2_char(y4)
    bin2 = function(x4,k4)
    for l in range (10):
        bin[l] = bin1[l] ^ bin2[l]
    x5 = decrypt_list_bin(bin)

    return x5+x4


#fonction qui cherche l'indice du caractere dans la liste
def find_dec(c : str):
    for i in range(len(dico)):
        if c == dico[i] :
            return i
    ##return 0

#fonction qui renvoie la liste des indices correspondant ÃƒÆ’Ã‚Â  chaque caractere du string passe en entree
def str2dec(s : str):
    l=[0*i for i in range(4)]
    for i in range(4):
        l[i] = find_dec(s[i])
    return l

#fonction qui convertie un decimal en chaine de caratere
def dec2str(l : list):
    s=""
    for i in range(4):
        s = s + dico[l[i]]
    return s

#fonction qui calcule l'exponentiation modulaire d'un message m (sous forme de liste d'indice)
#et l'a renvoie sous la meme forme
def puiss_mod(m, e, n):
    """ m est une liste d'entiers contenant des indices de caracteres contenu dans le dico
        e cle publique
        n = pq pour aller aux toilettes
    """
    indice = 0
    r = [0,0]
    res = [0*i for i in range(4)]
    for i in range(4):
        dec = e
        r[0] = 1
        r[1] = m[indice]
        while dec > 0 :
            if dec % 2 == 1 :
                r[0] = (r[0] * r[1]) % n
            dec = dec // 2
            r[1] = (r[1] * r[1]) % n
        res[indice] = r[0]
        if indice <= 3 : indice = indice + 1
    return res

#genere un nombre aleatoire modulo 32
def rand_num():
    return random.randint(0,1000) % 32

#fonction qui genere une cle de 4 caracteres sous de string
def key_generator():
    res = ''
    for i in range (4) :
        res += dico[rand_num()%32]
    return res

#fonction qui convertit un nombre binaire (sous forme de liste de 0 et de 1) en un entier (en base 10)
def bin2dec(m : list):
    puiss = 4
    dec = 0
    for i in range(5):
        if m[i] == 1:
            dec = dec + m[i] * pow(2, puiss)
        puiss = puiss - 1
    return dec

# fonction permettant d'afficher sous forme de string un message crypte par encryptRSA
def print_crypt(C : list):
    res = ''
    for i in range (4) :
        res += dico[C[i]%32]
    return res

#cryptage RSA
def encryptRSA(m : str, n : int, e : int):
    M = str2dec(m)
    C = puiss_mod(M, e, n)
    return C

#decryptage RSA
def decryptRSA(C : list, n : int, d : int):
    D = puiss_mod(C, d, n)
    M = ""
    for i in range(4):
        M += dico[D[i]]
    return M

#Programme de calcul du pgcd
def pgcd(a, b) :
   while a % b != 0 :
      a, b = b, a % b
   return b

#Genere un nombre aleatoire modulo n
def rand_num_mod(n:int):
    return (rand_num() % n)

#Genere la cle publique e a partir de p et q
def e_generator(p : int, q : int):
    phi_n = (p - 1) * (q - 1)
    e = rand_num_mod(phi_n)
    test = True;
    while(test):
        if e > 0 and e < phi_n and pgcd(e,phi_n) == 1 :
            test = False
        else:
            e=rand_num_mod(phi_n)
    return e

#Algo euclide etendu
def euclide_extended(a,b):
    x = 1 ; xx = 0 # U0,U1
    y = 0 ; yy = 1 # V0,V1
    while b != 0 :
        q = a // b
        a , b = b , a % b
        xx , x = x - q*xx , xx
        yy , y = y - q*yy , yy
    return (a,x,y)

#Calcul de d la cle privee
def d_generator(p,q,e):
    n=p*q
    phi=(p-1)*(q-1)
    c,d,dd = euclide_extended(e,phi)
    return (d % phi)


#Genere un nombre premier a  partir de la fonction prime [2,......97]
def randomPrime():
    return random.choice([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])

def password_generator(key:str):
    bin1 = encrypt_2_char("AB")
    bin2 = encrypt_2_char("OK")
    binkey1 = encrypt_2_char(key[:2])
    binkey2 = encrypt_2_char(key[2:])
    l1 = [0*i for i in range (10)]
    l2 = [0 * i for i in range(10)]
    for i in range (len(bin1)):
        l1[i] = bin1[i] ^ binkey1[i]
    for i in range (len(bin2)):
        l2[i] = bin2[i] ^ binkey2[i]
    return decrypt_list_bin(l1)+decrypt_list_bin(l2)


