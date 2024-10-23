import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([5.077962160110474, 9.013759851455688, 12.937053203582764, 17.76500678062439, 19.717092990875244, 26.06159496307373, 30.644050359725952, 33.93631958961487, 41.07670068740845, 45.532599687576294])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Heap Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    nearly_sorted_times = np.array([3.812366008758545, 8.694662809371948, 13.42140817642212, 16.921286582946777, 22.483594179153442, 26.202216863632202, 29.689919233322144, 38.529911518096924, 41.09232974052429, 48.22750759124756])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Heap Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    reverse_sorted_times = np.array([4.140477657318115, 7.578798055648804, 9.468424081802368, 16.327558994293213, 19.898243188858032, 20.198894023895264, 23.319712162017822, 25.014699935913086, 24.4360408782959, 26.92414879798889])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Heap Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    random_sorted_times = np.array([3.265512466430664, 6.812263488769531, 10.269314765930176, 15.150147914886475, 21.621594667434692, 23.813374042510986, 23.86575436592102, 26.63124942779541, 25.685194492340088, 29.15438222885132])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Heap Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([5.077962160110474, 9.013759851455688, 12.937053203582764, 17.76500678062439, 19.717092990875244, 26.06159496307373, 30.644050359725952, 33.93631958961487, 41.07670068740845, 45.532599687576294])
    nearly_sorted_times = np.array([3.812366008758545, 8.694662809371948, 13.42140817642212, 16.921286582946777, 22.483594179153442, 26.202216863632202, 29.689919233322144, 38.529911518096924, 41.09232974052429, 48.22750759124756])
    reverse_sorted_times = np.array([4.140477657318115, 7.578798055648804, 9.468424081802368, 16.327558994293213, 19.898243188858032, 20.198894023895264, 23.319712162017822, 25.014699935913086, 24.4360408782959, 26.92414879798889])
    random_sorted_times = np.array([3.265512466430664, 6.812263488769531, 10.269314765930176, 15.150147914886475, 21.621594667434692, 23.813374042510986, 23.86575436592102, 26.63124942779541, 25.685194492340088, 29.15438222885132])

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

    plt.title('All cases of Heap Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
    sorted_times = np.array([5.077962160110474, 9.013759851455688, 12.937053203582764, 17.76500678062439, 19.717092990875244, 26.06159496307373, 30.644050359725952, 33.93631958961487, 41.07670068740845, 45.532599687576294])
    nearly_sorted_times = np.array([3.812366008758545, 8.694662809371948, 13.42140817642212, 16.921286582946777, 22.483594179153442, 26.202216863632202, 29.689919233322144, 38.529911518096924, 41.09232974052429, 48.22750759124756])
    reverse_sorted_times = np.array([4.140477657318115, 7.578798055648804, 9.468424081802368, 16.327558994293213, 19.898243188858032, 20.198894023895264, 23.319712162017822, 25.014699935913086, 24.4360408782959, 26.92414879798889])
    random_sorted_times = np.array([3.265512466430664, 6.812263488769531, 10.269314765930176, 15.150147914886475, 21.621594667434692, 23.813374042510986, 23.86575436592102, 26.63124942779541, 25.685194492340088, 29.15438222885132])

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

    plt.title('All cases of Heap Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
#SortedArray()
#NearSortedArray()
#ReverseSorted()
RandomSorted()
#AllIn()
#AllInDot()

