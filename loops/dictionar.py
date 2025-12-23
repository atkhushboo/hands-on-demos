users=[
    {"id":1,"total":500,"coupon":"f20"},
    {"id":2,"total":1000,"coupon":"k30"},
    {"id":3,"total":2500,"coupon":"k50"}
]

discount={                            #dictionary instead of match case 
    "f20":(0,50),
    "k30":(0.3,0),
    "k50":(0.5,0),
}


for user in users:
    # print(user)
    percentage,flat = discount.get(user["coupon"],(0,0))
    offer = user["total"]*percentage+flat
    pay=user["total"]-offer
    print(f"user{user['id']}:affter use coupon you pay only : {pay}/-")

    # print(f"user{user['id']}: Amount:- {user['total']}/- and got coupun for next visit: {paid}/-")
