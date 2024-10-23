import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([0.46874356269836426, 1.12496018409729, 1.5936942100524902, 2.0936763286590576, 2.7565836906433105, 3.4686293601989746, 4.581352233886719, 5.972296714782715, 7.131577491760254, 8.015030145645142])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Shell Sort, sequence Pratt)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    nearly_sorted_times = np.array([1.0312139987945557, 2.5624115467071533, 5.187941312789917, 5.842481851577759, 8.249714612960815, 11.624596118927002, 14.517431259155273, 18.24936604499817, 20.049274682998657, 26.280338525772095])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Shell Sort, sequence Pratt)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    reverse_sorted_times = np.array([0.5781152248382568, 1.374950885772705, 2.0624279975891113, 2.962118148803711, 3.4373815059661865, 4.374277353286743, 5.296692609786987, 6.234158277511597, 6.859137058258057, 7.758349180221558])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Shell Sort, sequence Pratt)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    random_sorted_times = np.array([2.5473544597625732, 5.402482748031616, 10.662963628768921, 16.251235485076904, 17.437660455703735, 26.06439709663391, 28.461458206176758, 42.92310857772827, 56.041175365448, 60.499234676361084])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Shell Sort, sequence Pratt)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([0.46874356269836426, 1.12496018409729, 1.5936942100524902, 2.0936763286590576, 2.7565836906433105, 3.4686293601989746, 4.581352233886719, 5.972296714782715, 7.131577491760254, 8.015030145645142])
    nearly_sorted_times = np.array([1.0312139987945557, 2.5624115467071533, 5.187941312789917, 5.842481851577759, 8.249714612960815, 11.624596118927002, 14.517431259155273, 18.24936604499817, 20.049274682998657, 26.280338525772095])
    reverse_sorted_times = np.array([0.5781152248382568, 1.374950885772705, 2.0624279975891113, 2.962118148803711, 3.4373815059661865, 4.374277353286743, 5.296692609786987, 6.234158277511597, 6.859137058258057, 7.758349180221558])
    random_sorted_times = np.array([2.5473544597625732, 5.402482748031616, 10.662963628768921, 16.251235485076904, 17.437660455703735, 26.06439709663391, 28.461458206176758, 42.92310857772827, 56.041175365448, 60.499234676361084])

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

    plt.title('All cases of Shell Sort, sequence Pratt')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([0.46874356269836426, 1.12496018409729, 1.5936942100524902, 2.0936763286590576, 2.7565836906433105, 3.4686293601989746, 4.581352233886719, 5.972296714782715, 7.131577491760254, 8.015030145645142])
    nearly_sorted_times = np.array([1.0312139987945557, 2.5624115467071533, 5.187941312789917, 5.842481851577759, 8.249714612960815, 11.624596118927002, 14.517431259155273, 18.24936604499817, 20.049274682998657, 26.280338525772095])
    reverse_sorted_times = np.array([0.5781152248382568, 1.374950885772705, 2.0624279975891113, 2.962118148803711, 3.4373815059661865, 4.374277353286743, 5.296692609786987, 6.234158277511597, 6.859137058258057, 7.758349180221558])
    random_sorted_times = np.array([2.5473544597625732, 5.402482748031616, 10.662963628768921, 16.251235485076904, 17.437660455703735, 26.06439709663391, 28.461458206176758, 42.92310857772827, 56.041175365448, 60.499234676361084])

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

    plt.title('All cases of Shell Sort, sequence Pratt')
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
