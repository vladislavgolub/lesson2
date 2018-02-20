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
{'class' : '11', 'scores' : [3,4,5,5,5]}]

am_stud = 0

sum_scor_sch = 0

av_sch = 0

am_in_class = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

av_class = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sum_scor_class = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for klass in range (len(am_in_class)):
	am_in_class[klass] = len(report[klass]['scores'])

for klass in range(len(sum_scor_class)):
	for student in range(am_in_class[klass]):
		sum_scor_class[klass] += report[klass]['scores'][student]

for klass in range(len(sum_scor_class)):
	av_class[klass] = sum_scor_class[klass] / am_in_class[klass]
	am_stud += am_in_class[klass]
	sum_scor_sch += sum_scor_class[klass]

av_sch = sum_scor_sch / am_stud

print('Средний балл по школе: ', av_sch)
print('Средний балл по классам: ', av_class)
