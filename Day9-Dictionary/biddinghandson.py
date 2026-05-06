import main

print(main.logo)

def find_highest_biddder(bidding_dict): #bidding_dict is a parameter name,we can use any
    #while sending parameter we should send proper one from the function call
    highest_bid = 0
    winner = ""
    #max(bidding_dict)
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids={}
continue_bidding = True #this is just a variable
while continue_bidding:
        name = input("whats your name ")  #** for variables we don't need to put "", only for dict we should use ""
        bid = int(input("whats your bid "))
        bids[name] = bid
        has_people = input("Are there any other bidders? Type 'yes' or 'no' \n ").lower()
        if has_people == "yes":
            continue_bidding = True
        else:
            continue_bidding = False
            find_highest_biddder(bids)
        print("\n"*20)







