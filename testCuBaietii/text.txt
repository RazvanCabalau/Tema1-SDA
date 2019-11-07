from itertools import chain, combinations
import collections
import random

n = 9 #random.randint(8, 12)
v = [7, 2, 4, 8, 3, 5, 9, 10, 1]#random.sample(range(12), n)
numberOfSteps = 2 #random.randint(2, (n -1) // 2)

minAnte = 0 # pt ca genram pana nr la 12

sterse = []
print(v)
while len(sterse) <= numberOfSteps:
    minim = 13
    pozMin = 0
    for i in range(n - len(sterse)):
        if (minim > v[i] and v[i] > minAnte):
            minim = v[i]    
            pozMin = i
    minAnte = minim
    print ("minAnte = ", minAnte)
    if pozMin > numberOfSteps + len(sterse): #prea multe elem in stanga
        sterse.append(minim)
        for i in  range (pozMin + 1, n - len(sterse) + 1):
            v[i] = v[i+1]
    else:
        if(pozMin!=0):
            for i in range (pozMin):
                if len(sterse) <= numberOfSteps and v[i] > minim:
                    sterse.append(v[i])
                    for j in  range (i, n - len(sterse) ):
                        v[j] = v[j+1]
    print(v[0:n-len(sterse)])
    print("Sterse: ", sterse)
print(sterse)
    

