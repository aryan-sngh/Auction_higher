

def greater(auction_dict):
    winner = " "
    higher = 0
    for keys in auction_dict:
        lower = auction_dict[keys]
        if lower>higher:
            higher = lower
            winner = keys
    print(f"winner is {winner} for bit higher price = {higher}")

should_continue = True
auction_dict = {}
while should_continue:
    name = input("enter your name")
    price = int(input("enter the price:"))
    auction_dict[name] = price
    yes_no = input("what to continue:")
    if yes_no == "no":
        should_continue = False
        print(greater(auction_dict))
        print("thank you ")
    else:
        print("\n"*100)



