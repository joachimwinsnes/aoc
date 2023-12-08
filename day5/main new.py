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

def getRangeVal(maps):
    ss = []
    se = []
    ds = []
    de = []
    for index, map in enumerate(maps):
        ss.append(int(map[1]))
        se.append(int(map[1]) + int(map[2]) - 1)
        ds.append(int(map[0]))
        de.append(int(map[0]) + int(map[2]) - 1)
    return ss, se, ds, de



def calculate(fromtypes, ss, se, ds, de):
    temp = []
    for fromtype in fromtypes:
        found = False
        for i in range(0, len(ss) ):
            if int(fromtype) in range(ss[i], se[i] + 1):
                print("Type is in list")
                temp.append(int(fromtype) + int(ds[i] - ss[i]))
                found = True
        if not found:
            temp.append(int(fromtype))
    #print(temp)
    return temp

print("soils")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(seedtosoilmap)
print("calculating")
soils = calculate(seeds, ss, se, ds, de)


print("fert")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(soiltofertilizermap)
print("calculating")
fertelizers = calculate(soils, ss, se, ds, de)



print("water")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(fertilizertowatermap)
print("calculating")
waters = calculate(fertelizers, ss, se, ds, de)


print("light")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(watertolightmap)
print("calculating")
lights = calculate(waters, ss, se, ds, de)

print("temp")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(lighttotemperaturemap)
print("calculating")
temperatures = calculate(lights, ss, se, ds, de)

print("humi")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(temperaturetohumiditymap)
print("calculating")
humidities = calculate(temperatures, ss, se, ds, de)

print("location")
sourcerange = []
destrange = []
ss, se, ds, de = [], [], [], []
ss, se, ds, de = getRangeVal(humiditytolocationmap)
print("calculating")
locations = calculate(humidities, ss, se, ds, de)




print("locations: " + str(locations))

lowest= 1000000000000000000000000000
for l in locations:
    if l < lowest:
        lowest = l
print("lowest location: " + str(lowest))