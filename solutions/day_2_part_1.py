VALUE = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def player_wins(opponent, player):
    return VALUE[opponent] == VALUE[player]-1 or VALUE[opponent]==3 and VALUE[player]==1

def outcome_of_the_round(opponent, player):
    if VALUE[opponent] == VALUE[player]:
        return 3
    if player_wins(opponent, player):
        return 6
    else:
        return 0

def total_score_of_the_round(opponent, player):
    return VALUE[player] + outcome_of_the_round(opponent, player)


def solution(raw_input: str):
    rounds = raw_input.splitlines()
    return sum( [total_score_of_the_round(*round.split(" ")) for round in rounds ] )
