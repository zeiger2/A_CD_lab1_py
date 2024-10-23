import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    sorted_times = np.array([2.8124029636383057, 5.7395031452178955, 9.069193840026855, 12.067383527755737, 15.108853101730347, 19.17363142967224, 22.38443374633789, 25.50543713569641, 28.860786199569702, 31.978812217712402, 37.0831515789032, 40.475528717041016, 42.75680327415466, 59.187382221221924, 67.65085244178772])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Shell Sort, sequence Shell)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    nearly_sorted_times = np.array([6.034437656402588, 13.770036935806274, 20.58276653289795, 31.931432247161865, 40.95993375778198, 51.23851799964905, 63.2111382484436, 72.1833848953247, 74.05302953720093, 83.44420671463013, 97.1748719215393, 109.41012144088745, 118.50046396255493, 129.76768493652344, 135.64804577827454])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Shell Sort, sequence Shell)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    reverse_sorted_times = np.array([4.218603610992432, 8.978453159332275, 13.618446588516235, 19.096022367477417, 23.455239295959473, 29.191312313079834, 34.101818561553955, 40.66016340255737, 43.863714933395386, 49.36348819732666, 57.350048542022705, 62.56535220146179, 66.13435888290405, 73.0229024887085, 79.0599353313446])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Shell Sort, sequence Shell)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    random_sorted_times = np.array([8.452831745147705, 20.57112407684326, 30.891977071762085, 48.01183795928955, 56.022456407547, 65.84003710746765, 77.47675561904907, 105.87169575691223, 107.41858196258545, 136.95855283737183, 138.9546022415161, 150.75103735923767, 169.72310733795166, 177.16766238212585, 195.7170979976654])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Shell Sort, sequence Shell)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    sorted_times = np.array([2.8124029636383057, 5.7395031452178955, 9.069193840026855, 12.067383527755737, 15.108853101730347, 19.17363142967224, 22.38443374633789, 25.50543713569641, 28.860786199569702, 31.978812217712402, 37.0831515789032, 40.475528717041016, 42.75680327415466, 59.187382221221924, 67.65085244178772])
    nearly_sorted_times = np.array([6.034437656402588, 13.770036935806274, 20.58276653289795, 31.931432247161865, 40.95993375778198, 51.23851799964905, 63.2111382484436, 72.1833848953247, 74.05302953720093, 83.44420671463013, 97.1748719215393, 109.41012144088745, 118.50046396255493, 129.76768493652344, 135.64804577827454])
    reverse_sorted_times = np.array([4.218603610992432, 8.978453159332275, 13.618446588516235, 19.096022367477417, 23.455239295959473, 29.191312313079834, 34.101818561553955, 40.66016340255737, 43.863714933395386, 49.36348819732666, 57.350048542022705, 62.56535220146179, 66.13435888290405, 73.0229024887085, 79.0599353313446])
    random_sorted_times = np.array([8.452831745147705, 20.57112407684326, 30.891977071762085, 48.01183795928955, 56.022456407547, 65.84003710746765, 77.47675561904907, 105.87169575691223, 107.41858196258545, 136.95855283737183, 138.9546022415161, 150.75103735923767, 169.72310733795166, 177.16766238212585, 195.7170979976654])

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

    plt.title('All cases of Shell Sort, sequence Shell')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000])
    sorted_times = np.array([2.8124029636383057, 5.7395031452178955, 9.069193840026855, 12.067383527755737, 15.108853101730347, 19.17363142967224, 22.38443374633789, 25.50543713569641, 28.860786199569702, 31.978812217712402, 37.0831515789032, 40.475528717041016, 42.75680327415466, 59.187382221221924, 67.65085244178772])
    nearly_sorted_times = np.array([6.034437656402588, 13.770036935806274, 20.58276653289795, 31.931432247161865, 40.95993375778198, 51.23851799964905, 63.2111382484436, 72.1833848953247, 74.05302953720093, 83.44420671463013, 97.1748719215393, 109.41012144088745, 118.50046396255493, 129.76768493652344, 135.64804577827454])
    reverse_sorted_times = np.array([4.218603610992432, 8.978453159332275, 13.618446588516235, 19.096022367477417, 23.455239295959473, 29.191312313079834, 34.101818561553955, 40.66016340255737, 43.863714933395386, 49.36348819732666, 57.350048542022705, 62.56535220146179, 66.13435888290405, 73.0229024887085, 79.0599353313446])
    random_sorted_times = np.array([8.452831745147705, 20.57112407684326, 30.891977071762085, 48.01183795928955, 56.022456407547, 65.84003710746765, 77.47675561904907, 105.87169575691223, 107.41858196258545, 136.95855283737183, 138.9546022415161, 150.75103735923767, 169.72310733795166, 177.16766238212585, 195.7170979976654])

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

    plt.title('All cases of Shell Sort, sequence Shell')
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

