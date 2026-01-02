# def show(num):
#     if num==0:
#         return
#     print(num)  
#     show(num-1)
# print(show(5))

def fact(num):
    print(f"the factorial is: {num}!")
    # print(f"the factorial is: {num}!*")
    if num==0 or num==1:
        return 1
    else:
         return num* fact(num-1)
    
print(fact(6))
