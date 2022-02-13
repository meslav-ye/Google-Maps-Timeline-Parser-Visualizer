import matplotlib.pyplot as plt
import csv
import os

rootdir = os.getcwd()

#Cycling
CYCLING = "CYCLING"
distanceCycling = dict()

#Walking
WALKING = "WALKING"
distanceWalking = dict()

#Vehicle
IN_PASSENGER_VEHICLE = "IN_PASSENGER_VEHICLE"
distanceVehicle = dict()

#Unknown
UNKNOWN1 = "UNKNOWN"
UNKNOWN2 = "UNKNOWN_ACTIVITY_TYPE"
distanceUnknown = dict()

#Train
TRAIN = "IN_TRAIN"
distanceTrain = dict()

#All
allSum = 0

def readFiles(file, name):
    global allSum
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            date = row[0]
            dayDistance = int(row[1])/1000
            allSum = allSum + dayDistance
            if(row[2]==CYCLING):
                if date in distanceCycling:
                    distanceCycling[date] = dayDistance + distanceCycling[date]
                else:
                    distanceCycling[date] = dayDistance
            elif(row[2]==WALKING):
                if date in distanceWalking:
                    distanceWalking[date] = dayDistance + distanceWalking[date]
                else:
                    distanceWalking[date] = dayDistance
            elif(row[2]==IN_PASSENGER_VEHICLE):
                if date in distanceVehicle:
                    distanceVehicle[date] = dayDistance + distanceVehicle[date]
                else:
                    distanceVehicle[date] = dayDistance
            elif(row[2]==UNKNOWN1 or row[2]==UNKNOWN2):
                if date in distanceUnknown:
                    distanceUnknown[date] = dayDistance + distanceUnknown[date]
                else:
                    distanceUnknown[date] = dayDistance
            elif(row[2]==TRAIN):
                if date in distanceTrain:
                    distanceTrain[date] = dayDistance + distanceTrain[date]
                else:
                    distanceTrain[date] = dayDistance

def getSumDistance(distance):
    sum = 0
    for k, v in distance.items():
        sum = sum+v
    return sum

def drawPieChart(allTypes):
    x = []
    y = []
    for k, v in allTypes.items():
        x.append(k)
        y.append(getSumDistance(v))
    plt.pie(y,labels = x,autopct = '%.2f%%')
    plt.title('Distance by type', fontsize = 20)
    figName = f"PIE_CHART.png"
    if os.path.exists(figName):
        os.remove(figName)
    plt.savefig(figName)
    plt.show()
    plt.clf()
    plt.cla()

def getPeriodDistance(distance, period):
    d = dict()
    for k, v in distance.items():
        if(period == "YEAR"):
            year = k.split("-")[0]
            if year in d:
                d[year] = v+d[year]
            else:
                d[year] = v
        elif(period == "MONTH"):
            month = k.split("-")[1]
            if month in d:
                d[month] = v+d[month]
            else:
                d[month] = v
    return d

def saveShowPlot(x,y,name,period, sum):
    if(period == "YEAR"):
        coloring = 'g'
    else:
        coloring = 'b'
    plt.bar(x, y, color = coloring, width = 0.70,label = f"{name} distance")
    plt.xlabel(f'{period}')
    plt.ylabel('Distance in km')
    plt.title('Distance sum = ' +str(round(sum,2))+' km', fontsize = 20)
    plt.grid()
    plt.legend()
    figName = f"{name}_BY_{period}.png"
    if os.path.exists(figName):
        os.remove(figName)
    plt.savefig(figName)
    plt.show()
    plt.clf()
    plt.cla()

def plotDistanceGraph(distance, name):
    periodMonth = "MONTH"
    periodYear = "YEAR"
    x = []
    y = []
    yearDict = dict(sorted(getPeriodDistance(distance, periodYear).items()))
    monthDict = dict(sorted(getPeriodDistance(distance, periodMonth).items()))
    sumYear = getSumDistance(yearDict)
    sumMonth = getSumDistance(monthDict)

    for k,v in yearDict.items():
        x.append(k)
        y.append(v)
    saveShowPlot(x,y,name,periodYear, sumYear)

    x = []
    y = []

    for k,v in monthDict.items():
        x.append(k)
        y.append(v)
    saveShowPlot(x,y,name, periodMonth, sumMonth)

files = [os.path.join(root, name)
         for root, dirs, files in os.walk(rootdir)
         for name in files
         if name.endswith(".csv")]
for file in files:
    name = os.path.basename(file)
    readFiles(file,name)

allTypes = dict()
allTypes[CYCLING] = distanceCycling
allTypes[WALKING] = distanceWalking
allTypes[UNKNOWN1] = distanceUnknown
allTypes[TRAIN] = distanceTrain
allTypes[IN_PASSENGER_VEHICLE] = distanceVehicle
drawPieChart(allTypes)
plotDistanceGraph(distanceCycling, CYCLING)
plotDistanceGraph(distanceVehicle, IN_PASSENGER_VEHICLE)
plotDistanceGraph(distanceTrain, TRAIN)
plotDistanceGraph(distanceUnknown, UNKNOWN1)
plotDistanceGraph(distanceWalking, WALKING)
print("All distance sum = "+str(allSum) + " km")
