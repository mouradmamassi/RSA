from crypto import *
import linecache

#recuperation des donnees necessaires pour B
pb = int(linecache.getline('donneesB.txt', 1))
pb = int(pb)
qb = int(linecache.getline('donneesB.txt', 2))
qb = int(qb)
nb = int(linecache.getline('donneesB.txt', 3))
nb = int(nb)
eb = linecache.getline('donneesB.txt', 4)
eb = int(eb)
db = linecache.getline('donneesB.txt', 5)
db = int(db)
na = int(linecache.getline('donneesA.txt', 3))
na = int(na)
ea = linecache.getline('donneesA.txt', 4)
ea = int(ea)
