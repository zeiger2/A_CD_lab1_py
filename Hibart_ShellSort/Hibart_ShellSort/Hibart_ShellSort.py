import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    sorted_times = np.array([3.328012228012085, 7.846923351287842, 11.521644115447998, 14.671360492706299, 18.546230792999268, 22.5148446559906, 26.73344659805298, 30.908615589141846, 36.49873185157776, 39.48300552368164])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Shell Sort, sequence Hibbart)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    nearly_sorted_times = np.array([11.843339920043945, 15.708605527877808, 35.99875545501709, 72.20405316352844, 64.37275648117065, 51.03290009498596, 67.37266397476196, 76.271329164505, 86.828537940979, 99.84028649330139])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Shell Sort, sequence Hibbart)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    reverse_sorted_times = np.array([4.32797384262085, 9.369613409042358, 14.999480485916138, 19.514946222305298, 25.62411069869995, 31.486710786819458, 34.03006911277771, 40.029857873916626, 45.18936347961426, 51.57633924484253])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Shell Sort, sequence Hibbart)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    random_sorted_times = np.array([20.127736806869507, 22.377121925354004, 42.13729000091553, 74.09628582000732, 90.20773601531982, 122.14152216911316, 150.86280751228333, 145.33206939697266, 159.75260901451111, 171.3000967502594])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Shell Sort, sequence Hibbart)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    sorted_times = np.array([3.328012228012085, 7.846923351287842, 11.521644115447998, 14.671360492706299, 18.546230792999268, 22.5148446559906, 26.73344659805298, 30.908615589141846, 36.49873185157776, 39.48300552368164])
    nearly_sorted_times = np.array([11.843339920043945, 15.708605527877808, 35.99875545501709, 72.20405316352844, 64.37275648117065, 51.03290009498596, 67.37266397476196, 76.271329164505, 86.828537940979, 99.84028649330139])
    reverse_sorted_times = np.array([4.32797384262085, 9.369613409042358, 14.999480485916138, 19.514946222305298, 25.62411069869995, 31.486710786819458, 34.03006911277771, 40.029857873916626, 45.18936347961426, 51.57633924484253])
    random_sorted_times = np.array([20.127736806869507, 22.377121925354004, 42.13729000091553, 74.09628582000732, 90.20773601531982, 122.14152216911316, 150.86280751228333, 145.33206939697266, 159.75260901451111, 171.3000967502594])

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

    plt.title('All cases of Shell Sort, sequence Hibbart')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000])
    sorted_times = np.array([3.328012228012085, 7.846923351287842, 11.521644115447998, 14.671360492706299, 18.546230792999268, 22.5148446559906, 26.73344659805298, 30.908615589141846, 36.49873185157776, 39.48300552368164])
    nearly_sorted_times = np.array([11.843339920043945, 15.708605527877808, 35.99875545501709, 72.20405316352844, 64.37275648117065, 51.03290009498596, 67.37266397476196, 76.271329164505, 86.828537940979, 99.84028649330139])
    reverse_sorted_times = np.array([4.32797384262085, 9.369613409042358, 14.999480485916138, 19.514946222305298, 25.62411069869995, 31.486710786819458, 34.03006911277771, 40.029857873916626, 45.18936347961426, 51.57633924484253])
    random_sorted_times = np.array([20.127736806869507, 22.377121925354004, 42.13729000091553, 74.09628582000732, 90.20773601531982, 122.14152216911316, 150.86280751228333, 145.33206939697266, 159.75260901451111, 171.3000967502594])

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

    plt.title('All cases of Shell Sort, sequence Hibbart')
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


