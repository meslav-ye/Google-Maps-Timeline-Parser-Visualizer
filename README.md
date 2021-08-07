# Google-Maps-Timeline-Parser-Visualizer

## Parser.py
Python parser for your google data from google maps timeline.
It parse data based on date, distance and type of transport ({'UNKNOWN': 1, 'UNKNOWN_ACTIVITY_TYPE': 1, 'IN_TRAIN': 1, 'IN_TRAM': 1,
 'IN_SUBWAY': 1, 'IN_PASSENGER_VEHICLE': 1, 'WALKING': 1, 'CYCLING': 1, 'IN_BUS': 1, 'RUNNING': 1}).
Save data in csv files based on year and month. 

## Visualizer.py
Python visualizer visualize your data that was parsed with parser.py. 
It creates graphs for each type of transportation based (currently types UNKNOWN, IN_TRAIN, IN_PASSENGERVEHICLE, WALKING, CYCLING) on months and years. 

### How to use parser.py
1. After you download your data, export it, move parser.py inside "Semantic Location History" directory
2. run `python parser.py`
3. It will create directory "parsed"

### How to use visualizer.py
1. After parsed dir was created, move visualizer.py in parsed dir
2. run `python visualizer.py`
3. It will create figures in current directory

### How to Download your data from google

1. Go to https://takeout.google.com/

2. Select Location history only

![image](https://user-images.githubusercontent.com/72811656/128600945-ff205a17-adaf-488a-bb7a-0afd66512200.png)

3. Export and wait

4. You will receive mail on your gmail account when it is done


