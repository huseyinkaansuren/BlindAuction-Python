#from replit import clear
#HINT: You can call clear() to clear the output in the console.
bid_dict={}
iscontinue=True
def find_highest_bidder(bid_dict):
    max_bid = 0
    for bids in bid_dict:
        if max_bid < bid_dict[bids]:
            max_bid = bid_dict[bids]
            max_payed_name = bids
    print(f"Max payed is {max_payed_name} with {max_bid}")

while iscontinue:
    name=input("What is your name?:").lower()
    bid_price=int(input("Enter your Bid Price:$"))
    bid_dict[name]=bid_price
    selection=input("Does anybody play? 'y' for yes, 'n' for no:").lower()
    if selection=="n":
        iscontinue=False
        find_highest_bidder(bid_dict)