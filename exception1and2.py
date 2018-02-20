def ask_user():
	answer = ''
	while answer != 'Хорошо':
		try:
			answer = input('Как дела? ')
		except (TypeError, KeyboardInterrupt): #я понимаю, что typeerror никогда не даст о себе знать, но программа
											   #настолько гладкая, что я даже не знаю какие еще исключения тут могут понадобиться
			print('\nПока')
			break



ask_user()