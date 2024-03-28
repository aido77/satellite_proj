from learningattributefill import *
from random import *

reference_dict = {1:'Acceleration', 2:'Angular Velocity (ω)', 3:'Force', 4:'value of g', 5:'Mass', 6:'Radius of Orbit', 7:'Speed'}
unit_dict = {1:'ms^-2', 2:'rad s^-1', 3:'Newtons', 4:'ms^-2', 5:'kg', 6:'m', 7:'ms^-1'}

question_list = [[],[]]
def question_generate():
    learning_attribute_fill()
    for i in range(5):
        x = randint(0,len(learning_database)-1)
        temp_sat =  learning_database[x]
        y = randint(1,7)
        solution = str(temp_sat[y])
        if y == 1:
            z = randint(0,1)
            if z == 0:
                val1 = 7
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 1:
                val1 = 2
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
        elif y == 2:
            z = randint(0,2)
            if z == 0:
                val1 = 7
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 1:
                val1 = 1
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 2:
                val1 = 3
                val2 = 5
                val3 = 6
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
        elif y == 3:
            z = randint(0,3)
            if z == 0:
                val1 = 5
                val2 = 7
                val3 = 6
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
            elif z == 1:
                val1 = 5
                val2 = 2
                val3 = 6
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
            elif z == 2:
                val1 = 4
                val2 = 5
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 3:
                val1 = 5
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
        elif y == 4:
            z = randint(0,1)
            if z == 0:
                val1 = 3
                val2 = 5
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 1:
                val1 = 6
                val2 = ''
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = ''
                givenVal3 = ''
        elif y == 5:
            z = randint(0,3)
            if z == 0:
                val1 = 3
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 1:
                val1 = 3
                val2 = 4
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 2:
                val1 = 3
                val2 = 6
                val3 = 7
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
            elif z == 3:
                val1 = 3
                val2 = 6
                val3 = 2
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
        elif y == 6:
            z = randint(0,5)
            if z == 0:
                val1 = 4
                val2 = ''
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = ''
                givenVal3 = ''
            elif z == 1:
                val1 = 3
                val2 = 5
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 2:
                val1 = 3
                val2 = 2
                val3 = 5
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
            elif z == 3:
                val1 = 3
                val2 = 5
                val3 = 7
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
            elif z == 4:
                val1 = 1
                val2 = 2
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 5:
                val1 = 1
                val2 = 7
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
        elif y == 7:
            z = randint(0,2)
            if z == 0:
                val1 = 2
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 1:
                val1 = 1
                val2 = 6
                val3 = ''
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = ''
            elif z == 2:
                val1 = 3
                val2 = 6
                val3 = 5
                givenVal1 = str(temp_sat[val1])
                givenVal2 = str(temp_sat[val2])
                givenVal3 = str(temp_sat[val3])
        question_list.insert(i,[temp_sat[0],solution,y,val1,givenVal1,val2,givenVal2,val3,givenVal3])
    question_list.pop()
    question_list.pop()

question_part = [[],[]]
question_full = [[],[]]
def question_formulate():
    question_generate()
    for i in range(5):
        temp_question = question_list[i]
        if temp_question[7] != '':
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                    " of ", temp_question[4], unit_dict[temp_question[3]], ", ", reference_dict[temp_question[5]], " of ", temp_question[6], unit_dict[temp_question[5]], " and ", 
                                    reference_dict[temp_question[7]], " of ", temp_question[8], unit_dict[temp_question[7]], ". Find ", reference_dict[temp_question[2]]," of the satellite"])
        elif temp_question[7] == '' and temp_question[5] != '':
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                        " of ", temp_question[4], unit_dict[temp_question[3]], " and ", reference_dict[temp_question[5]], " of ", temp_question[6], unit_dict[temp_question[5]],
                                             ". Find the ", reference_dict[temp_question[2]], " of the satellite"])
        else:
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                        " of ", temp_question[4], unit_dict[temp_question[3]], ". Find ", reference_dict[temp_question[2]], " of the satellite"])
    question_part.pop()
    question_part.pop()
    for i in range(5):
        temp_q = question_part[i]
        temp_str = ''.join(temp_q)
        question_full.insert(i,temp_str)
        next
    question_full.pop()
    question_full.pop()
