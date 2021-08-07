import matplotlib.pyplot as plt
import csv
import os

rootdir = os.getcwd()
x = []
y = []

#Cycling
CYCLING = "CYCLING"
distanceByMonthCycling = dict()
distanceByYearCycling = dict()

#Walking
WALKING = "WALKING"
distanceByMonthWalking = dict()
distanceByYearWalking = dict()

#Vehicle
IN_PASSENGER_VEHICLE = "IN_PASSENGER_VEHICLE"
distanceByMonthVehicle = dict()
distanceByYearVehicle = dict()

#Unknown
UNKNOWN1 = "UNKNOWN"
UNKNOWN2 = "UNKNOWN_ACTIVITY_TYPE"
distanceByYearUnknown = dict()
distanceByMonthUnknown = dict()

#Train
TRAIN = "IN_TRAIN"
distanceByYearTrain = dict()
distanceByMonthTrain = dict()

allSum = 0
def readFiles(file, name):
    year = name[:4]
    global allSum
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            month = row[0].split("-")[1]
            dayDistance = int(row[1])/1000
            allSum = allSum + dayDistance
            if(row[2]==CYCLING):

                if month in distanceByMonthCycling:
                    distanceByMonthCycling[month] = dayDistance + distanceByMonthCycling[month]
                else:
                    distanceByMonthCycling[month] = dayDistance

                if year in distanceByYearCycling:
                    distanceByYearCycling[year] = dayDistance + distanceByYearCycling[year]
                else:
                    distanceByYearCycling[year] = dayDistance
            elif(row[2]==WALKING):

                if month in distanceByMonthWalking:
                    distanceByMonthWalking[month] = dayDistance + distanceByMonthWalking[month]
                else:
                    distanceByMonthWalking[month] = dayDistance

                if year in distanceByYearWalking:
                    distanceByYearWalking[year] = dayDistance + distanceByYearWalking[year]
                else:
                    distanceByYearWalking[year] = dayDistance
            elif(row[2]==IN_PASSENGER_VEHICLE):

                if month in distanceByMonthVehicle:
                    distanceByMonthVehicle[month] = dayDistance + distanceByMonthVehicle[month]
                else:
                    distanceByMonthVehicle[month] = dayDistance

                if year in distanceByYearVehicle:
                    distanceByYearVehicle[year] = dayDistance + distanceByYearVehicle[year]
                else:
                    distanceByYearVehicle[year] = dayDistance
            elif(row[2]==UNKNOWN1 or row[2]==UNKNOWN2):

                if month in distanceByMonthUnknown:
                    distanceByMonthUnknown[month] = dayDistance + distanceByMonthUnknown[month]
                else:
                    distanceByMonthUnknown[month] = dayDistance

                if year in distanceByYearUnknown:
                    distanceByYearUnknown[year] = dayDistance + distanceByYearUnknown[year]
                else:
                    distanceByYearUnknown[year] = dayDistance
            elif(row[2]==TRAIN):

                if month in distanceByMonthTrain:
                    distanceByMonthTrain[month] = dayDistance + distanceByMonthTrain[month]
                else:
                    distanceByMonthTrain[month] = dayDistance

                if year in distanceByYearTrain:
                    distanceByYearTrain[year] = dayDistance + distanceByYearTrain[year]
                else:
                    distanceByYearTrain[year] = dayDistance

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
    plt.savefig(f"PIE_CHART.png")
    plt.show()
    plt.clf()
    plt.cla()

def plotDistanceGraph(distance, name, time):
    sum = getSumDistance(distance)
    x=[]
    y=[]
    distance = dict(sorted(distance.items()))
    for k, v in distance.items():
        x.append(k)
        y.append(v)

    if(time == "YEAR"):
        coloring = 'g'
    else:
        coloring = 'b'
    plt.bar(x, y, color = coloring, width = 0.70,label = f"{name} distance")
    plt.xlabel(f'{time}')
    plt.ylabel('Distance in km')
    plt.title('Distance sum = ' +str(round(sum,2))+' km', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.savefig(f"{name}_BY_{time}.png")
    plt.show()
    plt.clf()
    plt.cla()


files = [os.path.join(root, name)
         for root, dirs, files in os.walk(rootdir)
         for name in files
         if name.endswith(".csv")]
for file in files:
    name = os.path.basename(file)
    readFiles(file,name)

yearString = "YEAR"
monthString = "MONTH"
allTypes = dict()
allTypes[CYCLING] = distanceByYearCycling
allTypes[WALKING] = distanceByYearWalking
#allTypes[UNKNOWN1] = distanceByYearUnknown
allTypes[TRAIN] = distanceByYearTrain
allTypes[IN_PASSENGER_VEHICLE] = distanceByYearVehicle
drawPieChart(allTypes)
plotDistanceGraph(distanceByYearCycling, CYCLING, yearString)
plotDistanceGraph(distanceByYearWalking, WALKING, yearString)
plotDistanceGraph(distanceByYearUnknown, UNKNOWN1, yearString)
plotDistanceGraph(distanceByYearTrain, TRAIN, yearString)
plotDistanceGraph(distanceByYearVehicle, IN_PASSENGER_VEHICLE, yearString)
plotDistanceGraph(distanceByMonthTrain, TRAIN, monthString)
plotDistanceGraph(distanceByMonthUnknown, UNKNOWN1, monthString)
plotDistanceGraph(distanceByMonthVehicle, IN_PASSENGER_VEHICLE, monthString)
plotDistanceGraph(distanceByMonthWalking, WALKING, monthString)
plotDistanceGraph(distanceByMonthCycling, CYCLING,monthString)
print("All distance sum = "+str(allSum) + " km")
