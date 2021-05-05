arr = [8,5,2,6,1,4,9,3,7,0]

def select_sort(arr):
    for i in range(len(arr)):
        min_val = arr[i]
        index_min = i
        for j in range(i+1, len(arr)):
            if min_val > arr[j]:
                min_val = arr[j]
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]
    return arr

print(select_sort(arr))
