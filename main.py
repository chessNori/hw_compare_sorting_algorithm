import func
import sort_func
from time import time

insertion_sort_time = [0.]
merge_sort_time = [0.]
heap_sort_time = [0.]
quick_sort_time = [0.]

print('n: 001 >> ', end='')
for n in range(1, 1001):
    if n % 100 == 0:
        print('\nn: ' + str(n) + ' >> ', end='')
    if n % 10 == 0:
        print('*', end='')

    data = func.random_data(n)
    start = time()
    sort_func.insertion_sort(data)
    insertion_sort_time.append(time() - start)

    data = func.random_data(n)
    start = time()
    sort_func.merge_sort(data)
    merge_sort_time.append(time() - start)

    data = func.random_data(n)
    start = time()
    sort_func.heap_sort(data)
    heap_sort_time.append(time() - start)

    data = func.random_data(n)
    start = time()
    sort_func.quick_sort(data, 0, n - 1)
    quick_sort_time.append(time() - start)

func.plot_results(insertion_sort_time, merge_sort_time, heap_sort_time, quick_sort_time)
