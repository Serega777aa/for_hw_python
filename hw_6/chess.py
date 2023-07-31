from random import randint

POS_COUNT = 8
SIZE = 8

def check_correct_pos(positions):
    for i in positions:
        for j in positions:
            if j == i:
                continue
            if j[0] == i[0] or j[1] == i[1] or abs(j[0] - i[0]) == abs(j[1] - i[1]):
                return False
    return True


def get_random_pos():
    pos = []
    while len(pos) != POS_COUNT:
        coord = (randint(1, SIZE), randint(1, SIZE))
        if coord not in pos:
            pos.append(coord)
    return pos







