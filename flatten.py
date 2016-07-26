
def flatten(arr, new_arr=[]):
    if arr == []:
        return new_arr
    elif type(arr[0]) == list:
        return flatten(arr[1:], flatten(arr[0], new_arr))
    else:
        new_arr.append(arr[0])
        return flatten(arr[1:], new_arr)

print(flatten([[1,2, [7, [], [8,9]] , 3],[] ,[4, [5]]]))