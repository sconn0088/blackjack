import random, re

deck = {
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "Ace of Spades": 11,
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10,
    "Ace of Clubs": 11,
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "Ace of Diamonds": 11,
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Hearts": 11
}

card_types = list(deck.keys())

print("Welcome to  Blackjack!")
print("Follow the prompts to bet against the House and win big.")
print("First, what is your name?")

name = raw_input("> ")

print("\nNice to meet you, %s!") % (name)
print("How many decks would you like to play with?")
print("Choose between 2 and 10:")

def deck_size():
    number = raw_input("")
    try:
        number = int(number)
        if number >= 2 and number <= 10:
            return number
        else:
            print("Choose a number between 2 and 10:")
            deck_size()
    except:
        print("Please input a number between 2 and 10:")
        deck_size()

number_of_decks = deck_size()
multiple_decks = []

def deck_builder(number):
    i = 0
    while i < number:
        multiple_decks.append(card_types)
        i += 1
    return multiple_decks

playing_decks = deck_builder(number_of_decks)
# flatten list of lists into single list
playing_decks = [item for sublist in playing_decks for item in sublist]

print("\nWe'll start you with $1000.")
print("You can play with a bet of $25, $50, $100, or $200.")
print("Type in just the number without the '$.'")
print("What would you like your bet to be?")

money = 1000
def place_bet():
    bet = raw_input("")
    try:
        bet = int(bet)
        if bet == 25 or bet == 50 or bet == 100 or bet == 200:
            return bet
        else:
            print("Choose a bet of 25, 50, 100, or 200.")
            place_bet()
    except:
        print("Choose a bet of 25, 50, 100, or 200.")
        place_bet()
bet = place_bet()

def additional_bet(add_bet, money):
    if add_bet <= money:
        return add_bet
    else:
        print("You don't have that much money...")
        additional_bet(add_bet, money)

def deal_my_hand():
    my_hand = []
    my_hand.append(random.choice(playing_decks))
    playing_decks.remove(my_hand[0])
    my_hand.append(random.choice(playing_decks))
    playing_decks.remove(my_hand[1])
    return my_hand

def deal_dealer_hand():
    dealer_hand = []
    dealer_hand.append(random.choice(playing_decks))
    playing_decks.remove(dealer_hand[0])
    dealer_hand.append(random.choice(playing_decks))
    playing_decks.remove(dealer_hand[1])
    return dealer_hand

def user_card_count(my_hand):
    user_count = 0
    for card in my_hand:
        if re.match("[2-6]", card):
            user_count += 1
        if re.match("10", card):
            user_count -= 1
        if re.match("[A-Z]", card):
            user_count -= 1
    return user_count

def computer_card_count(dealer_hand):
    computer_count = 0
    for card in dealer_hand:
        if re.match("[2-6]", card):
            computer_count += 1
        if re.match("10", card):
            computer_count -= 1
        if re.match("[A-Z]", card):
            computer_count -= 1
    return computer_count

def user_points(my_hand):
    user_points = 0
    for card in my_hand:
        user_points += deck[card]
    return user_points

def computer_points(dealer_hand):
    dealer_points = 0
    for card in dealer_hand:
        dealer_points += deck[card]
    return dealer_points

