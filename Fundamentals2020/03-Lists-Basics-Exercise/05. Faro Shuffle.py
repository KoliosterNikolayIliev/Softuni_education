cards = input().split(' ')
number = int(input())

for _ in range(number):
    first_half = []
    second_half = []
    new_cards = []

    for j in range(0, len(cards) // 2):
        element = cards[j]
        first_half.append(element)
    for h in range(len(cards) // 2, len(cards)):
        element = cards[h]
        second_half.append(element)

    for m in range(len(first_half)):
        new_cards.append(first_half[m])
        new_cards.append(second_half[m])
    cards = new_cards
print(cards)
