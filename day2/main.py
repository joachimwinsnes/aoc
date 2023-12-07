
f = open("input.txt", "r")

class Bag:
    red = 12
    green = 13
    blue = 14

class Game:
    def __init__(self, id, gameSets):
        self.id = id
        self.gameSets = gameSets
        self.possible = True

idSum = 0
gameObjects = []
games = []
line = f.readline()
while line != "":
    games.append(str(line))
    line = f.readline()

for game in games:
    gameId = game.split(':')[0].split(' ')[1]
    gameSets = game.split(':')[1].split(';')
    gameObjects.append(Game(gameId, gameSets))
    

for i in range(len(gameObjects)):
    for set in gameObjects[i].gameSets:
        colors = set.split(',')
        
            
        for color in colors:
            if gameObjects[i].id == '88':
                print(color.split(' ')[2])
            if color.split(' ')[2].replace("\n","") == 'red':
                if int(color.split(' ')[1]) > Bag.red:
                    gameObjects[i].possible = False
                    break
            if gameObjects[i].id == '88':
                print("still here 1")
            if color.split(' ')[2].replace("\n","") == 'green':
                if int(color.split(' ')[1]) > Bag.green:
                    gameObjects[i].possible = False
                    break
            if gameObjects[i].id == '88':
                print("still here 2")
            if color.split(' ')[2].replace("\n","") == 'blue':
                if gameObjects[i].id == '88':
                    print("on blue")
                    print(colors)
                if int(color.split(' ')[1]) > Bag.blue:
                    gameObjects[i].possible = False
                    break
            
            

for gameObj in gameObjects:
    if gameObj.possible:
        idSum += int(gameObj.id)
        #print(gameObj.id)
    print("game " + gameObj.id + ": " + str(gameObj.possible))
    #print("sum: " + str(idSum))

print("total id sum: " + str(idSum))