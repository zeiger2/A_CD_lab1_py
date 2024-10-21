import time
from random import *

#InsertionSort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#SelectionSort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#BybbleSort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

#QuickSort
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)



#MergeSort
def merge(arr, left, mid, right):
    n1=mid-left+1
    n2=right-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[left+1]
    for j in range(n2):
        R[j]=arr[mid+1+j]
    i,j=0,0
    k=left
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
def mergesort(arr, left, right):
    if left<right:
        mid=(left+right)//2

        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)

        merge(arr,left,mid,right)

#HeapSort
def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2  
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr) 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

#ShellSort
def shellSort(arr, n):
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
            while i>=0:
                if arr[i+gap]>arr[i]:

                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap
            j+=1
        gap=gap//2

#RandomizeArray
def RandomArr(kol):
    A=[randint(0,kol) for i in range(kol)]
    return A
def SortedArr(kol):
    A=[i for i in range(kol)]
    return A
def ReverseSortedArr(kol):
    A=[i for i in range(kol, 0, -1)]
    return A
def NearSortedArr(kol):
    arr0=[i for i in range(kol-kol//10)]
    arr1=[randint(0, kol) for i in range (kol//10)]
    A=arr0+arr1
    return A

A=[]
#A=SortedArr(1000)
#A=NearSortedArr(1000)
A=ReverseSortedArr(15000)
#A=RandomArr(1000)

start=time.time()
#print(A)
insertion_sort(A)
#print(A)
end=time.time()
print(end-start)

