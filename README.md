# Retina

Retina is a Application that aims to count an object in a real time.

## Presentation

[![Watch the video](https://github.com/angularya/Retina/blob/master/img/tn.png)](https://www.youtube.com/watch?v=cSmKRrP16xs)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

A step by step series of examples that tell you how to get a development env running
1. [Download](https://github.com/angularya/Retina/archive/master.zip) all the file in Retina Repo
2. Make sure you have an internet connection
3. and just run the install.sh

## Running the tests

access the webcam
1. python retina.py

access specific video file
1. python retina.py --input $VIDEOPATH

get the output video file
1. python retina.py --input $VIDEOPATH --output $VIDEOOUTPUTFOLDER
### Available Object to Detect
1. car
2. bus
3. bicycle
4. motorbike
5. person
6. boat
7. cat
8. dog
9. cow
10. sheep
11. bird
12. botle"
## After the test

after the test you will get a data.csv file
the data.csv file contain
1. timestamp.
2. total object.
3. weather data like(temperature, humidity, and etc).

![csv](https://github.com/angularya/Retina/blob/master/img/csv.png)

you can run plotit to show plot from your current data
just execute python <ins>plotit.py</ins>
    it will open your browser and show your current data
    
![plot](https://github.com/angularya/Retina/blob/master/img/plot.png)

## Built With

* [OpenCV](https://opencv.org/) - Used to get Computer Vision library
* [Openweather](https://openweathermap.org/) - Used to get Weather data
* [NumPy](https://numpy.org/) - Used to generate N-dimensional array
* [Pandas](https://pandas.pydata.org/) - Used to manipulate Dataframe to array
* [JSON](https://www.json.org/) - Used to save data from API
* [Plotly](https://plotly.com/) - Used to generate graph
* [SciPy](https://www.scipy.org/) - Used to get library for scientific computing
* [MobileNet SSD] - Pretrained Model
* [Python](https://www.python.org/) - Used for writng Application

## Authors

* **Anisa Amalia Zulva** 
* **Ayu Hartanti** 
* **Kharisma Dwi S** 
* **Muhammad Arya Wicaksana** 
* **Rindiani Sunardi** 
* **Rifaldi Gilang R** 

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/angularya/Retina/blob/master/LICENSE) file for details
