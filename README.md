# Retina

Retina is a Application that aims to count an object in a certain time.

## Presentation

[![Watch the video](https://img.youtube.com/vi/cSmKRrP16xs/maxresdefault.jpg)](https://www.youtube.com/watch?v=cSmKRrP16xs)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

A step by step series of examples that tell you how to get a development env running
1. Download all the file in Retina Repo
2. Make sure you have an internet connection
3. and just run the install.sh

## Running the tests

access the webcam
1. python retina.py

access specific video file
1. python retina.py --input $VIDEOPATH

get the output video file
1. python retina.py --input $VIDEOPATH --output $VIDEOOUTPUTFOLDER

## After the test

after the test you will get a data.csv file
the data.csv file contain
1. timestamp
2. total object
3. weather data like(temperature,humidity,)

## Built With

* [OpenCV](https://opencv.org/) - Used to get Computer Vision library
* [Openweather](https://openweathermap.org/) - Used to get Weather data
* [NumPy](https://numpy.org/) - Used to generate N-dimensional array
* [JSON](https://www.json.org/) - Used to save data from API
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

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
