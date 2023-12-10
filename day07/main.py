from audioop import reverse


f = open("./input.txt").readlines()
f = [line.replace("\n", "") for line in f]

hands = [[line.split(" ")[0], int(line.split(" ")[1]), 0] for line in f]
cards = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))

# part 1

for i in range(len(hands)):
    hand = hands[i][0]
    amounts = []
    for card in cards:
        amount = hand.count(card)
        if amount > 0:
            amounts.append(amount)
    score = 0
    highCard = sum(cards.index(hand[-(c+1)])*100**c for c in range(len(hand)))
    if 5 in amounts:
        score = 7*100**len(hand) + highCard
    elif 4 in amounts:
        score = 6*100**len(hand) + highCard
    elif 3 in amounts and 2 in amounts:
        score = 5*100**len(hand) + highCard
    elif 3 in amounts:
        score = 4*100**len(hand) + highCard
    elif amounts.count(2) == 2:
        score = 3*100**len(hand) + highCard
    elif 2 in amounts:
        score = 2*100**len(hand) + highCard
    else:
        score = 1*100**len(hand) + highCard
    hands[i][2] = score

sorted_hands = sorted(hands, key=lambda el: el[2])
winnings = 0
for i in range(len(sorted_hands)):
    winnings += sorted_hands[i][1] * (i+1)

print(winnings)

# part 2

cards = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))

for i in range(len(hands)):
    hand = hands[i][0]
    amounts = []
    jokers = hand.count("J")
    for card in cards[1:]:
        amount = hand.count(card)
        amounts.append(amount)
    score = 0
    highCard = sum(cards.index(hand[-(c+1)])*100**c for c in range(len(hand)))
    if 5-jokers in amounts:
        score = 7*100**len(hand) + highCard
    elif 4-jokers in amounts:
        score = 6*100**len(hand) + highCard
    elif (3 in amounts and 2 in amounts) or (jokers == 1 and amounts.count(2) == 2):
        score = 5*100**len(hand) + highCard
    elif 3-jokers in amounts:
        score = 4*100**len(hand) + highCard
    elif (amounts.count(2) == 2) or (jokers == 1 and 2 in amounts):
        score = 3*100**len(hand) + highCard
    elif 2-jokers in amounts:
        score = 2*100**len(hand) + highCard
    else:
        score = 1*100**len(hand) + highCard
    hands[i][2] = score

sorted_hands = sorted(hands, key=lambda el: el[2])
winnings = 0
for i in range(len(sorted_hands)):
    winnings += sorted_hands[i][1] * (i+1)

print(winnings)