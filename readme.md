# COVID VISUALISATION TOOL

This is a covid data visualisation tool. It provides an interactive interface that can be used to show the evolution of covid from 2020 to 2022. 
The web application can be found in this here: *This url is no longer available, please reference "installation guide" at the end of the readme.* The videos and images that were created can me found in this repository without need to use the webapp. 

## OVERVIEW
In this web application users can view data in several ways:
* Videos of the evolution of covid in a specific continent (not all continents are supported) from the start of 2020 till march of 2022. You can view the cases, cases by 100.000 people and average cases by 100.000 people in last 5 days
* Maps: you can search for all images shown on the videos
* Charts: charts are made automatically based on the requested parameters. You can view the information of the videos in a intuitive such as on a bar chart

## DATA
Covid cases were obtained using this API: https://covid19tracking.narrativa.com/
Population was obtained with this API: https://pypi.org/project/countryinfo/
Maps from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
Special thanks to: https://www.relataly.com/visualize-covid-19-data-on-a-geographic-heat-maps/291/

## FILES OVERVIEW
All static images and videos can be found at /videos and /images.

* Main.py: based on the JSON file created with getdata.py, it creates maps, videos and images.
    * dataInDay class: to create the map of a given region on a given day and a given type. It uses geopandas to plot the data and saves the map. It has functions to obtain the key relevannt information including relative cases, average 5 days cases and more
    * Video class: it creates a video that is a sequence of all the images of a given region and type
    * Runsimutaion: creates all images of all possible days with a given region and type
      
* Getdata.py: it obtains the data from the API stated above (la narrativa) and outputs the formatted data into a GENERAL.JSON file
* Utils.py: it matches iso3 and iso3 codes with population data


* Web application: to create an interactive and intuitive platform. It was created using django.

## Installation guide
The url is no longer active. Therefore, in order to see results follow the following steps:
1. Download the code and install requirements with pip install -r requirement.txt
2. Copy the /images and /video directories into /webapplication/covid/visualitation/static
3. Run the application with python manage.py runserver

If you just want to see the videos or images, you can download /videos and/or /images
