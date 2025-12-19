def order():

    order_amount=int(input("Order ammount is: "))

    delivery_fee= 0 if order_amount >300 else 50        #ternary operator :- user to perform operation in single line ..

    print(f"Your delivery fee is: {delivery_fee}")
    print("Total order amount is:" ,order_amount+ delivery_fee)

order()

