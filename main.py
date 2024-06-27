from random import choice
from art import logo
from os import system


def clear():
    system('cls')


def draw_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack_game():
    print(logo)
    user_cards, computer_cards = [], []
    for n in range(2):
        user_cards.append(draw_a_card())
        computer_cards.append(draw_a_card())

    # user drawing cards
    while True:
        user_score, computer_score = calculate_score(user_cards), calculate_score(computer_cards)

        print(f"User cards: {user_cards}. Current score: {user_score}")
        print(f"Computer card: {computer_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            break

        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_cards.append(draw_a_card())
        else:
            break

    # computer drawing cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_a_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        blackjack_game()
