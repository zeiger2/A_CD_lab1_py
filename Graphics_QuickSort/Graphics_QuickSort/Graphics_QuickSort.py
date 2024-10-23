import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def SortedArray():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    sorted_times = np.array([0.047971248626708984, 0.5704522132873535, 1.1597232818603516, 1.7314214706420898, 2.294534206390381, 2.84875226020813, 3.6166670322418213, 4.490989685058594, 8.61497712135315, 11.572803497314453, 11.956952333450317, 15.336101293563843, 16.407600164413452, 15.181761741638184, 18.788347959518433])

    p = Polynomial.fit(sizes, sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for sorted array with regression curve (Quick Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def NearSortedArray():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    nearly_sorted_times = np.array([0.12717032432556152, 1.8031508922576904, 3.717944383621216, 5.6246161460876465, 4.5351362228393555, 7.012730360031128, 8.074693202972412, 10.294122457504272, 7.996476411819458, 13.389690160751343, 14.94700026512146, 15.453686714172363, 16.108301639556885, 16.662757635116577, 20.825777053833008])

    p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    nearly_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, nearly_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for nearly-sorted array with regression curve (Quick Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def ReverseSorted():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    reverse_sorted_times = np.array([0.18888211250305176, 2.1166884899139404, 1.798027753829956, 2.7977755069732666, 8.63939118385315, 7.002409219741821, 10.060767889022827, 11.892349004745483, 11.317625761032104, 11.557964324951172, 15.418451309204102, 18.19173502922058, 10.135722160339355, 17.031106233596802, 16.55787205696106])

    p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    reverse_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, reverse_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for reverse-sorted array with regression curve (Quick Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def RandomSorted():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    random_sorted_times = np.array([0.05915570259094238, 0.786292552947998, 1.647937536239624, 2.6990227699279785, 4.3513689041137695, 4.956403493881226, 6.5059521198272705, 7.374005556106567, 7.6833274364471436, 8.606997013092041, 10.40755295753479, 11.183074235916138, 12.885019540786743, 13.772489547729492, 14.923906564712524])

    p = Polynomial.fit(sizes, random_sorted_times, deg=2)
    sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
    random_sorted_times_smooth = p(sizes_smooth)

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, random_sorted_times, color='red', label='Algorithm result')
    plt.plot(sizes_smooth, random_sorted_times_smooth, color='blue', label='Regression curve')

    plt.title('Execution time for random-sorted array with regression curve (Quick Sort)')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.legend()

    plt.show()
def AllIn():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    sorted_times = np.array([0.047971248626708984, 0.5704522132873535, 1.1597232818603516, 1.7314214706420898, 2.294534206390381, 2.84875226020813, 3.6166670322418213, 4.490989685058594, 8.61497712135315, 11.572803497314453, 11.956952333450317, 15.336101293563843, 16.407600164413452, 15.181761741638184, 18.788347959518433])
    nearly_sorted_times = np.array([0.12717032432556152, 1.8031508922576904, 3.717944383621216, 5.6246161460876465, 4.5351362228393555, 7.012730360031128, 8.074693202972412, 10.294122457504272, 7.996476411819458, 13.389690160751343, 14.94700026512146, 15.453686714172363, 16.108301639556885, 16.662757635116577, 20.825777053833008])
    reverse_sorted_times = np.array([0.18888211250305176, 2.1166884899139404, 1.798027753829956, 2.7977755069732666, 8.63939118385315, 7.002409219741821, 10.060767889022827, 11.892349004745483, 11.317625761032104, 11.557964324951172, 15.418451309204102, 18.19173502922058, 10.135722160339355, 17.031106233596802, 16.55787205696106])
    random_sorted_times = np.array([0.05915570259094238, 0.786292552947998, 1.647937536239624, 2.6990227699279785, 4.3513689041137695, 4.956403493881226, 6.5059521198272705, 7.374005556106567, 7.6833274364471436, 8.606997013092041, 10.40755295753479, 11.183074235916138, 12.885019540786743, 13.772489547729492, 14.923906564712524])

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

    plt.title('All cases of Quick Sort')
    plt.xlabel('Array size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.show()
def AllInDot():
    sizes = np.array([1000, 11000, 21000, 31000, 41000, 51000, 61000, 71000, 81000, 91000, 101000, 111000, 121000, 131000, 141000])
    sorted_times = np.array([0.047971248626708984, 0.5704522132873535, 1.1597232818603516, 1.7314214706420898, 2.294534206390381, 2.84875226020813, 3.6166670322418213, 4.490989685058594, 8.61497712135315, 11.572803497314453, 11.956952333450317, 15.336101293563843, 16.407600164413452, 15.181761741638184, 18.788347959518433])
    nearly_sorted_times = np.array([0.12717032432556152, 1.8031508922576904, 3.717944383621216, 5.6246161460876465, 4.5351362228393555, 7.012730360031128, 8.074693202972412, 10.294122457504272, 7.996476411819458, 13.389690160751343, 14.94700026512146, 15.453686714172363, 16.108301639556885, 16.662757635116577, 20.825777053833008])
    reverse_sorted_times = np.array([0.18888211250305176, 2.1166884899139404, 1.798027753829956, 2.7977755069732666, 8.63939118385315, 7.002409219741821, 10.060767889022827, 11.892349004745483, 11.317625761032104, 11.557964324951172, 15.418451309204102, 18.19173502922058, 10.135722160339355, 17.031106233596802, 16.55787205696106])
    random_sorted_times = np.array([0.05915570259094238, 0.786292552947998, 1.647937536239624, 2.6990227699279785, 4.3513689041137695, 4.956403493881226, 6.5059521198272705, 7.374005556106567, 7.6833274364471436, 8.606997013092041, 10.40755295753479, 11.183074235916138, 12.885019540786743, 13.772489547729492, 14.923906564712524])

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

    plt.title('All cases of Quick Sort')
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

