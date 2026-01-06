def combine(lis):
    lis_new=[]

    for elemt_one in range(0,len(lis)):
        for elemt_two in range(0,len(lis)):
            # print(lis[elemt_one],lis[elemt_two])
            my_tup=tuple([lis[elemt_one],lis[elemt_two]])
            # print(my_tup)
            if lis[elemt_one] !=lis[elemt_two]:
                lis_new.append(my_tup)
                # print(lis_new)

    print("Set of list")
    return lis_new
   
print(combine([2,3,4,5,6,7]))