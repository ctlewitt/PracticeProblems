import random
import time


def random_list(n):
    return [random.random() for _ in range(n)]

def time_me(func):
    def timed_funcion(list):
        start = time.time()
        func(list)
        end = time.time()
        total_time = end - start
        print("sorting list of size {} with {} took {} milliseconds".format(
            len(list), func.__name__, total_time * 1000)
        )
    return timed_funcion

@time_me
def insertion_sort(xs):
    result = []
    for x in xs:
        if not result:
            result.append(x)
        else:
            for i, r in enumerate(result+[float("inf")]):
                if r > x:
                    break
                result.insert(i, x)
    return result

@time_me
def quick_sort(xs):
    return quicksort(xs)

def quicksort(xs):
    if len(xs) <= 1:
        return xs
    pivot = xs[0]
    left = []
    right = []
    for x in xs[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)


# task: refactor this by writing a decorator for printing out timing
# information and annotating the sorting functions above with it, such
# we don't have to have any timing related code in the loop below

def measure_timings(sort_functions):
    for sort_function in sort_functions:
        for size in [10, 100, 1000, 10000]:
            sort_function(random_list(size))


measure_timings([quick_sort, insertion_sort])