# def multiple(*arg):
#     return arg

# print(multiple("khushboo","atul"))  #postional multiple value arguments
# # print(multiple())

# def mobile(*brand_name ,**details):
#     print(f"Brand name is: {','.join(brand_name)}")
#     print("About Mobile: ")

#     for key,val in details.items():
#         print(f".{key.capitalize()},{val}")

# mobile("Samsung","iphone",color="White",storage="128Gb",battery="65000mh")

# def chai_order(cup):
#     if cup ==0:
#         return "Soory its over!"
    
#     return "Chai is ready"
# print(chai_order(4))

#..................... #recursive.......................

# def fact(n):
#     print(f"{n}! *")

#     if n==0 or n==1:
#         return 1
#     else:
#       return n* fact(n-1)        #recursive case 
# print(fact(5))

##..................... #lambdas function.......................

add=lambda a,b : a+b    #variable = lambda argument:expresion
print(add(10,4))


mull = lambda x ,y:x*y
print(mull(2,5))