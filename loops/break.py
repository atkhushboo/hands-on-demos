stock=["ginger","rice","milk","out of stock","potato","pasta","discontinued","maggie"]


for stocks in stock:
    if stocks=="out of stock":
        continue
    # print("out of stock")

    if stocks=="discontinued":
        print(f"{stocks}:-items")
        break
    print(f"{stocks}:-in stock items")
   
print("Stock discontinued")