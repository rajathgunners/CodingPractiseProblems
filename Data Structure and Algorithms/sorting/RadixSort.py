#radix utility function
def RadixSortUtil(arr, dp, n):
    count = [0 for _ in range(10)]
    op = [0 for i in range(n)]
    
    for i in arr:
        count[(i//pow(10, dp-1))%10] += 1
    
    for c in range(1, 10):
        count[c] += count[c-1]
    
    for index in range(n-1, -1, -1):
        op[count[(arr[index]//pow(10, dp-1))%10]-1] = arr[index]
        count[(arr[index]//pow(10, dp-1))%10] -= 1
    
    return op

#main function
def RadixSort(arr):
    maxval = max(arr)
    
    digitplace = 0
    while maxval > 0:
        digitplace += 1
        arr = RadixSortUtil(arr, digitplace, len(arr))
        maxval = maxval//10
    
    return arr


if __name__ == "__main__":
    n = int(input("Enter size of array? "))
    
    ip = map(int, input("Enter the numbers in array? ").strip().split())
    
    ip = RadixSort(ip)
    print(ip)        