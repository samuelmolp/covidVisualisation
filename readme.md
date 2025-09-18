# COVID VISUALISATION TOOL

This is a covid data visualisation tool. It provides an interactive and intuitive interface that can be used to show the evolution of covid around the world. 
The web application can be found here: *This url is no longer available, please reference "installation guide" at the end of the readme.* 
The videos and images from the start of 2020 to 2022 can be found in this repository without need to use the web app. 

## OVERVIEW
In this web application users can view data in several ways:
* Videos of the evolution of covid in a continent (not all continents are supported). You can view the cases, cases by 100.000 people and average cases by 100.000 people in last 5 days
* Charts: charts are made automatically based on the requested parameters to compare between regions and days
* Maps: you can search for all images created. Each image is from a single day. Here can be found an example:

![Example](/images/images/world/5days_relative_cases/2021-08-31.png)




## DATA
Covid cases were obtained using this API: https://covid19tracking.narrativa.com/
Population was obtained with this API: https://pypi.org/project/countryinfo/
Maps from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
Special thanks to: https://www.relataly.com/visualize-covid-19-data-on-a-geographic-heat-maps/291/

## FILES OVERVIEW
* Main.py: based on the JSON file created with getdata.py, it creates maps, videos and images.      
* Getdata.py: it obtains the data from the API stated above (la narrativa) and outputs the formatted data into a GENERAL.JSON file
* Utils.py: it matches iso3 and iso3 codes with population data


* Web application: an interactive and intuitive platform was developed using django.

## Installation guide
The url is no longer active. Therefore, in order to see results follow the following steps:
1. Download the code and install requirements with pip install -r requirement.txt
2. Copy /images and /video directories into /webapplication/covid/visualitation/static or create them by running getdata.py and main.py so that they are up to the current day 
3. Run the application
If you just want to see the videos or images, you can download /videos and/or /images

