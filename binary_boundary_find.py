from collections import defaultdict

## tell how many of the number occur in the list
# if unsorted: iterate through with a counter; may as well create a dict as you go,
# so you can have them all in case they ask later

# if sorted: use binary search

# returns number of times num occurs in array arr
def get_num_instances_of_num(arr, num, is_sorted=False):
    if arr is None or len(arr) == 0:
        return 0
    if is_sorted:
        left_boundary_idx, right_boundary_idx = find_boundaries(arr, num)
        # check if num occurs at all (ie even at one of the endpoints; if arr[left bound] != num,
        # then left and right bound are in same place and num is not in array
        if arr[left_boundary_idx] != num:
            return 0
        return right_boundary_idx - left_boundary_idx + 1
    # unsorted; just get all counts and return count of num; if it's None, return 0
    return get_all_num_counts(arr).get(num) or 0

def get_all_num_counts(arr):
    num_counts = defaultdict(int)
    for num in arr:
        num_counts[num] += 1
        # if num in num_counts:
        #     num_counts[num] += 1
        # else:
        #     num_counts[num] = 1
    return num_counts

# returns the exact indexes of the first and last instances of num in the array (no off by 1 errors and no string splice formatting)
def find_boundaries(arr, num):
    # get left boundary index
    if arr[0] == num:
        left_boundary_idx = 0
    else:
        left_boundary_idx = find_left_boundary(arr, num, 0, len(arr)-1) + 1
    if arr[len(arr)-1] == num:
        right_boundary_idx = len(arr)-1
    else:
        right_boundary_idx = find_right_boundary(arr, num, 0, len(arr)-1) - 1
    return left_boundary_idx, right_boundary_idx

# finds the index of the first number greater than num in the array, unless the last element of the array is num
# then it returns the index of the last element in the array
def find_right_boundary(arr, num, left, right):
    if right - left <= 1:
        return right
    center = int((left + right) / 2)
    if num >= arr[center]: # right boundary is to the right of center
        return find_right_boundary(arr, num, center, right)
    if num < arr[center]: # right boundary is to the left of center
        return find_right_boundary(arr, num, left, center)

# finds the index of the last number smaller than num in the array, unless the first element of the array is num
# then it returns the index of the first element in the array
def find_left_boundary(arr, num, left, right):
    if right - left <= 1:
        return left
    center = int((left + right) / 2)
    if num <= arr[center]:
        return find_left_boundary(arr, num, left, center)
    if num > arr[center]:
        return find_left_boundary(arr, num, center, right)


# what am i looking for?
arr1 = [2, 2, 3, 3, 3, 4, 4]
arr2 = [2, 2, 3, 4, 4, 4]
arr3 = [3, 4, 4, 4]
arr4 = [2, 2, 2, 3]
arr5 = []
arr6 = [3,5,6,2,5,8,2,7, 52, 6,6,43,7,88,0]


print(arr1)
right_boundary_idx = find_right_boundary(arr1, 3, 0, len(arr1)-1)
left_boundary_idx = find_left_boundary(arr1, 3, 0, len(arr1)-1)
print("right bound idx: " + str(right_boundary_idx))
print("val@right bound: " + str(arr1[right_boundary_idx]))
print("left bound idx: " + str(left_boundary_idx))
print("val@left bound: " + str(arr1[left_boundary_idx]))
print(get_num_instances_of_num(arr1, 3, True))
print(get_num_instances_of_num(arr1, 3))

print()

print(arr2)
right_boundary_idx = find_right_boundary(arr2, 3, 0, len(arr2)-1)
left_boundary_idx = find_left_boundary(arr2, 3, 0, len(arr2)-1)
print("right bound idx: " + str(right_boundary_idx))
print("val@right bound: " + str(arr2[right_boundary_idx]))
print("left bound idx: " + str(left_boundary_idx))
print("val@left bound: " + str(arr2[left_boundary_idx]))
print(get_num_instances_of_num(arr2, 3, True))
print(get_num_instances_of_num(arr2, 3))

print()

print(arr3)
right_boundary_idx = find_right_boundary(arr3, 3, 0, len(arr3)-1)
left_boundary_idx = find_left_boundary(arr3, 3, 0, len(arr3)-1)
print("right bound idx: " + str(right_boundary_idx))
print("val@right bound: " + str(arr3[right_boundary_idx]))
print("left bound idx: " + str(left_boundary_idx))
print("val@left bound: " + str(arr3[left_boundary_idx]))
print(get_num_instances_of_num(arr3, 3, True))
print(get_num_instances_of_num(arr3, 3))
print()

print(arr4)
right_boundary_idx = find_right_boundary(arr4, 3, 0, len(arr4)-1)
left_boundary_idx = find_left_boundary(arr4, 3, 0, len(arr4)-1)
print("right bound idx: " + str(right_boundary_idx))
print("val@right bound: " + str(arr4[right_boundary_idx]))
print("left bound idx: " + str(left_boundary_idx))
print("val@left bound: " + str(arr4[left_boundary_idx]))
print(get_num_instances_of_num(arr4, 3, True))
print(get_num_instances_of_num(arr4, 3))
print()

print(arr5)
print(get_num_instances_of_num(sorted(arr5), 3, True))
print(get_num_instances_of_num(arr5, 3))

print(arr6)
print(get_num_instances_of_num(sorted(arr6), 52, True))
print(get_num_instances_of_num(arr6, 52))


print(arr6)
print(get_num_instances_of_num(sorted(arr6), 90, True))
print(get_num_instances_of_num(arr6, 90))
