f = open("input.txt", "r")


seeds = f.readline().split(":")[1].strip().replace("\n", "").split(" ")

seedtosoilmap = []
soiltofertilizermap = []
fertilizertowatermap = []
watertolightmap = []
lighttotemperaturemap = []
temperaturetohumiditymap = []
humiditytolocationmap = []

line = f.readline().strip()
while line == "":
    line = f.readline().strip()

line = f.readline().strip()
while line != "":
    seedtosoilmap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

line = f.readline().strip()
line = f.readline().strip()
while line != "":
    soiltofertilizermap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()
    
line = f.readline().strip()
line = f.readline().strip()
while line != "":
    fertilizertowatermap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

line = f.readline().strip()
line = f.readline().strip()
while line != "":
    watertolightmap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

line = f.readline().strip()
line = f.readline().strip()
while line != "":
    lighttotemperaturemap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

line = f.readline().strip()
line = f.readline().strip()
while line != "":
    temperaturetohumiditymap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

line = f.readline().strip()
line = f.readline().strip()
while line != "":
    humiditytolocationmap.append(line.replace("\n", "").split(" "))
    line = f.readline().strip()

#print("seeds: " + str(seeds))
#print("seedtosoilmap: " + str(seedtosoilmap))
#print("soiltofertilizermap: " + str(soiltofertilizermap))
#print("fertilizertowatermap: " + str(fertilizertowatermap))
#print("watertolightmap: " + str(watertolightmap))
#print("lighttotemperaturemap: " + str(lighttotemperaturemap))
#print("temperaturetohumiditymap: " + str(temperaturetohumiditymap))
#print("humiditytolocationmap: " + str(humiditytolocationmap))

soils = []
fertelizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []

def createRanges(maps):
    srange = []
    drange = []
    for index, map in enumerate(maps):
        print("map: " + str(index + 1))
        srange = ([(i) for i in range(int(map[1]), int(map[1]) + int(map[2]))]) + srange
        drange = ([(i) for i in range(int(map[0]), int(map[0]) + int(map[2]))]) + drange
    return srange, drange

def calculate(fromtypes, srange, drange):
    temp = []
    for fromtype in fromtypes:
        if not int(fromtype) in srange:
            temp.append(int(fromtype))
        else:
            for index, source in enumerate(srange):
                if int(fromtype) == int(source):
                    temp.append(drange[index])
    return temp

print("soils")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(seedtosoilmap)
print("calculating")
soils = calculate(seeds, sourcerange, destrange)

print("fert")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(soiltofertilizermap)
print("calculating")
fertelizers = calculate(soils, sourcerange, destrange)

print("water")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(fertilizertowatermap)
print("calculating")
waters = calculate(fertelizers, sourcerange, destrange)

print("light")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(watertolightmap)
print("calculating")
lights = calculate(waters, sourcerange, destrange)

print("temp")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(lighttotemperaturemap)
print("calculating")
temperatures = calculate(lights, sourcerange, destrange)

print("humi")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(temperaturetohumiditymap)
print("calculating")
humidities = calculate(temperatures, sourcerange, destrange)

print("location")
sourcerange = []
destrange = []
sourcerange, destrange = createRanges(humiditytolocationmap)
print("calculating")
locations = calculate(humidities, sourcerange, destrange)




print("locations: " + str(locations))

lowest= 1000000000000000000000000000
for l in locations:
    if l < lowest:
        lowest = l
print("lowest location: " + str(lowest))