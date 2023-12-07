
f = open("input.txt", "r")

arr = []

inputLine = f.readline()
while inputLine != "":
    arr.append(inputLine.replace("\n", "").replace(".", " "))
    inputLine = f.readline()



score = 0
skip = 0
trailIdx = 0
symboleString = "!#¤%&/()=?@£${€}[]+*-_;,:"

#def findOtherNeighbor():
#    return:

#gears = [
#    [22, 0],  ### [gcord y, gcord, x, partnumber, amount of additions]
#]

gears = []                                                         
for i in range (0, 140):                               
    new = []                  
    for j in range (0, 140):    
        new.append([1, 0])       
    gears.append(new)


def hasSymNeighbor(l, p, pt, gears):
    itDoes = False
    print("-----------------")
    print(arr[l][p:pt])
    #print("l: " + str(l) + " p: " + str(p) + " pt: " + str(pt))

    # left
    if p > 0:
        if arr[l][p - 1].strip() == "*" :
            print("found left " + str(arr[l][p - 1].strip()))
            gears[l][p-1] = [int(gears[l][p-1][0]) * int(arr[l][p:pt]), gears[l][p-1][1] + 1]
            itDoes = True

    # right
    if pt < len(arr[line]):
        if arr[l][pt].strip() == "*":
            print("found right "+ str(arr[l][pt].strip()))
            gears[l][pt] = [int(gears[l][pt][0]) * int(arr[l][p:pt]), gears[l][pt][1] + 1]
            itDoes = True
    # over
    if l > 0:
        if not p > 0:
            mp = p
        else: mp = p - 1
        if not pt < len(arr[line]):
            mpt = pt
        else:
            mpt = pt + 1
        if arr[l - 1][mp:mpt].strip() == "*":
            print("found over "+ str(arr[l - 1][mp:mpt].strip()))
            for gp in range(mp, mpt):
                if arr[l-1][gp] == "*":
                    gears[l - 1][gp] = [int(gears[l - 1][gp][0]) * int(arr[l][p:pt]), gears[l - 1][gp][1] + 1]
            itDoes = True
    # under
    if  l < len(arr) - 1:
        if not p > 0:
            mp = p
        else:
            mp = p - 1
        if not pt < len(arr[line]):
            mpt = pt
        else:
            mpt = pt + 1
        if arr[l + 1][mp:mpt].strip() == "*":
            for gp in range(mp, mpt):
                if arr[l+1][gp] == "*":
                    print(str(l+1) + " " + str(gp))
                    gears[l + 1][gp] = [int(gears[l + 1][gp][0]) * int(arr[l][p:pt]), gears[l + 1][gp][1] + 1]
            print("found under "+ str(arr[l + 1][mp:mpt].strip()))
            itDoes = True


    print("amount: " + str(itDoes))
    return gears


for line in range(len(arr)):
    for place in range(len(arr[line])):
        px = 1
        if skip > 0:
            skip -= 1
        else:
            if arr[line][place:place + px].isnumeric():
                while arr[line][place:place + px].isnumeric():
                    if place + px > len(arr[line]):
                        #print("longer")
                        break
                    else:
                        px += 1
                #print(arr[line][place:place + px - 1])
                gears = hasSymNeighbor(line, place, place + px - 1, gears)
                    #score += int(arr[line][place:place + px - 1])
                
                skip = px - 1



            
#print(gears)
for line in gears:
    for entry in line:
        print(entry)
        if entry[1] > 1:
            score += entry[0]
#print(arr)
print("Total: " + str(score))
#print(len(arr))