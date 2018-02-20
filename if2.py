str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
if str1 == str2:
	print(1)
if len(str1) > len(str2):
	print(2)
if str1 == 'learn' and str1 != str2:
	print(3)