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


#RandomizeArray
def RandomArr(kol,_seed):
    seed(_seed)
    A=[randint(0,50) for _ in range(kol)]
    return A

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

A=[]
A=RandomArr(15,5)


#print(A)
#print(insertion_sort(A))
