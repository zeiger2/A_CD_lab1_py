import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01563, 0.01563, 0.01563, 0.01562])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Bubble Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    nearly_sorted_times = np.array([0.48436, 1.93743, 4.37485, 7.93723, 12.65924, 19.57236, 27.25910, 32.64367, 41.50620, 50.75654, 60.83632, 72.92171, 85.84709, 100.17216, 113.42737])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Bubble Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    reverse_sorted_times = np.array([0.93747, 3.76550, 8.51533, 15.01893, 23.80060, 33.72810, 46.85866, 59.94638, 76.19236, 94.18353, 115.45592, 135.91511, 160.18260, 189.56244, 213.33376])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Bubble Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    random_sorted_times = np.array([0.70390, 2.86397, 6.44203, 11.37656, 17.86264, 25.32462, 34.70720, 44.84403, 61.02469, 74.48927, 91.25834, 111.41879, 122.83316, 139.93531, 161.56760])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Bubble Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01563, 0.01563, 0.01563, 0.01562])
    nearly_sorted_times = np.array([0.48436, 1.93743, 4.37485, 7.93723, 12.65924, 19.57236, 27.25910, 32.64367, 41.50620, 50.75654, 60.83632, 72.92171, 85.84709, 100.17216, 113.42737])
    reverse_sorted_times = np.array([0.93747, 3.76550, 8.51533, 15.01893, 23.80060, 33.72810, 46.85866, 59.94638, 76.19236, 94.18353, 115.45592, 135.91511, 160.18260, 189.56244, 213.33376])
    random_sorted_times = np.array([0.70390, 2.86397, 6.44203, 11.37656, 17.86264, 25.32462, 34.70720, 44.84403, 61.02469, 74.48927, 91.25834, 111.41879, 122.83316, 139.93531, 161.56760])

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

    plt.title('All cases of Bubble Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01563, 0.01563, 0.01563, 0.01562])
    nearly_sorted_times = np.array([0.48436, 1.93743, 4.37485, 7.93723, 12.65924, 19.57236, 27.25910, 32.64367, 41.50620, 50.75654, 60.83632, 72.92171, 85.84709, 100.17216, 113.42737])
    reverse_sorted_times = np.array([0.93747, 3.76550, 8.51533, 15.01893, 23.80060, 33.72810, 46.85866, 59.94638, 76.19236, 94.18353, 115.45592, 135.91511, 160.18260, 189.56244, 213.33376])
    random_sorted_times = np.array([0.70390, 2.86397, 6.44203, 11.37656, 17.86264, 25.32462, 34.70720, 44.84403, 61.02469, 74.48927, 91.25834, 111.41879, 122.83316, 139.93531, 161.56760])

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

    plt.title('All cases of Bubble Sort')
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
