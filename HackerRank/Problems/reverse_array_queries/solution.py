#!/usr/bin/python3
def reverse_array_query(arr, operations):
    for op in operations:
        index_1 = op[0]
        index_2 = op[1]
        if index_1 == 0 and index_2 == len(arr) - 1:
            arr = arr[::-1]
        else:
            slice_1 = arr[0:index_1]
            slice_2 = arr[index_2 + 1: len(arr)]
            l = arr[index_1: index_2 + 1]
            arr = slice_1 + l[::-1] + slice_2 
    return arr        

if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    operations = [[0, 9], [3, 5], [2, 4]]
    print(arr)
    reversed_arr = reverse_array_query(arr, operations)
    print(reversed_arr)
