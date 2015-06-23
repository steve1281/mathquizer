
import random

quiz = []

for i in range(1,12):
    for j in range(1,12):
        quiz.append( {'question': str(i) + ' x ' + str(j), 'answer': i*j} )

random.shuffle(quiz)

