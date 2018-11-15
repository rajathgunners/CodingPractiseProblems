def countingSort(arr):
    maxrange = max(arr)+1
    aux = [0 for x in range(maxrange)]
    
    for i in arr:
        aux[i] = aux[i]+1
    print(aux)
    
    pos=1                                                                           
    while pos < (len(aux)-1):
        aux[pos+1]+=aux[pos]
        pos+=1
    print(aux)
    sortedarr = [0 for x in range(len(arr))]
    
    for i in arr:
        sortedarr[aux[i]-1] = i
        aux[i]-=1
    print("sorted Array")
    print(sortedarr)
        


arr = [5, 2, 9, 5, 2, 3, 5]
countingSort(arr)