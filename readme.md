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

* Getdata.py: this file obtains the data from the API stated above (la narrativa) and outputs the data into a GENERAL.JSON file. In that json, each key is a date that has associated another dictionary of country:cases (that day). Specific json files for each day are also created and can be found at /JSONS. This was done to prevent needing API calls when using the API as the result is too slow. 
* Utils.py: this file obtains some arrays necessary in main.py. It obtains all iso2 and iso3 codes and creates a dict matching them to the population. 
* Main.py: it has several parts:
    * dataInDay class: map to create the map of a given region on a given day of a given type. Regions, types and days specifications can be found in the code. It uses geopandas to plot the data and saves the map. To retrieve covid cases it uses general.json. It contains the functions to obtain relative cases, average 5 days cases...
    * Video class: it creates a video that is a sequence of all the images of a given region and type
    * Runsimutaion: creates all images of all possible days with a given region and type


* Web application:
    * Views.py: renders the necessary templates and has an API route that returns a json with keys being the days from the specified range and values being dict of country of the region and covid cases (or other specified parameters). This data is then used to create the charts. 
    * Javascript files for all urls that render the images, videos or charts with the specified parameters. Videos and images are taken from /static. Charts are created with chart.js and it calls the API route in views.py
    * Templates for all urls (index, videos, images, charts and aboutData) and a layout
    * Css for all urls

## Installation guide

The url is no longer active. Therefore, in order to see results follow the following steps:
1. Download the code and install requirements with pip install -r requirement.txt
2. Copy the /images and /video directories into /webapplication/covid/visualitation/static
3. Run the application with python manage.py runserver

If you just want to see the videos or images, you can download /videos and/or /images
