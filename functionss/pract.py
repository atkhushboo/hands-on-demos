# Question 1: Reverse a String
# Write a program to reverse a string without using built-in reverse functions.

# name="Atul"
# arr=[]
# for word in name:
#     arr.insert(0,word)
#     # print(arr)
#     rev=''.join(arr)
# print(f"Reverse a string: {rev}")


#.........recursion.............#
# name="atul"
# def rever():
#     global name
#     arr=list(name)
#     if arr in name:
#         return
   
#     x=arr[::-1]
#     print(x)
#     rever()
# print(rever())

# n=0
# def number():
#     global n
#     if n==5:
#         return
#     n=n+1 
#     print(5-n)
#     number()
# print(number())

#  Question 3: Count Vowels in a String
# Write a program to count the number of vowels (a, e, i, o, u) in a string.

def check(s):
    flag = False
    vowel="aeiou"
    
    for vol in vowel:
        if vol in s:
            flag=True
    
    return flag
print(check("khush"))

    