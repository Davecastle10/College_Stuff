# this is my answer to question 7c on the monday 5th june 2017 AS computer scince OCR exam course ref code H046/01
# i think this code works but i can't exactly test it due to the nature of the question
# this could be more efficient but i made it at 10:30 pm and i don't reallly have time to improve it that much.

def updateDisplay(input_string):

    words = input_string.split()# assigns the sring to the varible words as a list
    row = 0# row variable
    col = 0# column variable

    while len(words) > 0:
        if row > 4:# if the loop has run and row > 4 shift all lines up 1 removing the top line from view
            display[0] = display[1]
            display[1] = display[2]
            display[2] = display[3]
            for i in range(20):
                display[4][i] = ""


#        for i in range(len(words)): # this line was needed but i don't think it is now due to other changes i made
        temp = words.remove()# assigns next word in queue to temp

        if col + len(temp) > 20:# adding word on to the line exceeds 2 character legth of line go to nect line/row
            row +=1

        for q in range(len(temp)):# adding word to current line/row
            display[row][q + col] = temp(q)
            col += 1
        if col + len(temp) < 20:# adds a space after the lst word if ther is still space on the row
            display[row][1 + col] = " "
            col +=1

        
            
