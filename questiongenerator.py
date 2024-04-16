from learningattributefill import *
from random import *

reference_dict = {1:'Acceleration', 2:'Angular Velocity (ω)', 3:'Force', 4:'value of g', 5:'Mass', 6:'Radius of Orbit', 7:'Speed'}
#is a dictionary that has numbers to corresponding attributes
unit_dict = {1:'ms^-2', 2:'rad s^-1', 3:'Newtons', 4:'ms^-2', 5:'kg', 6:'m', 7:'ms^-1'}
#is a dictionary that has numbers to corresponding units
question_list = [[],[]]
def question_generate():
    learning_attribute_fill()
    #calls the learning attribute fill function
    for i in range(5):
        x = randint(0,len(learning_database)-1)
        #picks a random satellite
        temp_sat =  learning_database[x]
        #lists the temmporary satellite
        y = randint(1,7)
        #chooses a random attribute from the satellite
        solution = str(temp_sat[y])
        #stores the solution as a variable
        if y == 1:
        #if the attribute is 'acceleration'
            z = randint(0,1)
            #chooses a random equation to use
            if z == 0: 
                #if the equation is the first one
                val1 = 7
                #speed
                val2 = 6
                #radius of orbit
                val3 = ''
                #value three doesn't need to be given
            elif z == 1:
                val1 = 2
                val2 = 6
                val3 = ''
        elif y == 2:
            z = randint(0,2)
            if z == 0:
                val1 = 7
                val2 = 6
                val3 = ''
            elif z == 1:
                val1 = 1
                val2 = 6
                val3 = ''
            elif z == 2:
                val1 = 3
                val2 = 5
                val3 = 6
        elif y == 3:
            z = randint(0,3)
            if z == 0:
                val1 = 5
                val2 = 7
                val3 = 6
            elif z == 1:
                val1 = 5
                val2 = 2
                val3 = 6
            elif z == 2:
                val1 = 4
                val2 = 5
                val3 = ''
            elif z == 3:
                val1 = 5
                val2 = 6
                val3 = ''
        elif y == 4:
            z = randint(0,1)
            if z == 0:
                val1 = 3
                val2 = 5
                val3 = ''
            elif z == 1:
                val1 = 6
                val2 = ''
                val3 = ''
        elif y == 5:
            z = randint(0,3)
            if z == 0:
                val1 = 3
                val2 = 6
                val3 = ''
            elif z == 1:
                val1 = 3
                val2 = 4
                val3 = ''
            elif z == 2:
                val1 = 3
                val2 = 6
                val3 = 7
            elif z == 3:
                val1 = 6
                val2 = ''
                val3 = ''
        elif y == 6:
            z = randint(0,5)
            if z == 0:
                val1 = 4
                val2 = ''
                val3 = ''
            elif z == 1:
                val1 = 3
                val2 = 5
                val3 = ''
            elif z == 2:
                val1 = 3
                val2 = 2
                val3 = 5
            elif z == 3:
                val1 = 3
                val2 = 5
                val3 = 7
            elif z == 4:
                val1 = 1
                val2 = 2
                val3 = ''
            elif z == 5:
                val1 = 1
                val2 = 7
                val3 = ''
        elif y == 7:
            z = randint(0,2)
            if z == 0:
                val1 = 2
                val2 = 6
                val3 = ''
            elif z == 1:
                val1 = 1
                val2 = 6
                val3 = ''
            elif z == 2:
                val1 = 3
                val2 = 6
                val3 = 5
        if val3 != '':
            givenVal1 = str(temp_sat[val1])
            givenVal2 = str(temp_sat[val2])
            givenVal3 = str(temp_sat[val3])
        elif val2 != '':
            givenVal1 = str(temp_sat[val1])
            givenVal2 = str(temp_sat[val2])
            givenVal3 = ''
        else:
            givenVal1 = str(temp_sat[val1])
            givenVal2 = ''
            givenVal3 = ''

        question_list.insert(i,[temp_sat[0],solution,y,val1,givenVal1,val2,givenVal2,val3,givenVal3])
        #this inserts the full data into the database
    question_list.pop()
    question_list.pop()
    #removes the two initial variables used to generate the 2-Dimensional array

question_part = [[],[]]
question_full = []
def question_formulate():
    question_generate()
    #calls the questiongenerate() function, as coded above
    for i in range(5):
        temp_question = question_list[i]
        #creates a temporary variable which contains all the bare-bones question data
        if temp_question[7] != '':
        #if there are three givenVals
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                    " of ", temp_question[4], unit_dict[temp_question[3]], ", ", reference_dict[temp_question[5]], " of ", temp_question[6], unit_dict[temp_question[5]], " and ", 
                                    reference_dict[temp_question[7]], " of ", temp_question[8], unit_dict[temp_question[7]], ". Find ", reference_dict[temp_question[2]]," of the satellite"])
        elif temp_question[7] == '' and temp_question[5] != '':
            #if there are two givenVals
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                        " of ", temp_question[4], unit_dict[temp_question[3]], " and ", reference_dict[temp_question[5]], " of ", temp_question[6], unit_dict[temp_question[5]],
                                             ". Find the ", reference_dict[temp_question[2]], " of the satellite"])
        else:
        #if there's only one givenVal
            question_part.insert(i,["The Satellite ", temp_question[0], " has ", reference_dict[temp_question[3]], 
                                        " of ", temp_question[4], unit_dict[temp_question[3]], ". Find ", reference_dict[temp_question[2]], " of the satellite"])
    question_part.pop()
    question_part.pop()
    #removes the two inital variables
    for i in range(5):
        temp_q = question_part[i]
        #creates another temporary variable
        temp_str = ''.join(temp_q)
        #turns the list into a string and stores it in a temp variable
        question_full.append(temp_str)
        #adds this to the database
        next
    
