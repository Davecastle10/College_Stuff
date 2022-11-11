

marks = [[0.90, 0.82, 0.79, 0.81],
        [0.90, 0.91, 0.90, 0.92],
        [0.37, 0.41, 0.57, 0.68],
        [0.21, 0.98, 0.15, 0.83]]

#e.g. print(marks[1][3])
#outputs 0.92

#average(mean) of test 1 marks

def mean_marks(test_number, marks):
    total = 0
    average = 0
    for i in range(len(marks)):
        total = total + marks[i][test_number]
    count = len(marks)
    average = total/count
    return average
print(mean_marks(0,marks))