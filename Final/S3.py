from problem import Problem
import random
from itertools import chain, combinations
import collections


class ProblemTest1(Problem):
    def __init__(self):
        n = random.randint(8, 12)
        datagen = random.sample(range(12), n)
        #data trebuie sa fie un tuplu, adica pot sa pun elementele, nr de elem si nrPasi
        nrPasiUnu = random.randint(2, n // 2)
        nrPasiDoi = random.randint(2, n // 2)
        nrPasiTrei = random.randint(2, n // 2)
        
        data = (datagen, nrPasiUnu, nrPasiDoi, nrPasiTrei)

        statement = 'Primind sirul: ' + ', '.join(map(str, data[0])) + '. '
        statement += 'Gasiti numarul minim de elemente care pot fi sterse a.i. sa se poata considera ca s-au efectuat:\n'
        statement += 'a) ' + str (nrPasiUnu)
        statement += ' pasi din alg. de sort. prin selectia max\n' 
        statement += 'b) ' + str (nrPasiDoi)
        statement += ' pasi din alg. de sort. prin selectia min\n'
        statement += 'c) ' + str (nrPasiTrei)
        statement += ' pasi din alg. de sort. prin insertie directa'
    

        super().__init__(statement, data)
        #ca sa am si numere care merg sterse pot sa dau super().__init__(statement, data)
        #dupa ce fac solve
        #in solve pot sa modific statement

    def solve(self):
      v = self.data[0]
      solution = "Generam submultimi de elemente din vector pentru a cauta-o pe aceea care are numarul minim de elemente pe care "
      solution += "sa le putem sterge pentru a satisface fiecare dintre cerinte.\n"
      solution += "Generarea submultimilor se face prin selectia combinarilor de n elemente luate cate nrPasi corespunzator subpunctului.\n"
      solution += "La fiecare pas din cerinta iteram prin combinarile genrate si le alegem pe cele care au o lungime corespunzatoare\n"
      solution += "numarului de pasi si sunt sortate\n"

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

      nrPasiUnu = self.data[1]
      nrPasiDoi = self.data[2]
      nrPasiTrei = self.data[3]
      keepMinim = []
      keepMaxim = []
      keepInsertie = []

      for subset in powerset(v):
          if (len(subset) == nrPasiUnu and sorted(subset)):
              subset = list(subset)
              keepMinim.append(subset)
          if (len(subset) == nrPasiDoi and sorted(subset)):
              subset = list(subset)
              keepMaxim.append(subset)
          if (len(subset) == nrPasiTrei + 1 and sorted(subset)):
              subset = list(subset)
              keepInsertie.append(subset)

      arrMinim = []
      minimSterse = []
      min = len(v)
      for elem in keepMinim:
          arrMinim = eliminSelectMinim(elem)
          #print(elem, ":" ,arr)
          if len(arrMinim) < min:
              min = len(arrMinim)
              minimSterse = arrMinim
      print(min, minimSterse)

      arrMaxim = []
      minimSterse2 = []
      min2 = len(v)
      for elem in keepMaxim:
          arrMaxim = eliminSelectMaxim(elem)
          #print(elem, ":" ,arr2)
          if len(arrMaxim) < min2:
              min2 = len(arrMaxim)
              minimSterse2 = arrMaxim
      print(min2, minimSterse2)

      arrInsertie = []
      minimSterse3 = []
      min3 = len(v)
      for elem in keepInsertie:
          arrInsertie = eliminInsertie(elem)
          #print(elem, ":" ,arrInsertie)
          if len(arrInsertie) < min3:
              min3 = len(arrInsertie)
              minimSterse3 = arrInsertie
      print(min3, minimSterse3)
      return solution
          
