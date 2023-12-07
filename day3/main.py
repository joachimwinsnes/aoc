
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

def hasSymNeighbor(l, p, pt):
    itDoes = 0
    print("-----------------")
    print(arr[l][p:pt])
    #print("l: " + str(l) + " p: " + str(p) + " pt: " + str(pt))

    # left
    if p > 0:
        if arr[l][p - 1].strip() != "" and not arr[l][p - 1].strip().isnumeric():
            print("found left " + str(arr[l][p - 1].strip()))
            itDoes += 1

    # right
    if pt < len(arr[line]):
        if arr[l][pt].strip() != "" and not arr[l][pt].strip().isnumeric():
            print("found right "+ str(arr[l][pt].strip()))
            itDoes += 1
    # over
    if l > 0:
        if not p > 0:
            mp = p
        else: mp = p - 1
        if not pt < len(arr[line]):
            mpt = pt
        else:
            mpt = pt + 1
        if arr[l - 1][mp:mpt].strip() != "" and not arr[l - 1][mp:mpt].strip().isnumeric():
            print("found over "+ str(arr[l - 1][mp:mpt].strip()))
            itDoes += 1
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
        if arr[l + 1][mp:mpt].strip() != "" and not arr[l + 1][mp:mpt].strip().isnumeric():
            print("found under "+ str(arr[l + 1][mp:mpt].strip()))
            itDoes += 1


    print("amount: " + str(itDoes))
    return itDoes


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
                amount = hasSymNeighbor(line, place, place + px - 1)
                if amount > 0:
                    score += amount * int(arr[line][place:place + px - 1])
                
                skip = px - 1



            
#print(arr)
print("Total: " + str(score))
#print(len(arr))