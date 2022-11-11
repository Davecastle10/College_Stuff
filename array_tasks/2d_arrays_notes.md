#2d Arrays

##Scenario:
we have a group of students.
each have four test marks

students / test1 / test2 / test3 / test4
Abbie    / 0.9   / 0.82  / 0.79  / 0.81
Bob      / 0.9   / 0.91  / 0.90  / 0.92
Cat      / 0.32  / 0.41  / 0.57  / 0.68
Dave     / 0.21  / 0.98  / 0.15  / 0.83

this could be represented as 
marks = [[0.90, 0.82, 0.79, 0.81]'
        [0.90, 0.91, 0.90, 0.92]'
        [0.32, 0.41, 0.57, 0.68]'
        [0.21, 0.98, 0.15, 0.83]]

e.g. print(marks[1][3])
outputs 0.92

average(mean) of test 1 marks

def mean_marks(marks):
    total = 0
    average = 0
    for i in range(len(marks)):
        total = total + marks[i][0]
    count = len(marks)
    average = total/count
    return average




