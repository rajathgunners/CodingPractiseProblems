#!/bin/python3
#INSERTION SORT
import sys

def insertionSort2(n, arr):
    i = 1
    while i < n:
        m = arr[i]
        j = i-1
        while j>-1 and m < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = m
        for x in arr:
            print(x, end=" ")
        print()
        i = i+1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
