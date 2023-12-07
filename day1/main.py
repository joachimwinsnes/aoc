

f = open("input.txt", "r")

stringnumberlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
numberlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

calV = 0
count = 1
while True:
    print("line: " + str(count))
    count += 1

    line = f.readline()
    if line == "":
        break
    else: 
        firstnum = ""
        lastnum = ""
        lineLen = len(line)
        valuesinList = []
        newline = ""
        px1 = 0
        px2 = 1
        while firstnum == "":
            if line[px1:px2] in stringnumberlist or line[px1:px2] in numberlist:
                firstnum = line[px1:px2]
                print("first found")
            else:
                print(line[px1:px2])
                if len(line[px1:px2]) > 5 or px2 > len(line):    
                    px1 += 1
                    px2 = px1 + 1
                else:
                    px2 += 1
        
        px1 = lineLen
        px2 = px1 - 1
        while lastnum == "":
            if line[px2:px1] in stringnumberlist or line[px2:px1] in numberlist:
                lastnum = line[px2:px1]
                print("last found")
            else:
                if len(line[px2:px1]) > 5 or px2 < 0:    
                    px1 -= 1
                    px2 = px1 - 1
                else:
                    px2 -= 1
        
        
        if (firstnum.isdigit()):
            newline = str(firstnum)
        else:
            for i in range(len(stringnumberlist)):
                if(stringnumberlist[i] in firstnum):
                    newline = numberlist[i]
        
        if (lastnum.isdigit()):
            newline = newline +  str(lastnum)
        else:
            for i in range(len(stringnumberlist)):
                if(stringnumberlist[i] in lastnum):
                    newline =  newline + str(numberlist[i])
        print(newline)

        calV += int(newline)
        print("total: " + str(calV))
