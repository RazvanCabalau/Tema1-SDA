#am facut o parte din rezolvare
#nu cred ca e cea mai eficienta posibil
#mai sunt inca multe lucruri de facut

from itertools import chain, combinations
import collections
import random
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    #codul asta l-am primit pe mail de la prof, genereaza combinari de n luate cate m
    #adica in cazul nostru partitiile vectorului

def sorted (v):
    n = len (v)
    for i in range (n - 1):
        if v[i] > v[i + 1]:
            return 0
    return 1


def minMaxPositions (v, min, max):
    pozMin = 0
    pozMax = 0
    for i in range (len(v)):
        if min == v[i]:
            pozMin = i
        if max == v[i]:
            pozMax = i
    return (pozMin, pozMax)

n = random.randint(8, 12)
v = random.sample(range(12), n)
numberOfSteps = random.randint(2, n // 2)
keep = []
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
#asta e o functie lamnda, o folosesc ca sa gasesc sirurile generate in vectorul v

for subset in powerset(v):
    if (len(subset) == numberOfSteps and sorted(subset)):
        subset = list(subset)
        keep.append(subset)
ok = False
    # pun in keep toate sirurile sortate si care sunt de lungima ceruta in cerinta
subsets = []
for i in range (len(v) - numberOfSteps):
    for subset in keep:
        if compare (v[i : i+len(subset)], subset) == True:
            subsets.append(subset)
            ok = True
                #am spus mai sus de ce folosesc subsets
    #print(subsets)
keep.clear()
if ok == False:
    print ("In vector nu exista o submultime ordonata de dimensiune", numberOfSteps)
else:
    subset = subsets[0]
    minFirstSubset = subset[0]
    maxFirstSubset = subset[numberOfSteps - 1]
    print("\nSirul initial:", v)
    print ("\nSubmultimea obtinuta dupa", numberOfSteps, "pasi prin algoritmul de sortare prin selectia minimului este", subset)
    # stiu ca in subset o sa am sirul de numere sortat crescator
    #pastrez prima si ultima valoare ca fiind mariginile intervalelor

    elemDeleted = []
    sters = [0] * len(v)
    (pozMin, pozMax) = minMaxPositions(v, minFirstSubset, maxFirstSubset)

    nrElemDeleted = 0
    while (v[nrElemDeleted] != minFirstSubset): #sterge toate elementele care se afla inainte de minimul din secventa
        elemDeleted.append(v[nrElemDeleted])
        sters [nrElemDeleted] = 1
        nrElemDeleted += 1
    
    #print(elemDeleted)
    for i in range (nrElemDeleted + len(subset), len(v)): #aici sterg elementele care nu sunt in secventa si sunt mai mici decat minimul din secventa
        if (v[i] < minFirstSubset and sters[i] != 1):
            elemDeleted.append(v[i])
            sters[i] = 1
    #print(elemDeleted)
    for i in range(nrElemDeleted + len(subset), len(v)):
        if (len(elemDeleted) == numberOfSteps):
            break
        if (sters[i] != 1):
            if (v[i] < minFirstSubset):
                elemDeleted.append(v[i])
                sters[i] = 1
                print (v[i])
                continue
            if (v[i] > minFirstSubset and v[i] < maxFirstSubset):
                elemDeleted.append(v[i])
                sters[i] = 1
                print(v[i])
    print("\nNumarul minim de elemente pe care trebuie sa le stergem:", len(elemDeleted))
    print ("\nElementele pe care le-am sters:", elemDeleted)
#asta e prima abordare    
# for i in range (len(v)):
#     if (v[i] < minFirstSubset and i > pozMin):
#         elemDeleted.append(v[i])
#     if (v[i] > minFirstSubset and i < pozMin):
#         elemDeleted.append(v[i])
#     if (v[i] > minFirstSubset and v[i] < maxFirstSubset and i > pozMax):
#         elemDeleted.append(v[i])
    
    #am explicat in idei.txt ce vreau sa fac in forul asta, in principal asta e partea cea mai importanta din tema
    #

#varianta de mai sus e pentru 10

#pentru 11 tebuie sa facem cu backtraking, adica sa generam noi toate subsirurile alea
#cred ca in rest s-ar portivii foarte bine si pe varianta asta





#def valid (v, k):
#    for i in range (len(v) - 1):
#        if v[i] == v[k-1]:
#            return 0
#    return 1

#def backTracking (v):
#    k = 0
#    n = len(v)
#    partition = [0] * n
#    while k>=0:
#        partition[k] = 1
#        print (valid(partition, k))
#        if (valid(partition, k)):
#            if k == n:
#                print(v[:k])
#            else:
#                k +=1
#        else:
#             k -= 1

#print ("Metoda mea:")
#backTracking (v)

