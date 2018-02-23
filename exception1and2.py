def ask_user():
    answer = ''
    while answer != 'Хорошо':
        try:
            answer = input('Как дела? ')
        except (TypeError, KeyboardInterrupt): #я понимаю, что typeerror никогда не даст о себе знать, но программа
            print('\nПока')                    #настолько гладкая, что я даже не знаю какие еще исключения тут могут понадобиться
            break



ask_user()