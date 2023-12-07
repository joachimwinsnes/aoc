f = open("input.txt", "r")

cards = []
scores = []
total = 0

inputLine = f.readline()
while inputLine != "":
    cards.append(inputLine.replace("\n", ""))
    inputLine = f.readline()
idx = 0
copyobjectCount = []
for card in cards:
    copyobjectCount.append([card, 1])


for card in cards:
    #print(card.split(":")[0])
    #print(card.split(":")[1].split("|")[0].strip())
    #print(card.split(":")[1].split("|")[1].strip())
    # check 2 spots at a time, turn in to int and check

    count = 0
    cardScore = 0
    winningNumbers = card.split(":")[1].split("|")[0]
    numbers = card.split(":")[1].split("|")[1].strip()
    #print(numbers)
    if numbers[1] == " ":
        numbers = " " + numbers
    jump = 2
    i = 0
    
    while i + jump <= len(numbers) : 
        #print(int(numbers[i:i+jump]))
        if str(" " + str(int(numbers[i:i+jump])) + " ") in winningNumbers:
            #print("found: " + str(str(int(numbers[i:i+jump])) + " "))
                
            count += 1

        i += jump + 1

    # put in copy in cards array with cardnumber + 1 unitl count = 0
    print(int(card.split(":")[0].split("d")[1]))
    cardnum = int(card.split(":")[0].split("d")[1])
    cardbuffer = cards[idx + 1:idx + 1 + count]
    #print(cardbuffer)


    for buffercard in cardbuffer:
        buffercardnum = int(buffercard.split(":")[0].split("d")[1])
        copyobjectCount[buffercardnum - 1][1] += 1 * copyobjectCount[cardnum - 1][1]
    #
    #k = 0
    #for buffercard in cardbuffer:
    #    #print("place " + str(idx + 1 + k) +  "  Card " + str(cardnum) + ":" + buffercard.split(":")[1])
    #    cards.insert(idx + 1 + k, buffercard)
    #    k += 1
    
    for c in copyobjectCount:
        print(c)

    
    #if idx == 1:
        #break
    print("idx: "+ str(idx))
    #print("ran " + card.split(":")[0].split(" ")[1])

    #print(str(card.split(":")[0]) + ": " + str(int(card.split(":")[0].split(" ")[1]) + 1) + "-" + str(int(card.split(":")[0].split(" ")[1]) + count))
    #total += cardScore

    idx += 1
for o in copyobjectCount:
    total += o[1]
print("Total cards: " + str(total))