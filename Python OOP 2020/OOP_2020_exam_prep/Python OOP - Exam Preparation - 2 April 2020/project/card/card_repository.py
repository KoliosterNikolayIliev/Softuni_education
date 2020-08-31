from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        card_names = [x.name for x in self.cards]
        if card.name in card_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card = self.find(card)
        self.cards.remove(card)
        self.count -= 1

    def find(self, name: str):
        card = [x for x in self.cards if x.name == name][0]
        return card
