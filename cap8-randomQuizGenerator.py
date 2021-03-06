#!/usr/bin/python3
import random,os

capitalState = {'Alabama':'Montgomery',
'Alaska':'Juneau',
'Arizona':'Phoenix',
'Arkansas':'Little Rock',
'California':'Sacramento',
'Colorado':'Denver',
'Connecticut':'Hartford',
'Delaware':'Dover',
'Florida':'Tallahassee',
'Georgia':'Atlanta',
'Hawaii':'Honolulu',
'Idaho':'Boise',
'Illinois':'Springfield',
'Indiana':'Indianapolis',
'Iowa':'Des Moines',
'Kansas':'Topeka',
'Kentucky':'Frankfort',
'Louisiana ':'Baton Rouge',
'Maine':'Augusta',
'Maryland':'Annapolis',
'Massachusetts':'Boston',
'Michigan':'Lansing',
'Minnesota':'Saint Paul',
'Mississippi':'Jackson',
'Missouri':'Jefferson City',
'Montana':'Helena',
'Nebraska':'Lincoln',
'Nevada':'Carson City',
'New Hampshire':'Concord',
'New Jersey':'Trenton',
'New Mexico':'Santa Fe',
'New York':'Albany',
'North Carolina':'Raleigh',
'North Dakota':'Bismarck',
'Ohio':'Columbus',
'Oklahoma':'Oklahoma City',
'Oregon':'Salem',
'Pennsylvania':'Harrisburg',
'Rhode Island':'Providence',
'South Carolina':'Columbia',
'South Dakota':'Pierre',
'Tennessee':'Nashville',
'Texas':'Austin',
'Utah':'Salt Lake City',
'Vermont':'Montpelier',
'Virginia':'Richmond',
'Washington':'Olympia',
'West Virginia':'Charleston',
'Wisconsin':'Madison',
'Wyoming':'Cheyenne'}
#At least... i learned a lot... geographically speaking

for quizNum in range(35):
    #Create a folder named 'pagesCap8'... too many files...
    if os.path.exists('./pagesCap8') == False:
        os.makedirs('./pagesCap8')
    quizFile = open('pagesCap8/capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('pagesCap8/capitalsquiz_answers%s.txt' % (quizNum + 1),
                        'w')

    quizFile.write('Name:\nDate:\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitalState.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswer = capitalState[states[questionNum]]
        wrongAnswer = list(capitalState.values())
        #Making the wrongAnswer... wrong. lol
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
                        states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1,
                            'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
