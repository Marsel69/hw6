import random


def stavca(amount, lot):
    win_lot = random.randint(1, 30)
    if win_lot == lot:
        print('Вы выиграли')
        return amount * 2
    else:
        print('Вы проиграли')
        return -amount