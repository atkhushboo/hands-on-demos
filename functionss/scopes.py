cafe="CoffeeCut"   # Globle Scope

def order_cofee():
    coffee_name="Espresso"    #Local scope.

    print(f"Local Scope of Coffe is: {coffee_name}")

print(f"Globale scope of Function Cafe Name is: {cafe}")

coffee_names="latte"
order_cofee()
print(f"Enclosing scop of function {coffee_names}")
