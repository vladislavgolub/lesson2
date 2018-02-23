report = [
    {'class' : '1', 'scores' : [2,3,5,3,1]},
    {'class' : '2', 'scores' : [5,4,2,3,2]},
    {'class' : '3', 'scores' : [5,4,3,5,2]},
    {'class' : '4', 'scores' : [2,5,4,3,1]},
    {'class' : '5', 'scores' : [1,4,3,5,2]},
    {'class' : '6', 'scores' : [1,2,4,5,5]},
    {'class' : '7', 'scores' : [2,4,5,4,5]},
    {'class' : '8', 'scores' : [4,2,3,4,5]},
    {'class' : '9', 'scores' : [4,3,3,4,5]},
    {'class' : '10', 'scores' : [2,4,3,1,1]},
    {'class' : '11', 'scores' : [3,4,5,5,5]}
]

av_class = {}

sum_scor_sch = 0

am_stud = 0

for klass in report:
    sum_scor_class = sum(klass['scores'])
    am_in_class = len(klass['scores'])
    sum_scor_sch += sum_scor_class
    am_stud += am_in_class
    av_class[klass['class']] = sum_scor_class / am_in_class

print('Средний балл по школе: ', sum_scor_sch / am_stud)
print('Средний балл по классам: ', av_class)
