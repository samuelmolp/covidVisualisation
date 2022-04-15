from countryinfo import CountryInfo
import requests
import pycountry 
import time
import country_converter as coco


"""
File to get the three arrays used in main.py (iso2, iso3 and population)
"""

def getAllCountries_iso2():
    """
    Returns: list of all iso2 codes of all countries of chich we have data.
    It uses an api but also requires some values hardcoded
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


    input_countries = []

    for country in response["countries"]:
        input_countries.append(country["name"])

    
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2
    codes = [countries.get(country, 'Unknown code') for country in input_countries]

    for x in range(len(input_countries)):
        if x==0:
            codes[x]="US"
        if x==4:
            codes[x]="IR"
        if x==6:
            codes[x]="LA"
        if x==12:
            codes[x]="BU"
        if x==31:
            codes[x]="SY"
        if x==37:
            codes[x]="BN"
        if x==48:
            codes[x]="XK"
        if x==57:
            codes[x]="RU"
        if x==73:
            codes[x]="BO"
        if x==93:
            codes[x]="MD"
        if x==100:
            codes[x]="TW"
        if x==105:
            codes[x]="VN"
        if x==117:
            codes[x]="VA"
        if x==129:
            codes[x]="TZ"
        if x==141:
            codes[x]="VE"
        if x==146:
            codes[x]="TL"
        if x==153:
            codes[x]="FM"
        if x==170:
            codes[x]="KR"
        if x==174:
            codes[x]="CI"
        if x==180:
            codes[x]="CD"

    return codes


def getAllCountries_iso3():
    """
    Function to convert the iso2codes from previous function to iso3 codes
    Returns: list of all iso3 codes of all countries of chich we have data.
    """
    codes = getAllCountries_iso2()
    return coco.convert(names=codes, to='ISO3')


def match_iso3_to_population():
    """
    Function to match iso3 codes to population (uses pycountry api)
    Returns: dict with {iso3 code (str): population(int)}
    """
    codes_iso3 = getAllCountries_iso2()
    codes_iso2 = getAllCountries_iso3()

    population = {}

    x = 0
    for x in range(len(codes_iso3)):
        if codes_iso3[x]!="not found" and codes_iso3[x] not in ["XKX", "AND", "VAT", "MNE"]:                    
            if codes_iso3[x]=="SRB":    
                country = CountryInfo("Serbia")
                population[codes_iso3[x]]=country.population()
                continue

            try:
                country = CountryInfo(codes_iso2[x])
                population[codes_iso3[x]]=country.population()
            except KeyError:
                try:
                    country = CountryInfo(codes_iso2[x])
                    population[codes_iso3[x]]=country.population()
                except KeyError:
                    pass
        
        x+=1

    return population


if __name__ == "__main__":
    #match_iso3_to_population()
    pass