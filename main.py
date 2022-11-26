from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#1 Show logo
print(logo)


#4 Add Name and Bid into a dictionary as the key and value
list_name_bid = []
name_and_bid = {}
bidding_finished = False

def highest_bid(score):
  highest_bid = 0
  winner = ""
  for bidder in score:
    bid_amount = score[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  #2 Ask for Name
  user_name = input("What is your name?: ")
  #3 Ask for Bid Price
  user_bid = int(input("What is your bid?: $"))
  

#5 Ask if there are other users who want to bid
  name_and_bid[user_name] = user_bid
  ask_another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if ask_another_bid == 'no':
    bidding_finished = True
    highest_bid(name_and_bid)
  elif ask_another_bid == 'yes':
    clear()
