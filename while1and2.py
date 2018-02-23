def find_person(name):
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    num = 0
    while names[num] != name:
        num += 1
    print(names.pop(num), 'нашелся')

find_person("Валера")