while money > 0 and len(playing_decks) >= 4:
    deck["Ace of Spades"] = 11
    deck["Ace of Clubs"] = 11
    deck["Ace of Diamonds"] = 11
    deck["Ace of Hearts"] = 11
    money -= bet
    my_hand = deal_my_hand()
    dealer_hand = deal_dealer_hand()
    my_points = user_points(my_hand)
    dealer_points = computer_points(dealer_hand)
    user_count = user_card_count(my_hand)
    computer_count = computer_card_count(dealer_hand)
    running_count = user_count + computer_count
    print("\nMy hand: %s" % my_hand)
    print("My points: %d" % my_points)
    print("Dealer hand: %s" % dealer_hand)
    print("Dealer points: %d" % dealer_points)
    print("Running count: %d" % running_count)
    print("Winnings: $%d" % money)
    blackjack = False
    if dealer_points == 21:
        print("Dealer has Blackjack! You lose!")
        blackjack = True
    if my_points == 21:
        print("You have Blackjack! You win 2.5x your bet!")
        money += bet * 2.5
        blackjack = True
    if blackjack == False:
        skip_cpu = False
        if len(my_hand) == 2:
            if re.match("[Ace]", my_hand[0]) and re.match("[Ace]", my_hand[1]):
                my_points = 12
        if len(dealer_hand) == 2:
            if re.match("[Ace]", dealer_hand[0]) and re.match("[Ace]", dealer_hand[1]):
                dealer_points = 12
        print("\nDo you want to bet additional money?")
        print("Type 'y' for Yes or 'n' for No.")
        bet_additional = raw_input("")
        if bet_additional == "y" or bet_additional == "Y":
            print("How much of your remaining money would you like to bet?")
            add_money = int(raw_input(""))
            current_bet  = additional_bet(add_money, money)
            money -= current_bet
        if bet_additional == "n" or bet_additional == "N":
            current_bet = 0
        while my_points < 21:
            print("\nType 'h' to Hit or 's' to Stay.")
            h_or_s_choice = raw_input("")
            if h_or_s_choice == "h" or h_or_s_choice == "H":
                my_hand.append(random.choice(playing_decks))
                playing_decks.remove(my_hand[-1])
                my_points += deck[my_hand[-1]]
                if re.match("[2-6]", my_hand[-1]):
                    running_count += 1
                if re.match("10", my_hand[-1]):
                    running_count -= 1
                if re.match("[A-Z]", my_hand[-1]):
                    running_count -= 1
                print("\nMy hand: %s" % my_hand)
                print("My points: %d" % my_points)
                print("Dealer hand: %s" % dealer_hand)
                print("Dealer points: %d" % dealer_points)
                print("Running count: %d" % running_count)
                print("Winnings: $%d" % money)
                if my_points == 21:
                    print("You have Blackjack! You win 2.5x your bet!")
                    money += bet * 2.5
                    money += current_bet * 2.5
                    skip_cpu = True
                    break
                if my_points > 21:
                    if any("Ace" in card for card in my_hand):
                        my_points = 0
                        for card in my_hand:
                            if re.match("[Ace]", card):
                                deck[card] = 1
                            my_points += deck[card]
                        print("\nThe Ace is now worth 1.")
                        print("\nMy hand: %s" % my_hand)
                        print("My points: %d" % my_points)
                        print("Dealer hand: %s" % dealer_hand)
                        print("Dealer points: %d" % dealer_points)
                        print("Running count: %d" % running_count)
                        print("Winnings: $%d" % money)
                        if my_points > 21:
                            print("You have over 21 points. You bust!")
                            skip_cpu = True
                            break
                    else:
                        print("You have over 21 points. You bust!")
                        skip_cpu = True
                        break
            if h_or_s_choice == "s" or h_or_s_choice == "S":
                break
        if skip_cpu == False:
            end_cpu_turn = False
            while dealer_points < 17:
                dealer_hand.append(random.choice(playing_decks))
                playing_decks.remove(dealer_hand[-1])
                dealer_points += deck[dealer_hand[-1]]
                if re.match("[2-6]", dealer_hand[-1]):
                    running_count += 1
                if re.match("10", dealer_hand[-1]):
                    running_count -= 1
                if re.match("[A-Z]", dealer_hand[-1]):
                    running_count -= 1
                print("\nMy hand: %s" % my_hand)
                print("My points: %d" % my_points)
                print("Dealer hand: %s" % dealer_hand)
                print("Dealer points: %d" % dealer_points)
                print("Running count: %d" % running_count)
                print("Winnings: $%d" % money)
                if dealer_points == 21:
                    print("Dealer has Blackjack! You lose!")
                    end_cpu_turn = True
                    break
                if dealer_points > 21:
                    if any("Ace" in card for card in dealer_hand):
                        dealer_points = 0
                        for card in dealer_hand:
                            if re.match("[Ace]", card):
                                deck[card] = 1
                            dealer_points += deck[card]
                        print("\nThe Ace is now worth 1.")
                        print("\nMy hand: %s" % my_hand)
                        print("My points: %d" % my_points)
                        print("Dealer hand: %s" % dealer_hand)
                        print("Dealer points: %d" % dealer_points)
                        print("Running count: %d" % running_count)
                        print("Winnings: $%d" % money)
                        if dealer_points > 21:
                            print("Dealer has over 21 points. You win!")
                            money += bet * 2
                            money += current_bet * 2
                            end_cpu_turn = True
                            break
                    else:
                        print("Dealer has over 21 points. You win!")
                        money += bet * 2
                        money += current_bet * 2
                        end_cpu_turn = True
                        break
            if end_cpu_turn == False:
                if dealer_points >= 17 and dealer_points < 21:
                    if my_points > dealer_points:
                        print("You win!")
                        money += bet * 2
                        money += current_bet * 2
                    if my_points < dealer_points:
                        print("You lose!")
                    if my_points == dealer_points:
                        print("It's a tie. You push your bet.")
                        money += bet
                        money += current_bet

def user_winnings(money):
    if money <= 1000:
        winnings = 0
        return winnings
    if money > 1000:
        winnings = money - 1000
        return winnings
winnings = user_winnings(money)

print("\nGame over.")
print("%s's winnings: %d" % (name, winnings))
print("\nThank you for playing Blackjack!")
