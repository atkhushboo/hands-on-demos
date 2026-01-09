def two_D(listt):
    temp=[]
    new_list=[]
    for num in range(0,len(listt)):
        num=num+1
        temp.append(listt[num-1])

        if num%3==0:
            new_list.append(temp)
            temp=[]
    return new_list

print(two_D([1,2,3,4,5,6,7,8,9]))
