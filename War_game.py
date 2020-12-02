import random

suits = ['Hearts', 'Dimonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12,
          'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                gen_card = Card(suit, rank)
                self.all_cards.append(gen_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Remove card
    def remove_one(self):
        return self.all_cards.pop(0)

    # Add cards
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.all_cards))


# game_logic

player_one = Player('One')
player_two = Player('Two')

round_num = 0
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

print("len(player_two.all_cards) {}".format(len(player_two.all_cards)))

while game_on:

    round_num += 1
    print('Round {}'.format(round_num))
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break

    # Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False


        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("War!")
            if len(player_one.all_cards) < 5:
                print("Player One cannot challenge, Player Two wins")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two cannot challenge, Player One wins")
                game_on = False
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())