#this is a max-heap alogorithm
#the algorirthm takes and array and a particular index
def get_left(i):
    return (2*i)

def get_right(i):
    return ((2*1) + 1)

def get_parent(i):
    return (i/2)

def max_heapify(arr , i):
    left = get_left(i)
    right = get_right(i)
    
    if left <= len(arr) and arr[left] > arr[right] :
        largest = left
    else: largest = i
    if right <= len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest] 
        arr[largest] = temp
        max_heapify(arr, largest)
        