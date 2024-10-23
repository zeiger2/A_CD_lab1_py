import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.15490269660949707, 0.2808253765106201, 0.43389225006103516, 0.5221645832061768, 0.6256439685821533, 0.8261210918426514, 0.9930005073547363, 1.2746846675872803, 1.3881208896636963, 1.545541763305664, 1.6432485580444336, 1.7003142833709717, 1.911815881729126, 2.1023285388946533, 2.1773910522460938])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Merge Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    nearly_sorted_times = np.array([0.1697390079498291, 0.2751610279083252, 0.35994720458984375, 0.5371630191802979, 0.682565450668335, 0.7143869400024414, 0.9703342914581299, 0.9932212829589844, 1.1789438724517822, 1.3136160373687744, 1.3425483703613281, 1.483445167541504, 1.6322522163391113, 2.0996885299682617, 2.0456745624542236])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Merge Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    reverse_sorted_times = np.array([0.1089317798614502, 0.255108118057251, 0.3162379264831543, 0.5472440719604492, 0.6074798107147217, 0.7668356895446777, 0.9620559215545654, 1.0597748756408691, 1.1092748641967773, 1.3711426258087158, 1.459726333618164, 1.6021757125854492, 1.8361663818359375, 1.6604435443878174, 2.0050265789031982])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Merge Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    random_sorted_times = np.array([0.11710906028747559, 0.2751917839050293, 0.3446469306945801, 0.4791140556335449, 0.6018576622009277, 0.7094292640686035, 0.938995361328125, 0.9465370178222656, 1.1319715976715088, 1.1898584365844727, 1.4208884239196777, 1.5773372650146484, 1.7124269008636475, 1.7194459438323975, 1.9521324634552002])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Merge Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.15490269660949707, 0.2808253765106201, 0.43389225006103516, 0.5221645832061768, 0.6256439685821533, 0.8261210918426514, 0.9930005073547363, 1.2746846675872803, 1.3881208896636963, 1.545541763305664, 1.6432485580444336, 1.7003142833709717, 1.911815881729126, 2.1023285388946533, 2.1773910522460938])
    nearly_sorted_times = np.array([0.1697390079498291, 0.2751610279083252, 0.35994720458984375, 0.5371630191802979, 0.682565450668335, 0.7143869400024414, 0.9703342914581299, 0.9932212829589844, 1.1789438724517822, 1.3136160373687744, 1.3425483703613281, 1.483445167541504, 1.6322522163391113, 2.0996885299682617, 2.0456745624542236])
    reverse_sorted_times = np.array([0.1089317798614502, 0.255108118057251, 0.3162379264831543, 0.5472440719604492, 0.6074798107147217, 0.7668356895446777, 0.9620559215545654, 1.0597748756408691, 1.1092748641967773, 1.3711426258087158, 1.459726333618164, 1.6021757125854492, 1.8361663818359375, 1.6604435443878174, 2.0050265789031982])
    random_sorted_times = np.array([0.11710906028747559, 0.2751917839050293, 0.3446469306945801, 0.4791140556335449, 0.6018576622009277, 0.7094292640686035, 0.938995361328125, 0.9465370178222656, 1.1319715976715088, 1.1898584365844727, 1.4208884239196777, 1.5773372650146484, 1.7124269008636475, 1.7194459438323975, 1.9521324634552002])

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

    plt.title('All cases of Merge Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
    sorted_times = np.array([0.15490269660949707, 0.2808253765106201, 0.43389225006103516, 0.5221645832061768, 0.6256439685821533, 0.8261210918426514, 0.9930005073547363, 1.2746846675872803, 1.3881208896636963, 1.545541763305664, 1.6432485580444336, 1.7003142833709717, 1.911815881729126, 2.1023285388946533, 2.1773910522460938])
    nearly_sorted_times = np.array([0.1697390079498291, 0.2751610279083252, 0.35994720458984375, 0.5371630191802979, 0.682565450668335, 0.7143869400024414, 0.9703342914581299, 0.9932212829589844, 1.1789438724517822, 1.3136160373687744, 1.3425483703613281, 1.483445167541504, 1.6322522163391113, 2.0996885299682617, 2.0456745624542236])
    reverse_sorted_times = np.array([0.1089317798614502, 0.255108118057251, 0.3162379264831543, 0.5472440719604492, 0.6074798107147217, 0.7668356895446777, 0.9620559215545654, 1.0597748756408691, 1.1092748641967773, 1.3711426258087158, 1.459726333618164, 1.6021757125854492, 1.8361663818359375, 1.6604435443878174, 2.0050265789031982])
    random_sorted_times = np.array([0.11710906028747559, 0.2751917839050293, 0.3446469306945801, 0.4791140556335449, 0.6018576622009277, 0.7094292640686035, 0.938995361328125, 0.9465370178222656, 1.1319715976715088, 1.1898584365844727, 1.4208884239196777, 1.5773372650146484, 1.7124269008636475, 1.7194459438323975, 1.9521324634552002])

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

    plt.title('All cases of Merge Sort')
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

