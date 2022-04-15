# COVID VISUALISATION TOOL

This is a covid visualisation tool. The end result can be found in this url: TODO

## OVERVIEW
In this web application users can view data in several ways:
* Videos of the evolution of covid in a specific continent (not all continents are supported) from the start of 2020 till march of 2022. You can view the cases, cases by 100.000 people and average cases by 100.000 people in last 5 days
* Maps: you can search for any of the images that was shown in the videos
* Charts: charts are made automatically based on the requested parameters. 

## DATA
Covid cases were obtained using this API: https://covid19tracking.narrativa.com/
Population was obtained with this API: https://pypi.org/project/countryinfo/
Maps from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
Special thanks to: https://www.relataly.com/visualize-covid-19-data-on-a-geographic-heat-maps/291/

## FILES OVERVIEW

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

