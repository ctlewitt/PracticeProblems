def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    rest = my_list[1:]
    left = quick_sort([filter(lambda x: x <= pivot, rest)])
    right = quick_sort([filter(lambda x: x > pivot, rest)])
    return left + [pivot] + right
