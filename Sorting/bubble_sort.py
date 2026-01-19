# in-built sorting ...... internally use Timsort...
arr=[3,6,9,4,6,2]
# arr.sort()
result=sorted(arr)
print(result)

#.........bubble sort...............

def bubble_sort(listt):
    for i in range(len(listt)-1,0,-1):
        for j in range(i):
            if listt[j]>listt[j+1]:
                listt[j],listt[j+1]=listt[j+1],listt[j]
    return listt
print(bubble_sort([1,4,7,3,8,9,4]))