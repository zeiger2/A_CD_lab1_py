from math import radians
import numpy as np
import matplotlib.pyplot as plt

def main():
    #x = np.arange(0, radians(1800), radians(12))
    #plt.plot(x, np.cos(x), 'b')
    #plt.savefig("test3.png", bbox_inches='tight')
    #plt.show()

    # Определяем диапазон входных данных
    n = np.linspace(1, 100, 400)

    # Определяем временные сложности
    O_1 = np.ones_like(n)          # O(1)
    O_n = n                        # O(n)
    O_n_log_n = n * np.log(n)     # O(n log n)
    O_n_squared = n ** 2          # O(n^2)

    O1 =  n*(n-1)/2
    O2 = n*(n-1)/4
    O3 = n * np.log(n) + n
    O4 = n * np.log(n)
    O5 = n ** (3/2)
    O6 = n * (np.log(n))**2
    O7 = n * np.log(n) - n

    # Создание графика
    plt.figure(figsize=(10, 6))
    #plt.plot(n, O_1, label='O(1)', color='blue')
    #plt.plot(n, O_n, label='O(n)', color='orange')
    #plt.plot(n, O_n_log_n, label='O(n log n)', color='green')
    #plt.plot(n, O_n_squared, label='O(n²)', color='red')


    #plt.savefig("2.png", bbox_inches='tight')
    plt.plot(n, O1, label='Сортировка выбором и Пузырьковая сортировка: n*(n-1)/2', color='blue')
    plt.plot(n, O2, label='Сортировка вставкой: n*(n-1)/4', color='orange')
    plt.plot(n, O3, label='Сортировка слиянием и быстрая сортировка: nlog(n) + n', color='purple')
    #plt.plot(n, O4, label='Сортировка Шелл(последовательность Шелла): nlog(n)', color='red')
    #plt.plot(n, O5, label='Сортировка Шелл(последовательность Хиббарта): n**(3/2)', color='pink')
    #plt.plot(n, O6, label='Сортировка Шелл(последовательность Пратта): n log^2 n', color='gray')
    plt.plot(n, O6, label='Пирамидальная сортировка: nlog(n) - n', color='black')

    # Настройка графика
    plt.title('Графики временной сложности')
    plt.xlabel('Размер входных данных n')
    plt.ylabel('Время выполнения')
    plt.ylim(0, 200)  # Ограничение по оси Y для лучшего отображения
    plt.xlim(1, 50)  # Ограничение по оси X
    plt.legend()
    plt.grid()

    # Показать график
    plt.show()

main()

