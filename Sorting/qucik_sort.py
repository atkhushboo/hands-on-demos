def qucik_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for item in arr[:-1]:
        if item <pivot:
            left.append(item)
        else:
            right.append(item)
            print(right)
    sorted_arr=left+[pivot]+right
    print(sorted_arr)
arr=[1,2,6,7,5,9,33]
print(qucik_sort(arr))