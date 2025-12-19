def check_temp():

    device_status =str(input("Device Status is: ")).lower()
    temprature= int(input("Temprature is : "))

    if device_status=="active":
        print("Device is active ")

        if temprature >38:
            print("High Temprature alert!")

        else:
            print("Temprature is Normal.")
    
    else:
        print("Device is Offline")

check_temp()
