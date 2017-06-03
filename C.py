from crypto import *

#C genere la cle privee et publique de A
pa = randomPrime()
qa = randomPrime()
na = pa*qa
ea = e_generator(pa,qa)
da = d_generator(pa,qa,ea)

#C genere la cle privee et publique de B
pb = randomPrime()
qb = randomPrime()
nb = pb*qb
eb = e_generator(pb,qb)
db = d_generator(pb,qb,eb)

fa = open('donneesA.txt', 'w')
fa = open('donneesA.txt', 'a')
fa.write(str(pa) + "\n")
fa.write(str(qa) + "\n")
fa.write(str(na) + "\n")
fa.write(str(ea) + "\n")
fa.write(str(da) + "\n")
fa.close()

fb = open('donneesB.txt', 'w')
fb = open('donneesB.txt', 'a')
fb.write(str(pb) + "\n")
fb.write(str(qb) + "\n")
fb.write(str(nb) + "\n")
fb.write(str(eb) + "\n")
fb.write(str(db) + "\n")
fb.close()