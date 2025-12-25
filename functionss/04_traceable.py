def add_vat(price,vat_rate):

    return price *(100 +vat_rate)/100


orders=[12,20,15]

for order in orders:
    final_amount = add_vat(order,10)

    print(f"Order rate is: {order},including VAT Rate is: {final_amount}")