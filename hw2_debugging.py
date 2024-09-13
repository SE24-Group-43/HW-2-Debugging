'''Python code for Merge Sort'''
import rand


def merge_sort(a):
    '''This function is merging the sorted arrays'''
    # print(a)
    if len(a) <= 1:
        return a

    half = len(a) // 2

    return recombine(merge_sort(a[:half]), merge_sort(a[half:]))
    # return recombine(merge_sort(a[:half]), merge_sort(a[half:]))


def recombine(left_arr, right_arr):
    '''This function recombines the sorted arrays'''
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)
print(arr_out)
