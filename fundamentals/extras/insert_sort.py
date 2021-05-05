arr = [8,5,2,6,1,4,9,3,7,0]

def select_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = i -1
        while j>=0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr
print(select_sort(arr))