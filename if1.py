age = input('Сколько вам лет?	')
age = int(age)
if age < 7:
	print('Детский сад')
elif age < 18:
	print('Школа')
elif age < 23:
	print('ВУЗ')
else:
	print('Работа')