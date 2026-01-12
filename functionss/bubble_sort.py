# in-built sorting ...... internally use Timsort...
arr=[3,6,9,4,6,2]
# arr.sort()
result=sorted(arr)
print(result)


#.........bubble sort...............
def matrixx(lst):
    
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            # print(i,j)
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return(lst)
        
print(matrixx([3,4,5,2,8,9,1,6,7]))

#2D 1D

