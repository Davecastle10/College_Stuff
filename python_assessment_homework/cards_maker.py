
def create_deck():

    card_nums = ['A', '1','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'spades']
    final_deck = []
    temp_card = []
    for i in range(4):
        for iterant in range(13):
            temp_card = [card_nums[iterant], suits[i]]
            final_deck.append(temp_card)
    return final_deck
    
print(create_deck())
