basic_answers = {'привет':'Привет', 'как дела?':'Нормально', 'пока':'Пока'}

def get_answer(question, answers = basic_answers):
    question = question.lower()
    print(answers[question])
    return answers[question]


def ask_user():
    question = ''
    answer = ''
    while answer != 'Пока':
        question = input('Введите вопрос: ')
        answer = get_answer(question)


ask_user()