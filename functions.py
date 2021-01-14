def hello(name):
    print(f"Hello, {name}!")

hello("Panaam")

# def create_user_dictionary(name, age):
#     if age < 13: 
#         return None
#     new_user = {
#         "name": name,
#         "age": age,
#         "can_vote": age >= 18,
#         "interest": []
#     }
#     return new_user

def create_user_dictionary(name, age, *args):
    if age < 13:
        return None
    interests_lists =[]
    for interests in args:
        interests_lists.append(interests)
    new_user = {
        "name": name,
        "age": age,
        "can_vote": age >= 18,
        "interest": interests_lists
    }
    return new_user

def create_invoice(buyer_id, items, **kwargs):
        """
        Optional  Keyword Arguments:
        tax_exempt: boolean set to True if the buyer is tax exempt
        etc...
        """
        total = 0 
        exempt = False
        if kwargs.get("tax_exempt"):
            exempt = True
        for item in items:
            total += (item["price"] * item ["count"]) * (1.0 if exempt else 1.07)
        report = {
            "total": total,
            "items": items,
            "buyer": buyer_id,
            "tax_exempt":exempt
        }
        return report
    
cart = [
{"price": 2.99, "count": 4},
{"price": .99, "count":1},
{"price": 599.99, "count": 1}
    ]

mine = create_invoice(987, cart, tax_exmept = True)
print(mine)


#Lambda Function

#x => x*2

#lambda x : x*2

cart = [
{"price": 2.99, "count": 4},
{"price": .99, "count":1},
{"price": 599.99, "count": 1}
]

total = sum(list(map(lambda item: item["price"] * item["count"], cart)))
print(total)




