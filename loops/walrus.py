# value=13

# if(reminder := value %2):
#     print(f"reminder is {reminder}: not divisible")
# else:
#     print(f"{reminder}divisible")

flavor=["cocolate","vanila","strawberry","mango"]

while(flavors:=input("Choose your flavor: ").lower()) not in flavor:
    print("Sorry this flavor is not available!")
print("any thing: {flavors}")

