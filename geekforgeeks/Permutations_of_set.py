# python program to print all permutations of a given list or string
 #(repetitions allowed)

def Perm(L, X):
     global n
     if not X:
         print(L, end = "\t")
         n = n + 1
         print(n)
     else:
         
         for z in X:
             temp = list(X)
             temp.remove(z)
             Perm(L + [z],temp)
             

lists = ['A', 'B', 'B']
 nl = []
 n = 0 #counter
 Perm(nl, lists)

#nl.remove('A')
 #print("nl = {}".format(nl))
 #print("lists = {}".format(lists))
