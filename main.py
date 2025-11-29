#!/usr/bin/env python3
"""
main.py - Entry point for the application.

Run with: python main.py
"""


from deck import Deck


def main():
    """Main entry point."""
    print("Hello, World!")
    # Your application logic goes here
    my_deck = Deck()
    print(f"Deck initialized with {len(my_deck.cards)} cards.")
    print(my_deck.cards[0].suit, my_deck.cards[0].value)
    print(my_deck.cards[0])
    print(my_deck.cards)
    print("*****************************************************")
    # random.shuffle(my_deck.cards)
    # print(my_deck.cards)


if __name__ == "__main__":
    main()
