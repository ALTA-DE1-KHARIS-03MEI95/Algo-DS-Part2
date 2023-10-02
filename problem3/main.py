def playing_domino (cards, deck):
    max_count = 0
    suggest_card = []

    for i in cards:
        if deck [0] in i or deck[1] in i:
            if sum(i) > max_count:
                max_count = sum(i)
                suggest_card = i
    return suggest_card

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []