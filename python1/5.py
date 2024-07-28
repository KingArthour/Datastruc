
bids=input("Enter All Bid : ")

bid_list=bids.split()
bid_list = [int(bid) for bid in bid_list]
bid_list.sort()


def vick_auct(bid_list):

    if len(bid_list)<=1:
        print("not enough bidder")
    elif bid_list[len(bid_list)-1] == bid_list[len(bid_list)-2]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {bid_list[len(bid_list)-1]} need to pay {bid_list[len(bid_list)-2]}")


vick_auct(bid_list)



