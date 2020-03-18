
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    #put back together here
    #sorting happens here

    #our cursors
    a = 0
    b = 0
    
    for k in range(0, elements):
        #compare a and b
        #if a is out of range, push b and iterate
        #if b is out of range, push a and iterate
        if a >= len(arrA): #we're done with arrA, push remaining arrB
            merged_arr[k] = arrB[b]
            b += 1
        elif b >= len(arrB): #we're done with arrB, push remaining arrA
            merged_arr[k] = arrA[a]
            a += 1
        #if a is smaller, put in array and iterate
        #if b is smaller, put in array and interate
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b +=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
unsorted = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

def merge_sort( arr ):
    # TO-DO
    # split here
    # find the middle of arr
    mid = len(arr)//2
    # base case is len(arr) > 1 (keep going until length is not > 1)
    if len(arr) > 1:
        #sort stuff in left and put it to the left
        left = merge_sort(arr[:mid])

        #sort stuff in right put it to the right
        right = merge_sort(arr[mid:])

        #merge left and right
        arr = merge(left, right)
        
    return arr

print(merge_sort(unsorted))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
