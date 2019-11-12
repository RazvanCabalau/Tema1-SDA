from problem import Problem
import random
from itertools import chain, combinations
import collections


class ProblemTest1(Problem):
    def __init__(self):
        n = random.randint(8, 12)
        datagen = random.sample(range(12), n)
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


    def solve(self):
        v = self.data[0]
        solution = "Pentru toate cazuriel generam submultimi de elemente din vector pentru a cauta-o pe aceea care \nare numarul minim de elemente pe care "
        solution += "sa le putem sterge pentru a satisface fiecare cerinta.\n"
        solution += "Generarea submultimilor se face prin selectia combinarilor de n elemente luate cate nrPasi \ncorespunzator subpunctului.\n"
        solution += "La fiecare pas din cerinta iteram prin combinarile genrate si le alegem pe cele care au o\nlungime corespunzatoare"
        solution += "numarului de pasi pe care l-a facut altgoritmul si sunt sortate\n"

        def powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

        def sorted (v):
            n = len (v)
            for i in range (n - 1):
                if v[i] > v[i + 1]:
                    return 0
            return 1

        def eliminSelectMaxim (subset):
            primul = subset[0]
            ultimul = subset [len(subset) -1]
            sterse = []
            sol = "\nPentru secventa ["
            for i in range (len(subset)):
                sol += str(subset[i])
                if i != len(subset) -1:
                    sol += ', '
            sol += "] elementele [ "
            for i in range(len(v)):
                if v[i] in subset:
                    continue
                if v[i] > ultimul:
                    sterse.append(v[i])
                    sol += str(v[i]) + " "
                    continue
                if v[i] < primul and i > v.index(primul):
                    sterse.append(v[i])
                    sol += str(v[i]) + " "
                    continue
                if v[i] < ultimul and i > v.index(ultimul):
                    sterse.append(v[i])
                    sol += str(v[i]) + " "
                    continue
                if v[i] > primul and v[i] < ultimul:
                    sterse.append(v[i])
                    sol += str(v[i]) + " "
                    continue
            sol += '] au fost sterse conform celor de mai sus.\n'
            return (sterse, sol)  

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
        combinari = powerset(v)

        for subset in combinari: 
            if (len(subset) == nrPasiUnu and sorted(subset)):
                subset = list(subset)
                keepMaxim.append(subset)
            if (len(subset) == nrPasiDoi and sorted(subset)):
                subset = list(subset)
                keepMinim.append(subset)
            if (len(subset) == nrPasiTrei + 1 and sorted(subset)):
                subset = list(subset)
                keepInsertie.append(subset)
        
        solution +="\na)Selectia maximului:"

        if (len(keepMaxim) == 0):
            solution += "\nNu a fost gasita o secventa sortata de lungime " + str(nrPasiUnu) + ".\n"
        else:
            solution += "\n\nPentru selectia maximului am gasit "+ str(len(keepMaxim)) + " subseturi de lungime " + str(nrPasiUnu) +" : "
            for subset in keepMaxim:
                solution += "["
                for i in range (len(subset)):
                    solution += str(subset[i])
                    if i != len(subset) -1:
                        solution += ', '
                solution += "] "
            solution += "\n\nLa fiecare pas consideram secventa sortata  s1, ..., sP, unde P e lungimea secventei, si eliminam numerele:\n"
            solution += "\t- care sunt mai mari decat sP\n"
            solution += "\t- care sunt mai mici decat s1 si se afla dupa s1 in vector\n"
            solution += "\t- care sunt mai mici decat sP si se afla dupa sP in vector\n"
            solution += "\t- care apartin intervalului [s1, sP], dar nu sunt in secventa\n"
            
            sol = ""
            arrMaxim = []
            minimSterse = []
            min = len(v)
            for elem in keepMaxim:
                (arrMaxim, sol) = eliminSelectMaxim(elem)
                solution += sol
                if len(arrMaxim) < min:
                    min = len(arrMaxim)
                    minimSterse = arrMaxim

            solution += "\nSecventa de lungime " + str(min) + " pe care o stergem este: "
            solution += '[ '
            for i in range (len(minimSterse)):
                solution += str(minimSterse[i])
                if i != len(minimSterse) -1:
                    solution += ' '
            solution += "] "
        
        solution +="\n\nb)Selectia minimului:"

        if (len(keepMinim) == 0):
            solution += "\nNu a fost gasita o secventa sortata de lungime " + str(nrPasiDoi) + ".\n"
        else:
            solution += "\n\nPentru selectia minimului am gasit "+ str(len(keepMinim)) + " subseturi de lungime " + str(nrPasiDoi) +" : "
            
            for subset in keepMinim:
                solution += "["
                for i in range (len(subset)):
                    solution += str(subset[i])
                    if i != len(subset) -1:
                        solution += ', '
                solution += "] "

            solution += "\n\nLa fiecare pas consideram secventa sortata  s1, ..., sP, unde P e lungimea secventei, si eliminam numerele:\n"
            solution += "\t- care sunt mai mici decat s1\n"
            solution += "\t- care sunt mai mari decat sP si se afla la stanga lui sP\n"
            solution += "\t- care apartin intervalului [s1, sP] dar nu se afla un subset\n"
                
            sol = ""
            arrMinim = []
            minimSterse2 = []
            min2 = len(v)

            for elem in keepMinim:
                arrMinim = eliminSelectMinim(elem)
                if len(arrMinim) < min2:
                    min2 = len(arrMinim)
                    minimSterse2 = arrMinim
            solution += "\nSecventa de lungime " + str(min2) + " pe care o stergem este: "
            solution += '[ '

            for i in range (len(minimSterse2)):
                solution += str(minimSterse2[i])
                if i != len(minimSterse2) -1:
                    solution += ' '
            solution += " ] "

        solution +="\n\nc)Insertie:"
        if (len(keepInsertie) == 0):
            solution += "\nNu a fost gasita o secventa sortata de lungime " + str(nrPasiTrei) + ".\n"
        else:
            solution += "\n\nPentru insertie am gasit "+ str(len(keepInsertie)) + " subseturi care respecta cerinta : "

            for subset in keepInsertie:
                solution += "["
                for i in range (len(subset)):
                    solution += str(subset[i])
                    if i != len(subset) -1:
                        solution += ', '
                solution += " ] "
            solution += "\n\nLa fiecare pas consideram secventa sortata  s1, ..., sP, unde P e lungimea secventei, si eliminam numerele:\n"
            solution += "\t- care sunt mai mici decat s1\n"
            solution += "\t- care sunt mai mari decat sP\n"
            solution += "\t- care apartin intervalului [s1, sP] dar nu se afla un subset\n"
            arrInsertie = []
            minimSterse3 = []
            min3 = len(v)

            for elem in keepInsertie:
                arrInsertie = eliminInsertie(elem)
                if len(arrInsertie) < min3:
                    min3 = len(arrInsertie)
                    minimSterse3 = arrInsertie
            solution += "\nSecventa de lungime " + str(min3) + " pe care o stergem este: "
            solution += "[ "
                
            for i in range (len(minimSterse3)):
                solution += str(minimSterse3[i])
                if i != len(minimSterse3) -1:
                    solution += ' '
            solution += " ] "

        return solution
            
