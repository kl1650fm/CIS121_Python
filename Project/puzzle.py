import random
# Create a puzzleLlist
# Numbers into List i=horizontal j=vertical
iNum = 4
jNum = 4
puzzleList = []
# [[1, 5, 9, 13]],[2,6,10,14],..]
for i in range(iNum):
    tempList = []
    for j in range(jNum):
        # i = 0, j = 0, result = 1
        # i = 0, j = 1, result = 5
        result = j*jNum+i+1
        tempList.append(result)
    puzzleList.append(tempList)
# ex) print(puzzleList[2][1]=7)
# ex) print(puzzleList)[-1][-1] = 0 removing last number
puzzleList[-1][-1] = 0

# Randomize the numbers
numbers = []
for row in puzzleList:
    numbers.extend(row)

random.shuffle(numbers)

index = 0
for i in range(iNum):
    for j in range(jNum):
        puzzleList[i][j] = numbers[index]
        index += 1

# Show a PuzzleList
def puzzleShow():
    textTemp = ""
    for j in range(jNum):
        for i in range(iNum):
            textTemp += str(puzzleList[i][j]) + "\t"
        textTemp += "\n"
    print(textTemp)

# Find a Blank and change its location
def find_blank(puzzleList):
    for i in range(iNum):
        for j in range(jNum):
            if puzzleList[i][j] == 0:
                return (i,j)
    return None

direction = {
    "left":(-1,0), "right":(1,0),
    "up":(0,-1), "down":(0,1)
}

# Change the direction[] ex) left, right, up, down
ii, jj = direction["right"]
iNew = i+ii
jNew = j+jj
# Ignore moves when they go out of bounds
if iNew>=0 and iNew<iNum and jNew >= 0 and jNew<jNum:
    puzzleList[i][j], puzzleList[iNew][jNew] = puzzleList[iNew][jNew], puzzleList[i][j]
    
puzzleShow()


# pygame 
# in progress..