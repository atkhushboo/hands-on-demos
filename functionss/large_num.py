def large(listt):
    max=listt[0]
    for num in listt:
        if num >max:
            max=num
    return max
print(large([123,432,55,9,1,79]))