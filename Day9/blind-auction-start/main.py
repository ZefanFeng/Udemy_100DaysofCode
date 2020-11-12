from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bid_data = {}
should_continue  = True

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner_list = []
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount >= highest_bid:
      highest_bid = bid_amount
      winner = bidder
      winner_list.append(winner)
  print(f"The winner is {winner_list} with a bid of ${highest_bid}. ")

while should_continue:
  name = input("What's ur name?\n")
  money = int(input("What's your bid?$\n"))
  # add new bid
  bid_data[name] = money 
  # should continue?
  again = input('Are there any other bidders? Type"yes" or "no".\n').lower
  if again == "yes":
    clear()
  elif again == "no" :
    clear()
    should_continue = False
    # find highest bid, could be multiple
    #winner_list = []
    #winner = max(bid_data, key = bid_data.get)
    #win_bid = bid_data[winner]
    #winner_list.append(winner) 
    #print(f"The winner is {winner_list} with a bid of {win_bid}. ")
    find_highest_bidder(bid_data)





