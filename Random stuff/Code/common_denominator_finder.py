def calculate(num1, num2):
    temp = 0
    running = True
    while running == True:
        if num1 == num2:
            return num1
        elif num1 < num2:
            num2 = num2 - num1
        else:
            temp = num1
            num1 = num2
            num2 = temp - num2

print(calculate(4,16))