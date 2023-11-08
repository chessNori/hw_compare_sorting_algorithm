import random
import matplotlib.pyplot as plt
import numpy as np


def random_data(number_data: int):
    data_list = []
    avr_data = 0.
    while (avr_data < 4999) or (avr_data > 5001):  # Analyze random
        data_list = []
        for _ in range(number_data):
            data_list.append(random.randint(0, 10000))

        avr_data = np.average(np.array(data_list))

    # if number_data == 1000:
    #     plt.hist(data_list, label='Data Distribution(n=1000)')
    #     plt.show()

    return data_list


def plot_results(insertion, merge, heap, quick):
    plt.figure(figsize=(11, 11))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    plt.subplot(2, 2, 1)
    plt.plot(insertion)
    plt.title('Insertion Sort')
    plt.xlabel('Number of data')
    plt.ylabel('Duration of time(sec)')

    plt.subplot(2, 2, 2)
    plt.plot(merge)
    plt.title('Merge Sort')
    plt.xlabel('Number of data')
    plt.ylabel('Duration of time(sec)')

    plt.subplot(2, 2, 3)
    plt.plot(heap)
    plt.title('Heap Sort')
    plt.xlabel('Number of data')
    plt.ylabel('Duration of time(sec)')

    plt.subplot(2, 2, 4)
    plt.plot(quick)
    plt.title('Quick Sort')
    plt.xlabel('Number of data')
    plt.ylabel('Duration of time(sec)')

    plt.show()

    x = list(range(len(insertion)))
    # plt.plot(x, insertion, 'indianred', label='insertion sort')
    plt.plot(x, merge, 'seagreen', label='merge sort')
    plt.plot(x, heap, 'cornflowerblue', label='heap sort')
    plt.plot(x, quick, 'orange', label='quick sort')
    plt.xlabel('Number of data')
    plt.ylabel('Duration of time(sec)')
    plt.legend()

    plt.show()
