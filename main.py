from crypto import *
from A import *
from B import *
import sys

################################  Question 1.a  #################################

print("\n")
print("********************  Cryptage du message d'identification par A   *********************")
msgA = "AB?!"
print("Le message que A veut envoyer a B est :", msgA)

# A crypte son message en utilisant la cle publique de B
msgA_crypte = encryptRSA(msgA,nb,eb)
print("Le message crypte par A est :", print_crypt(msgA_crypte))


################################  Question 1.b  #################################

print("\n")
print("********************  Decryptage du message d'identification par B   *********************")
msgA_decrypte = decryptRSA(msgA_crypte,nb,db)
print("Le message decrypte par B est :", msgA_decrypte)
print("\n")

################################  Question 2.a  #################################

# on verifie que B recoit le bon message de la part de A
if msgA != msgA_decrypte:
    print("B n'a pas reçu le bon message... fin du programme")
    sys.exit()

print("********************  Cryptage du message de confirmation par B   *********************")
msgB = "ABOK"
print("Le message que B veut envoyer a A est :", msgB)


# B crypte son message en utilisant la cle publique de A
msgB_crypte = encryptRSA(msgB,na,ea)
print("Le message crypte par B est :", print_crypt(msgB_crypte))
print("\n")


################################  Question 2.b  #################################
print("********************  Decryptage du message de confirmation par A   *********************")
msgB_decrypte = decryptRSA(msgB_crypte,na,da)
print("Le message decrypte par A est :", msgB_decrypte)
print("\n")

################################  Question 3.a  #################################

# on verifie que A recoit le bon message de la part de B
if msgB != msgB_decrypte:
    print("A n'a pas reçu le bon message... fin du programme")
    sys.exit()
print("********************  Cryptage du message de A par A   *********************")
rand_msgA = key_generator()
print("A genere aleatoirement le message :",rand_msgA)

# A crypte le message genere aleatoirement en utilisant la cle publique de B
rand_msgA_crypte = encryptRSA(rand_msgA,nb,eb)
print("Le cryptage du message genere aleatoirement par A est :", print_crypt(rand_msgA_crypte))


################################  Question 3.b  #################################
print("\n")
print("********************  Decryptage du message de A par B   *********************")
rand_msgA_decrypte = decryptRSA(rand_msgA_crypte,nb,db)
print("Le decryptage par B du message aleatoire envoye par A est :", rand_msgA_decrypte)
print("\n")

################################  Question 3.c  #################################
print("********************  Cryptage du message de A par B   *********************")
# B crypte le message recu en utilisant la cle publique de A
rand_msgB_crypte = encryptRSA(rand_msgA_decrypte,na,ea)
print("Le message recu crypte par B avec la cle publique de A est :", print_crypt(rand_msgB_crypte))
print("\n")

################################  Question 3.d  #################################

print("********************  Decryptage et verification de la reception par A  *********************")
rand_msgB_decrypte = decryptRSA(rand_msgB_crypte,na,da)
print("Le message decrypte par A pour verifier que B a bien recu son message precedent est :", rand_msgB_decrypte)


if rand_msgA != rand_msgB_decrypte :
    print("Le message recu par A est different de celui qu'il avait envoye... fin du programme ")
    sys.exit()
print("Le message recu par A est bien celui qu'il avait envoye")
print("\n")


################################  Question 4   #################################
print("*************************  Mot de passe de A  *************************")
passA = password_generator(rand_msgA)
print("Mot de passe genere par A est : ",passA)
print("\n")

print("*************************  Mot de passe de B  *************************")
rand_msgB = key_generator()
print("B genere aleatoirement le message : ",key_generator())


passB = password_generator(rand_msgB)
print("Mot de passe genere par B est : ",passB)
print("\n")

################################  Question 5   #################################
print("*************************  Cryptage du message par A  *************************")

txt_crypte = encrypt_Feistel(passA,"KXCX")

print("Le message texte crypte par A par la methode FEISTEL est :" , txt_crypte)
print("\n")


################################  Question 6   #################################
print("*********************  Decryptage du message par A par B  *********************")
print("Le message texte de A decrypte par B est :" , decrypt_Feistel(txt_crypte,"KXCX"))