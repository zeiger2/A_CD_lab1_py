import time
from random import *
import sys
sys.setrecursionlimit(10000)

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
def quicksort(A):
    if len(A)>1:
        random_index=A[randint(0, len(A)-1)]
        less=[x for x in A if x<random_index]
        equel=[x for x in A if x==random_index]
        great=[x for x in A if x>random_index]
        A=quicksort(less)+equel+quicksort(great)
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
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def heap_sort(arr): 
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

#ShellSort
def shell_sort_shell(arr): # последовательть Шелла
    gap = len(arr)//2
    while gap > 0:
        for value in range(gap, len(arr)):
            temp = arr[value]
            index = value
            while index >= gap and arr[index-gap] > temp:
                arr[index] = arr[index-gap]
                index -= gap
                arr[index] = temp
        gap //= 2
    return arr



def generate_hibbard_sequence(n):
    gaps = []
    k = 1 
    while True:
        gap = (2 ** k) - 1
        if gap >= n:
            break
        gaps.append(gap)
        k += 1 
        gaps.reverse() 
    return gaps

def shell_sort_hibbard(arr):
    n = len(arr)
    gaps = generate_hibbard_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp



def generate_pratt_sequence(n):
    gaps = []
    i, j = 0, 0
    while True:
        gap = (2 ** i) * (3 ** j)
        if gap > n:
            break
        gaps.append(gap)
        if i < j:  
            j += 1
        else:      
            i += 1 
            gaps.reverse()  
    return gaps

def shell_sort_pratt(arr):
    n = len(arr)
    gaps = generate_pratt_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp


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

time_x=[]
for j in range(10000, 110000, 10000):
    print(j)
    A=[]
    #A=SortedArr(j)
    #A=NearSortedArr(j)
    #A=ReverseSortedArr(j)
    A=RandomArr(j)
    start=time.time()

    #mergesort(A,0,j-1)
    #quicksort(A)
    #shell_sort_hibbard(A)
    #shell_sort_pratt(A)
    heap_sort(A)

    end=time.time()
    time_x.append(end-start)
#A=[]
#A=SortedArr(2000)
#print(A)
#start=time.time()
#insertion_sort(A)
#selection_sort(A)
#bubbleSort(A)
#quickSort(A,0,len(A)-1)
#end=time.time()
#print(A)

#print(end-start)
print(time_x)

