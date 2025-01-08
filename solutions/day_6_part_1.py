MARKER_LENGTH = 4

def first_duplicate_character_index(marker):
    for index_1, character_1 in enumerate(marker):
        for character_2 in marker[index_1+1:]:
            if character_1==character_2:
                return index_1
    return None


def solution(raw_input: str):
    data_stream = raw_input.strip()
    marker_index = 0
    while (shift := first_duplicate_character_index(data_stream[marker_index:marker_index+MARKER_LENGTH]) is not None):
        marker_index+=shift
    return marker_index + MARKER_LENGTH
