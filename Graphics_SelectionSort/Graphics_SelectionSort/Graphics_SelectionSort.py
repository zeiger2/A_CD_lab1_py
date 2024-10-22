import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.45311, 1.79681, 4.09361, 7.18725, 11.21836, 16.16866, 22.41999, 28.64765, 36.43982, 45.20988, 54.06104, 64.59492, 75.39129, 88.33436, 100.83247])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Selection Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    nearly_sorted_times = np.array([0.42186, 1.74994, 3.98424, 7.15600, 11.24961, 16.15661, 22.45026, 28.45144, 36.17665, 45.36961, 54.60901, 64.45236, 76.16003, 88.83554, 101.41551])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Selection Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    reverse_sorted_times = np.array([0.53123, 2.17180, 4.84358, 8.64033, 13.67741, 19.57585, 26.70960, 34.24740, 44.77937, 54.41873, 65.07189, 77.71125, 92.09983, 106.24143, 121.70653])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Selection Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    random_sorted_times = np.array([0.43749, 1.81243, 4.04673, 7.12474, 11.19389, 16.23470, 22.03713, 28.61818, 36.41900, 44.32343, 54.81992, 64.02691, 76.60290, 87.80642, 101.08391])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Selection Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.45311, 1.79681, 4.09361, 7.18725, 11.21836, 16.16866, 22.41999, 28.64765, 36.43982, 45.20988, 54.06104, 64.59492, 75.39129, 88.33436, 100.83247])
    nearly_sorted_times = np.array([0.42186, 1.74994, 3.98424, 7.15600, 11.24961, 16.15661, 22.45026, 28.45144, 36.17665, 45.36961, 54.60901, 64.45236, 76.16003, 88.83554, 101.41551])
    reverse_sorted_times = np.array([0.53123, 2.17180, 4.84358, 8.64033, 13.67741, 19.57585, 26.70960, 34.24740, 44.77937, 54.41873, 65.07189, 77.71125, 92.09983, 106.24143, 121.70653])
    random_sorted_times = np.array([0.43749, 1.81243, 4.04673, 7.12474, 11.19389, 16.23470, 22.03713, 28.61818, 36.41900, 44.32343, 54.81992, 64.02691, 76.60290, 87.80642, 101.08391])

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

    plt.title('All cases of Selection Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.45311, 1.79681, 4.09361, 7.18725, 11.21836, 16.16866, 22.41999, 28.64765, 36.43982, 45.20988, 54.06104, 64.59492, 75.39129, 88.33436, 100.83247])
    nearly_sorted_times = np.array([0.42186, 1.74994, 3.98424, 7.15600, 11.24961, 16.15661, 22.45026, 28.45144, 36.17665, 45.36961, 54.60901, 64.45236, 76.16003, 88.83554, 101.41551])
    reverse_sorted_times = np.array([0.53123, 2.17180, 4.84358, 8.64033, 13.67741, 19.57585, 26.70960, 34.24740, 44.77937, 54.41873, 65.07189, 77.71125, 92.09983, 106.24143, 121.70653])
    random_sorted_times = np.array([0.43749, 1.81243, 4.04673, 7.12474, 11.19389, 16.23470, 22.03713, 28.61818, 36.41900, 44.32343, 54.81992, 64.02691, 76.60290, 87.80642, 101.08391])
    
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

    plt.title('All cases of Selection Sort')
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
AllInDot()
