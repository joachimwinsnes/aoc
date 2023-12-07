f = open("input.txt", "r")

cards = []
scores = []
total = 0

inputLine = f.readline()
while inputLine != "":
    cards.append(inputLine.replace("\n", ""))
    inputLine = f.readline()

for card in cards:
    #print(card.split(":")[0])
    #print(card.split(":")[1].split("|")[0].strip())
    #print(card.split(":")[1].split("|")[1].strip())
    # check 2 spots at a time, turn in to int and check
    count = 0
    cardScore = 0
    winningNumbers = card.split(":")[1].split("|")[0]
    numbers = card.split(":")[1].split("|")[1].strip()
    print(numbers)
    if numbers[1] == " ":
        numbers = " " + numbers
    jump = 2
    i = 0
    
    while i + jump <= len(numbers) : 
        #print(int(numbers[i:i+jump]))
        if str(" " + str(int(numbers[i:i+jump])) + " ") in winningNumbers:
            print("found: " + str(str(int(numbers[i:i+jump])) + " "))
            if count < 1:
                cardScore = 1
            else:
                cardScore = cardScore * 2
            count += 1

        i += jump + 1

    print(str(card.split(":")[0]) + " score: " + str(cardScore))
    total += cardScore

print("Total: " + str(total))