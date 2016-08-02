# tens: write a function that takes a list of numbers and returns all adjacent sublists that sums to 10.
# you can assume that all numbers are non-negative (remember 0)

# tens([2,3,5,5,4,1,0,9,1])
# [[2,3,5] [5,5] [5,4,1] [5,4,1,0] [1,0,9] [0,9,1] [9,1]]


def tens(nums):
    start_idx = 0
    curr_sum = 0
    arr_tens_arr = []
    # builds up possible subarrays from the right, recording as appropriate
    for end_idx in range(len(nums)):
        curr_sum += nums[end_idx]
        # if sum is too big, remove numbers from left
        while curr_sum > 10:
            curr_sum -= nums[start_idx]
            start_idx += 1
        # if sum is desired sum, record it (and all 0 related derivations)
        if curr_sum == 10:
            arr_tens_arr.append(nums[start_idx: end_idx + 1])
            temp_start_idx = start_idx
            # record all subarrays with 0s removed from beginning
            while nums[temp_start_idx] == 0:
                temp_start_idx += 1
                arr_tens_arr.append(nums[temp_start_idx : end_idx + 1])

    return arr_tens_arr

print(tens([2,3,5,5,4,1,0,9,1]))
print(tens([2,3,5,5,4,1,0,0,9,1]))
print(tens([0,2,3,5,5,4,1,0,0,9,1]))
print(tens([2,3,0,5,0,5,0,0,4,1,0,0,9,1]))
print(tens([2]))
print(tens([]))