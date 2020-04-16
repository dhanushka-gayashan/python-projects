from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '1 2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self):
        print('Creating New Ordered Deck!!')
        self.all_cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('Shuffling Deck')
        shuffle(self.all_cards)

    def split_in_half(self):
        return self.all_cards[:26], self.all_cards[26:]


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return 'contains {} cards'.format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        draw_card = self.hand.remove_card()
        print('{} has placed: {}.\n'.format(self.name, draw_card))
        return draw_card

    def remove_war_cards(self):
        if len(self.hand.cards) < 3:
            return self.hand.cards

        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.remove_card())

        return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


print("Welcome to War, Let's begin...")

# Create 2 half decks
deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()

# Create Players
computer = Player("computer", Hand(half1))

name = input("Enter your name: ")
user = Player(name, Hand(half2))

# Play War Automatically
total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds += 1

    print("Time for a new round")
    print("Here are the current standings...")

    print(user.name + " " + str(len(user.hand.cards)))
    print(computer.name + " " + str(len(computer.hand.cards)))

    print('Play a card...\n')

    table_cards = []

    c_card = computer.play_card()
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_count += 1

        table_cards.extend(computer.remove_war_cards())
        table_cards.extend(user.remove_war_cards())

        c_card = computer.play_card()
        u_card = user.play_card()

        table_cards.append(c_card)
        table_cards.append(u_card)

        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

# Final Result
print("Game over... Number of rounds: " + str(total_rounds))
print("War happened: " + str(war_count) + " times")

print("Does the computer still have cards? " + str(computer.still_has_cards()))
print("Does the " + user.name + " still have cards? " + str(user.still_has_cards()))

