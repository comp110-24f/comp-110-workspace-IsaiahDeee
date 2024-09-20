"""challenge question 3 - loops"""

__author__ = "730583303"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    track_index: int = 0

    while track_index < len(phrase):
        if phrase[track_index] == search_char:
            count = count + 1
        track_index = track_index + 1

    return count
