# write a function that takes an array of numbers and returns the largest sum of 3 adjacent numbers in the array


# Solution uses a technique similar to string search, so we don't recalculate the sum at each position, we just slide
# the window subtracting off the first element and adding on the newest element
def max_run(arr):
    if len(arr) <= 3:
        return sum(arr)
    curr_sum = sum(arr[:3])
    max_sum = curr_sum
    for idx in range(3, len(arr)):
        curr_sum -= arr[idx - 3]
        curr_sum += arr[idx]
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_run([]))
print(max_run([2, 2]))
print(max_run([-9, 2,-15,1]))
print(max_run([3, 2, 0]))
print(max_run([3, 2, 0, 7]))
print(max_run([2, 3, 4, 0, -3, 5, 9, -2]))

