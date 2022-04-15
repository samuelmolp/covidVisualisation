import requests
import json
import datetime
import time
import os

"""
File to load the cases of covid19 each day by fetching an API
It saves the info for each day in a json file and all the info in a general.json file
"""

START_DATE = datetime.datetime.strptime("2021-11-10", '%Y-%m-%d')


def getCasesByCountryAndDate(date, country):
    """
    Funtion to get the cases of a diven country a given day

    Parametres:
        -Date: str (year-month-day). The day of which we want to retrieve the data
        -Country: the country of which we want to retrieve the data (str)
    
    Returns: the cases of the given country the given day (int)
    """
    for x in range(100):
        try:
            url = f"https://api.covid19tracking.narrativa.com/api/{date}/country/{country}"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload).json()
            break
        except:
            time.sleep(15)

    try:
        return response["dates"][date]["countries"][country]["today_new_confirmed"]
    except:
        return

def getAllCountries():
    """
    Function to get the names of all countries by fetching the api
    Returns: list with the names of all of the countries
    """
    for x in range(100):
        try:
            url = "https://api.covid19tracking.narrativa.com/api/countries"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload).json()
            break
        except:
            time.sleep(15)


    countries = []

    for country in response["countries"]:
        countries.append(country["name"])

    return countries


def getAllDataByDate(date):
    """
    Function to get all the covid cases in each country of a given date
    Parametres:
        -Date: str (year-month-day). The day of which we want to retrieve the data
    Returns: list of dict {country:num of cases} for each country
    """
    casesInEachCountry = []

    countries = getAllCountries()

    for country in countries:
        print(country)
        casesInEachCountry.append({country:getCasesByCountryAndDate(date, country)})

    addDataToFiles(casesInEachCountry, date)
    return casesInEachCountry


def addDataToFiles(data, date):
    """
    Function to write the data to a json file

    Parametres:
        -Data: as a json object, all data of the date (json)
        -Date: as str (year-month-day). The date of the data
    """
    with open(f'{date}.json', 'w') as outfile:
        json.dump(data, outfile)

def RunWholeScript():
    """
    Function to load data from the start date until today by calling getAllDataByDate
    """
    current_day = START_DATE

    while current_day!=datetime.datetime.now().strftime("%Y-%m-%d"):
        print("\n\n--------------------------------------")
        print(current_day.strftime("%Y-%m-%d"))
        print("--------------------------------------")
        getAllDataByDate(current_day.strftime("%Y-%m-%d"))
        current_day=(current_day+datetime.timedelta(days=1))


def unirFiles():
    """
    Function to take all individual json files and merge them into a general.json file
    In general.json data is defines as a dict whose keys are days. 
    Each value is another dict with keys beign the countries and values beign the cases
    """
    all_files = os.listdir('./')

    final_Data = {}
    current_date= datetime.datetime.strptime("2020-01-23", '%Y-%m-%d')

    for file in all_files:
        if file=='api.py':
            continue

        with open(file) as f:
            data = json.load(f)    
            processed_data = {}

            keys = [next(iter(i.keys())) for i in data]
            values = [next(iter(i.values())) for i in data]

            for x in range(len(keys)):
                processed_data[keys[x]]=values[x]

            final_Data[current_date.strftime("%Y-%m-%d")]=processed_data

            current_date=(current_date+datetime.timedelta(days=1))
    
    addDataToFiles(final_Data, "GENERAL")
    

if __name__ == "__main__":
    #RunWholeScript()
    #unirFiles()
    pass

