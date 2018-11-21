
"""Given an input stream of n integers the task is to insert integers to stream and print the median of the new stream formed by each insertion of x to the stream.

Example

Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)

Input:
The first line of input contains an integer N denoting the no of elements of the stream. Then the next N lines contains integer x denoting the no to be inserted to the stream.

Output:
For each element added to the stream print the floor of the new median in a new line.

Constraints:
1<=N<=105 + 7
1<=x<=105 + 7

Example:
Input:
4
5
15
1 
3
Output:
5
10
5
4"""





from heapq import heapify, heappop, heappush, _heapify_max, _heappop_max

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)
    return 

def heap_diff(lowmax, highmin):
    return len(lowmax) - len(highmin) 

    
    
def FindMedian(arr):
    lowmax = []
    highmin = []
    
    count = 0
    median = []
    for ele in arr:
        count += 1
        
        if len(lowmax) == 0 or ele <= lowmax[0]:
            _heappush_max(lowmax, ele)
        else:
            heappush(highmin, ele)
    
        
        diff = heap_diff(lowmax, highmin)
        
        if diff == 2:
            temp = _heappop_max(lowmax)
            heappush(highmin, temp)
        elif diff == -2:
            temp = heappop(highmin)
            _heappush_max(lowmax, temp)
        
        if count%2 == 0:
            median.append((lowmax[0] + highmin[0])//2)
        else:
            if len(lowmax) > len(highmin):
                median.append(lowmax[0])
            else:
                median.append(highmin[0])
        
        print("less = {},  high = {}".format(lowmax, highmin))
    return median


N = int(input())
ip =[]
for i in range(N):
    ip.append(int(input()))

m = FindMedian(ip)

for j in m:
    print(j)
    
            
        