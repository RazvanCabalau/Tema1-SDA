from problem import Problem
import random

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
     #   solution = "b)"
      #  nrSortate = 0
       # vect = data[0]
        #n = len(vect)
        #nrPasiDoi = self.nrPasiDoi
        #inceputSecventa = 0
        #sfarsitSecventa = 0
        #for i in range(n-1):
        #    print("i=", i)
         #   if vect[i] < vect[i+1]:
          #      nrSortate += 1
          #      sfarsitSecventa += 1
           # else:
            #    inceputSecventa = i+1
             #   sfarsitSecventa = i+1
              #  nrSortate = 1
            #if nrSortate == nrPasiDoi:
             #   break
        #print("inceputSecventa: ", vect[inceputSecventa], " sfarsitSecventa ", vect[sfarsitSecventa])
        #minSecventa = vect[inceputSecventa]
        #maxSEcventa = vect[sfarsitSecventa]
        #elementeSterse = []
        #for i in range(n):
         #   if vect[i] > vect[inceputSecventa] and i < inceputSecventa:
          #      print("1 if", vect[i])
           #     elementeSterse.append(vect[i])
           # if vect[i] < vect[inceputSecventa] and i > sfarsitSecventa:
            #    print("2 if", vect[i])
             #   elementeSterse.append(vect[i])
            #if vect[i] > vect[sfarsitSecventa] and i > sfarsitSecventa:
             #   print("3 if", vect[i])
              #  elementeSterse.append(vect[i])
            #if (vect[i] < vect[sfarsitSecventa] and vect[i] < vect[inceputSecventa]) and i > sfarsitSecventa:
             #   print("4 if", vect[i])
              #  elementeSterse.append(vect[i])
            #if len(elementeSterse) == nrPasiDoi:
             #   break
        #print(elementeSterse)
        return 0
        #return solution
    
