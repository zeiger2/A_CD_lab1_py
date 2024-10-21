import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.00299, 0.00700, 0.01798, 0.01499, 0.01998, 0.02598, 0.03797, 0.04197, 0.02997, 0.03398, 0.04597, 0.04097, 0.04497, 0.04796, 0.06495])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Insertion Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    nearly_sorted_times = np.array([0.09375, 0.53124, 0.82810, 1.82123, 2.54740, 3.33609, 5.18190, 6.61190, 8.60155, 10.09110, 12.47979, 14.60895, 17.45444, 20.19146, 22.62814])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Insertion Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    reverse_sorted_times = np.array([1.08800, 4.48251, 10.38527, 19.74156, 29.79436, 42.75136, 55.85439, 75.01389, 96.23591, 115.28230, 139.87880, 167.92040, 197.87882, 234.03239, 259.95120])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Insertion Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    random_sorted_times = np.array([0.56249, 2.52609, 5.23048, 8.98553, 14.96114, 20.67983, 27.91302, 36.38804, 45.90503, 57.39476, 68.87406, 81.88110, 96.40961, 109.61145, 128.79643])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Insertion Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.00299, 0.00700, 0.01798, 0.01499, 0.01998, 0.02598, 0.03797, 0.04197, 0.02997, 0.03398, 0.04597, 0.04097, 0.04497, 0.04796, 0.06495])
    nearly_sorted_times = np.array([0.09375, 0.53124, 0.82810, 1.82123, 2.54740, 3.33609, 5.18190, 6.61190, 8.60155, 10.09110, 12.47979, 14.60895, 17.45444, 20.19146, 22.62814])
    reverse_sorted_times = np.array([1.08800, 4.48251, 10.38527, 19.74156, 29.79436, 42.75136, 55.85439, 75.01389, 96.23591, 115.28230, 139.87880, 167.92040, 197.87882, 234.03239, 259.95120])
    random_sorted_times = np.array([0.56249, 2.52609, 5.23048, 8.98553, 14.96114, 20.67983, 27.91302, 36.38804, 45.90503, 57.39476, 68.87406, 81.88110, 96.40961, 109.61145, 128.79643])

    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)

    sorted_smooth = np.poly1d(np.polyfit(sizes, sorted_times, 3))(sizes_smooth)
    nearly_sorted_smooth = np.poly1d(np.polyfit(sizes, nearly_sorted_times, 3))(sizes_smooth)
    reverse_sorted_smooth = np.poly1d(np.polyfit(sizes, reverse_sorted_times, 3))(sizes_smooth)
    random_smooth = np.poly1d(np.polyfit(sizes, random_sorted_times, 3))(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes_smooth, sorted_smooth, color='blue', label="Sorted Array", linewidth=2)
    plt.plot(sizes_smooth, nearly_sorted_smooth, color='purple', label="NearlySorted Array", linewidth=2)
    plt.plot(sizes_smooth, reverse_sorted_smooth, color='red', label="ReverseSorted Array", linewidth=2)
    plt.plot(sizes_smooth, random_smooth, color='green', label="RandomSorted Array", linewidth=2)

    plt.title('All cases of Insertion Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.00299, 0.00700, 0.01798, 0.01499, 0.01998, 0.02598, 0.03797, 0.04197, 0.02997, 0.03398, 0.04597, 0.04097, 0.04497, 0.04796, 0.06495])
    nearly_sorted_times = np.array([0.09375, 0.53124, 0.82810, 1.82123, 2.54740, 3.33609, 5.18190, 6.61190, 8.60155, 10.09110, 12.47979, 14.60895, 17.45444, 20.19146, 22.62814])
    reverse_sorted_times = np.array([1.08800, 4.48251, 10.38527, 19.74156, 29.79436, 42.75136, 55.85439, 75.01389, 96.23591, 115.28230, 139.87880, 167.92040, 197.87882, 234.03239, 259.95120])
    random_sorted_times = np.array([0.56249, 2.52609, 5.23048, 8.98553, 14.96114, 20.67983, 27.91302, 36.38804, 45.90503, 57.39476, 68.87406, 81.88110, 96.40961, 109.61145, 128.79643])

    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)

    sorted_smooth = np.poly1d(np.polyfit(sizes, sorted_times, 3))(sizes_smooth)
    nearly_sorted_smooth = np.poly1d(np.polyfit(sizes, nearly_sorted_times, 3))(sizes_smooth)
    reverse_sorted_smooth = np.poly1d(np.polyfit(sizes, reverse_sorted_times, 3))(sizes_smooth)
    random_smooth = np.poly1d(np.polyfit(sizes, random_sorted_times, 3))(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes_smooth, sorted_smooth, color='blue', label="Sorted Array", linewidth=2)
    plt.plot(sizes_smooth, nearly_sorted_smooth, color='purple', label="NearlySorted Array", linewidth=2)
    plt.plot(sizes_smooth, reverse_sorted_smooth, color='red', label="ReverseSorted Array", linewidth=2)
    plt.plot(sizes_smooth, random_smooth, color='green', label="RandomSorted Array", linewidth=2)

    plt.scatter(sizes, sorted_times, color='red', label='Result of Sorted Array', marker='o')
    plt.scatter(sizes, nearly_sorted_times, color='brown', label='Result of NearlySorted Array', marker='+')
    plt.scatter(sizes, reverse_sorted_times, color='black', label='Result of ReverseSorted Array', marker='x')
    plt.scatter(sizes, random_sorted_times, color='blue', label='Result of RandomSorted Array', marker='*')

    plt.title('All cases of Insertion Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
#SortedArray()
#NearSortedArray()
#ReverseSorted()
#RandomSorted()
#AllIn()
#AllInDot()