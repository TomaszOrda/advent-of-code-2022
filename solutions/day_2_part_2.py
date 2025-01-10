VALUE = {
    "A": 1,
    "B": 2,
    "C": 3,
}

OUTCOME_OF_THE_ROUND_VALUE = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def player_choice_value(opponent, outcome):
    shift = OUTCOME_OF_THE_ROUND_VALUE[outcome]//3 - 1
    player = VALUE[opponent] + shift
    if player == 4:
        return 1
    if player == 0:
        return 3
    else:
        return player


def total_score_of_the_round(opponent, outcome):
    return OUTCOME_OF_THE_ROUND_VALUE[outcome] + player_choice_value(opponent, outcome)


def solution(raw_input: str):
    rounds = raw_input.splitlines()
    return sum(total_score_of_the_round(*round.split(" ")) for round in rounds)
