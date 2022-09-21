from functional_casino import stavca

balance = 1000
while True:
    command = input('Введите команду:')
    if command == 'exit':
        print('Игра закончина!')
        break
    elif balance == 0:
        print('Вы обанкротились')
        break
    else:
        amount = int(input('Введите сумму'))
        if amount > balance or amount <= 0:
            print('Вы вели не правиьную сумму или вам не хвотает денег!')
            continue
        lot = int(input('Введите лот'))
        if lot > 30 or lot <= 0:
            print('Вы вели не правильную лот')
        win_amount = stavca(amount, lot)
        balance += win_amount
