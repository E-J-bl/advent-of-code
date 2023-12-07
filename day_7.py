data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

def cleanup(data):
    data = data.split("\n")

    for hand in data:
        temp = hand
        hand = hand.split(" ")
        data[data.index(temp)] = hand
    return data


def rank(hand):
    ranks = {"Five of a kind": 6, "Four of a kind": 5, "Full house": 4, 'Three of a kind': 3, 'Two pair': 2,
             'One pair': 1, "High card": 0}
    cards = "A K Q J T 9 8 7 6 5 4 3 2".split(" ")
    bet = hand.pop(1)
    hand = list(str(hand)[2:-2])
    handcomp = {}
    for card in hand:
        if card not in handcomp:
            handcomp[card] = 1
        else:
            handcomp[card] += 1
    value = 0
    for item in handcomp.values():
        if item == 2:
            value += 1
        if item == 3:
            value += 3
        if item == 4:
            value += 5
        if item == 5:
            value += 6
    return value


# some old code i stole from myself
def complexsetsort(data, sorterValue):
    unsorted = True
    sortcheck = 0
    while unsorted:
        sortcount = 0
        for i in range(len(data) - 1):
            if int(data[i][sorterValue]) < int(data[i + 1][sorterValue]):
                data[i], data[i + 1] = data[i + 1], data[i]
                sortcount += 1
        if sortcount == 0:
            sortcheck += 1
            if sortcheck == 3:
                unsorted = False
    return data


def set_sorter(data):
    hands = []
    cards = "A K Q J T 9 8 7 6 5 4 3 2".split(" ")
    for i in cleanup(data):
        hands.append([{i[0]: i[1]}, rank(i)])
    unsorted=True
    sortcount=0
    sortcheck=0
    hands = complexsetsort(hands, 1)
    while unsorted:
        for i in range(len(hands) - 1):

            if int(hands[i][1]) == int(hands[i + 1][1]):
                list(str(list(hands[i][0].keys())[0]))
                for let in range(len(list(list(str(list(hands[i][0].keys())[0]))))):
                    #print(list(list(str(list(hands[i][0].keys())[0]))),list(list(str(list(hands[i+1][0].keys())[0]))),cards.index((list(str(list(hands[i][0].keys())[0]))[let])),"num org:",(list(str(list(hands[i][0].keys())[0]))[let]), cards.index((list(str(list(hands[i + 1][0].keys())[0]))[let])),"num:",(list(str(list(hands[i + 1][0].keys())[0]))[let]))
                    if cards.index((list(str(list(hands[i][0].keys())[0]))[let])) > cards.index((list(str(list(hands[i+1][0].keys())[0]))[let])):
                        hands[i], hands[i + 1] = hands[i + 1], hands[i]
                        sortcount+=1
                        break
                    if cards.index((list(str(list(hands[i][0].keys())[0]))[let])) < cards.index((list(str(list(hands[i+1][0].keys())[0]))[let])):
                        break
        if sortcount == 0:
            sortcheck += 1
            if sortcheck == 3:
                unsorted = False
        sortcount=0
    return hands

def scorer(sorted_data):
    score=0
    data=sorted_data
    for hand in data:
        temp=hand[0]
        #print(temp,int(temp[str(list(temp.keys()))[2:-2]])*(len(data)-data.index(hand)),len(data)-data.index(hand),score)
        score+=int(temp[str(list(temp.keys()))[2:-2]])*(len(data)-data.index(hand))
    return score

def partB(data):

    hands = []
    cards = "A K Q T 9 8 7 6 5 4 3 2 J".split(" ")
    for i in cleanup(data):

        hands.append([{i[0]: i[1]}, rankb(i)])

    unsorted = True
    sortcount = 0
    sortcheck = 0
    hands = complexsetsort(hands, 1)
    while unsorted:
        for i in range(len(hands) - 1):

            if int(hands[i][1]) == int(hands[i + 1][1]):
                #print(list(str(list(hands[i][0].keys())[0])))
                for let in range(len(list(list(str(list(hands[i][0].keys())[0]))))):
                   # print(list(list(str(list(hands[i][0].keys())[0]))),
                          #list(list(str(list(hands[i + 1][0].keys())[0]))),
                          #cards.index((list(str(list(hands[i][0].keys())[0]))[let])), "num org:",
                          #(list(str(list(hands[i][0].keys())[0]))[let]),
                          #cards.index((list(str(list(hands[i + 1][0].keys())[0]))[let])), "num:",
                          #(list(str(list(hands[i + 1][0].keys())[0]))[let]))
                    if cards.index((list(str(list(hands[i][0].keys())[0]))[let])) > cards.index(
                            (list(str(list(hands[i + 1][0].keys())[0]))[let])) and hands[i][0]:
                        hands[i], hands[i + 1] = hands[i + 1], hands[i]
                        sortcount += 1
                        break
                    if cards.index((list(str(list(hands[i][0].keys())[0]))[let])) < cards.index(
                            (list(str(list(hands[i + 1][0].keys())[0]))[let])):
                        break
        if sortcount == 0:
            sortcheck += 1
            if sortcheck == 5:
                unsorted = False
        sortcount = 0
    return hands

def rankb(hand):

    ranks = {"Five of a kind": 6, "Four of a kind": 5, "Full house": 4, 'Three of a kind': 3, 'Two pair': 2,
             'One pair': 1, "High card": 0}
    cards = "A K Q T 9 8 7 6 5 4 3 2 J".split(" ")
    hand.pop(1)
    hand = list(str(hand)[2:-2])
    handcomp = {}
    for card in hand:
        if card not in handcomp:
            handcomp[card] = 1
        else:
            handcomp[card] += 1

    #print(handcomp)
    value = 0
    if "J" in handcomp.keys():
        temp=handcomp["J"]
        handcomp["J"] -= temp
        handcomp[max(handcomp, key=handcomp.get)]=handcomp[max(handcomp, key=handcomp.get)]+temp


        #print(handcomp)
    for item in handcomp.values():

        if item == 2:
            value += 1

        if item == 3:
            value += 3

        if item == 4:
            value += 5

        if item== 5:
            value += 6

    return value
print(set_sorter(data))
print(scorer(set_sorter(data)))
print(partB(data))
print(scorer(partB(data)))
