
arr =  [10, 3, 5, 7, 1, 9]
arr2 = [12, 3, 7, 4, 17, 2, 1, 0, 15, 5]
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
                
    return arr

print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Bubble sorting compares each item with it's right neighbor, if on right is greater, the numbers swap
    #On the first iteration the greatest number will have 'bubbled' to the far right
    #On each iteration another number becomes fixed on the right and no longer needs comparing
    #This process must continue until an iteration occurs with no swap
    
    #1. for each item in the array -> arr[n] should be compared to the next item -> arr[n + 1]
    #2. if arr[n] > arr[n+1] the items should swap places
    for i in range(0, len(arr)-1):
        lower_i = i
        for j in range(i+1, len(arr)):
            next_i = j
            while arr[lower_i] > arr[next_i]:
                arr[lower_i], arr[next_i] = arr[next_i], arr[lower_i]

    return arr

print(bubble_sort(arr2))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):


    return arr