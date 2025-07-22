# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def find_higher_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is "{winner}" with a bid of ${highest_bid}.')

bids = {} # It doesn't reset to zero every time the 'while loop' runs.
continue_bidding = True
while continue_bidding:
    # bids = {} -> If inside 'while loop', lose all of previous data.
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    # Dictionary 에서 [] 안에 key를 넣어주면, '해당 key'에 접근하거나 '새로운 key'를 생성 가능.
    bids[name] = price # 사용자가 입력한 "name"을 Dictionary bids의 새로운 key로 만들고, 그 key에 사용자가 입력한 price 값을 연결하여 저장해라.
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_higher_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20) # Clear the screen in between bids
