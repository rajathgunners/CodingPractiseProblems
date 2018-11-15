
#Bucket Sort

#function to sort bucket according to digit place
def BucketSortUtil(bucket, digitplace):
    temp = [[] for _ in range(10)]
    for i in bucket:
        for j in i:
            d = (j% pow(10, digitplace+1))//pow(10, digitplace)
            temp[d].append(j)
    return temp
        
        
        
    
#main function
def BucketSort(arr):
    bucket = [[] for _ in range(10)]
    
    maxv = 0
    
    #finding th maximum value to find the places and
    #separating into buckets using units place digit
    for i1 in arr:
        d = i1%10
        bucket[d].append(i1)
        if i1 > maxv:
            maxv = i1
    
    #calculating number of digits in maxval 
    count=0
    while maxv!=0:
        count += 1
        maxv = maxv//10
    
    #sorting in bucket from tens to most significant place
    for p in range(1 , count):
        bucket = BucketSortUtil(bucket.copy(), p)
    
    sortedlist = []
    for b in bucket:
        sortedlist.extend(b)
    
    print(sortedlist)

if __name__ == "__main__":
    n = int(input("Enter size of array? "))
    
    arr = map(int, input("Enter the numbers in array? ").strip().split())
    
    BucketSort(arr)
    
    