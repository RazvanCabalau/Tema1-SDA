from itertools import chain, combinations
import collections
import random
n = 6
v = [3, 6, 5, 4, 7, 2]#[7, 2, 4, 8, 3, 5, 9, 10, 1]
numberOfSteps = 1
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def sorted (v):
    n = len (v)
    for i in range (n - 1):
        if v[i] > v[i + 1]:
            return 0
    return 1

def eliminSelectMinim (subset):
    primul = subset[0]
    ultimul = subset [len(subset) -1]
    sterse = []
    for i in range(len(v)):
        if v[i] in subset:
            continue
        if v[i] < primul:
            sterse.append(v[i])
            continue
        if v[i] > ultimul and i < v.index(ultimul):
            sterse.append(v[i])
            continue
        if v[i] > primul and v[i] < ultimul:
            sterse.append(v[i])
            continue
    return sterse

def eliminSelectMaxim (subset):
    primul = subset[0]
    ultimul = subset [len(subset) -1]
    sterse = []
    for i in range(len(v)):
        if v[i] in subset:
            continue
        if v[i] > ultimul:
            sterse.append(v[i])
            continue
        if v[i] < primul and i > v.index(primul):
            sterse.append(v[i])
            continue
        if v[i] < ultimul and i > v.index(ultimul):
            sterse.append(v[i])
            continue
        if v[i] > primul and v[i] < ultimul:
            sterse.append(v[i])
            continue
        
    return sterse  

def eliminInsertie (subset):
    primul = subset[0]
    ultimul = subset [len(subset) -1]
    sterse = []
    for i in range(v.index(ultimul)):
        if v[i] in subset:
            continue
        if v[i] < primul:
            sterse.append(v[i])
            continue
        if v[i] > ultimul:
            sterse.append(v[i])
            continue
        if v[i] > primul and v[i] < ultimul:
            sterse.append(v[i])
            continue
    return sterse

keep = []
keepInsertie = []
for subset in powerset(v):
    if (len(subset) == numberOfSteps and sorted(subset)):
        subset = list(subset)
        keep.append(subset)
    if (len(subset) == numberOfSteps + 1 and sorted(subset)):
        subset = list(subset)
        keepInsertie.append(subset)

arr = []
minimSterse = []
min = len(v)
for elem in keep:
    arr = eliminSelectMinim(elem)
    #print(elem, ":" ,arr)
    if len(arr) < min:
        min = len(arr)
        minimSterse = arr
print(min, minimSterse)

arr2 = []
minimSterse2 = []
min2 = len(v)
for elem in keep:
    arr2 = eliminSelectMaxim(elem)
    #print(elem, ":" ,arr2)
    if len(arr2) < min2:
        min2 = len(arr2)
        minimSterse2 = arr2
print(min2, minimSterse2)

arr3 = []
minimSterse3 = []
min3 = len(v)
for elem in keepInsertie:
    arr3 = eliminInsertie(elem)
    print(elem, ":" ,arr3)
    if len(arr3) < min3:
        min3 = len(arr3)
        minimSterse3 = arr3
print(min3, minimSterse3)
    
