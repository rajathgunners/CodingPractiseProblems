def merge(arr1, arr2):
    mergedarr = list()
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            mergedarr.append(arr1[i])
            i+=1
        else:
            mergedarr.append(arr2[j])
            j+=1
    if i is len(arr1):
        mergedarr = mergedarr + arr2[j:]
    elif j is len(arr2):
        mergedarr = mergedarr + arr1[i:]
    
    return mergedarr
        
        
    
    



def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        lefthalf = mergeSort(arr, left, mid)
        righthalf = mergeSort(arr, mid+1, right)
        return merge(lefthalf, righthalf)
    else:
        return [arr[left]]
    





arr = [38, 27, 43, 3, 9, 82, 10]
arr = mergeSort(arr, 0, len(arr)-1)
print(arr)