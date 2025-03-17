bids = {}

last_player = False


def get_gratest_bid(bids_dict):


    max_bid = max(bids_dict.values())
    max_key = {key for key,value in bids_dict.items() if value == max_bid}
    
    print(f'Congrats {max_key} your the winner; Max bid: {max_bid}') 
   
while not last_player:
    
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))

    bids[name] = bid

    last_player = input('any other player? yes/no ' )=='no'

if last_player:
    get_gratest_bid(bids)