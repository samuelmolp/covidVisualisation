from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import datetime
import json
import cv2
import os


#Arrays obtained from utils.py
POPULATION = {'USA': 319259000, 'TCD': 13211000, 'CUB': 11210064, 'FJI': 859178, 'IRN': 77966400, 'IRQ': 36004552, 'LAO': 6693300, 'MLI': 15768000, 'OMN': 4089076, 'PER': 30814175, 'TGO': 6993000, 'BEN': 9988068, 'CHL': 17819054, 'CHN': 1367110000, 'EGY': 87668100, 'GAB': 1711000, 'GHA': 27043093, 'HTI': 10745665, 'IND': 1263930000, 'ITA': 60769102, 'JPN': 127080000, 'KEN': 41800000, 'LBY': 6253000, 'MLT': 416055, 'NPL': 27646053, 'NER': 17138707, 'QAT': 2269672, 'WSM': 187820, 'ESP': 46507760, 'SDN': 37289406, 'SYR': 22964324, 'YEM': 25956000, 'AGO': 24383301, 'BLZ': 349728, 'BTN': 755030, 'BRA': 203586000, 'BRN': 393372, 'CAN': 35540419, 'CYP': 858000, 'FRA': 66078000, 'GMB': 1882450, 'GRC': 10992589, 'GIN': 10628972, 'GUY': 784894, 'ISR': 8268400, 'JEY': 99000, 'JOR': 6666960, 'KWT': 3268431, 'LVA': 1991800, 'MWI': 15805239, 'MEX': 119713203, 'MCO': 36950, 'NOR': 5156450, 'PAN': 3713312, 'POL': 38496000, 'RUS': 146233000, 'RWA': 10996891, 'SRB': 7186862, 'SWE': 9737521, 'TUR': 76667864, 'UGA': 34856813, 'ZMB': 15023315, 'ALB': 2895947, 'DZA': 38700000, 'ARM': 3009800, 'AUT': 8527230, 'BHS': 319031, 'BHR': 1316500, 'BLR': 9475100, 'BEL': 11225469, 'BOL': 10027254, 'BDI': 9530434, 'COM': 763952, 'HRV': 4267558, 'CZE': 10521600, 'DNK': 5655750, 'ECU': 15888900, 'ERI': 6536000, 'EST': 1315819, 'FIN': 5470437, 'GEO': 4490500, 'DEU': 80783000, 'GRD': 103328, 'HUN': 9879000, 'ISL': 328170, 'IRL': 6378000, 'JAM': 2717991, 'LBN': 4104000, 'LSO': 2098000, 'LBR': 4397000, 'MDA': 3557600, 'MAR': 33465000, 'NAM': 2113077, 'NGA': 178517000, 'ROU': 19942642, 'SEN': 13508715, 'SOM': 10806000, 'TWN': 23424615, 'TUN': 10982754, 'UKR': 42973696, 'URY': 3404189, 'VUT': 264652, 'VNM': 89708900, 'BRB': 285000, 'BWA': 2024904, 'BGR': 7245677, 'KHM': 15184116, 'CMR': 20386799, 'COL': 47907800, 'DJI': 886000, 'DMA': 71293, 'SWZ': 1106189, 'ETH': 87952991, 'GGY': 63085, 'HND': 8725111, 'KIR': 106461, 'MYS': 30430500, 'MDV': 341256, 'MNG': 2987733, 'PAK': 188410000, 'PRY': 6893727, 'PRT': 10477800, 'SVK': 5415949, 'SVN': 2064966, 'SUR': 534189, 'TZA': 47421786, 'THA': 64871000, 'ZWE': 13061239, 'ARG': 42669500, 'AUS': 23696900, 'GTM': 15806675, 'IDN': 252164800, 'LTU': 2927310, 'MUS': 1261208, 'NIC': 6134270, 'SGP': 5469700, 'LKA': 20277597, 'VEN': 30206307, 'AZE': 9552500, 'BGD': 157486000, 'CPV': 518467, 'CRI': 4713168, 'TLS': 1172390, 'KAZ': 17377800, 'KGZ': 5776570, 'LUX': 549700, 'MDG': 21842167, 'MRT': 3545620, 'FSM': 101351, 'MOZ': 25041922, 'SMR': 32743, 'SYC': 89949, 'TJK': 8161000, 'UZB': 30492800, 'AFG': 26023100, 'SLV': 6401240, 'NLD': 16881000, 'NZL': 4547900, 'PHL': 100697400, 'LCA': 184000, 'SSD': 11384393, 'CHE': 8183800, 'BFA': 17322796, 'KOR': 50423955, 'SAU': 30770375, 'SLE': 6205000, 'ZAF': 54002000, 'CIV': 23821000, 'GNB': 1746000, 'LIE': 37132, 'GBR': 64105654, 'ESH': 586000, 'MKD': 2058539, 'COD': 69360000, 'PNG': 7398500, 'GNQ': 1430000, 'DOM': 10378267, 'ATG': 86295, 'TTO': 1328019, 'ARE': 9446000, 'KNA': 55000, 'STP': 187356, 'BIH': 3791622, 'CAF': 4709000, 'VCT': 109000}
CODES_ISO3 = ['USA', 'TCD', 'CUB', 'FJI', 'IRN', 'IRQ', 'LAO', 'MLI', 'OMN', 'PER', 'TGO', 'BEN', 'not found', 'CHL', 'CHN', 'EGY', 'GAB', 'GHA', 'HTI', 'IND', 'ITA', 'JPN', 'KEN', 'LBY', 'MLT', 'NPL', 'NER', 'QAT', 'WSM', 'ESP', 'SDN', 'SYR', 'YEM', 'AGO', 'BLZ', 'BTN', 'BRA', 'BRN', 'CAN', 'CYP', 'FRA', 'GMB', 'GRC', 'GIN', 'GUY', 'ISR', 'JEY', 'JOR', 'XKX', 'KWT', 'LVA', 'MWI', 'MEX', 'MCO', 'NOR', 'PAN', 'POL', 'RUS', 'RWA', 'SRB', 'SWE', 'TUR', 'UGA', 'ZMB', 'ALB', 'DZA', 'AND', 'ARM', 'AUT', 'BHS', 'BHR', 'BLR', 'BEL', 'BOL', 'BDI', 'COM', 'HRV', 'CZE', 'DNK', 'ECU', 'ERI', 'EST', 'FIN', 'GEO', 'DEU', 'GRD', 'HUN', 'ISL', 'IRL', 'JAM', 'LBN', 'LSO', 'LBR', 'MDA', 'MAR', 'NAM', 'NGA', 'ROU', 'SEN', 'SOM', 'TWN', 'TUN', 'UKR', 'URY', 'VUT', 'VNM', 'BRB', 'BWA', 'BGR', 'KHM', 'CMR', 'COL', 'DJI', 'DMA', 'SWZ', 'ETH', 'GGY', 'VAT', 'HND', 'KIR', 'MYS', 'MDV', 'MNG', 'PAK', 'PRY', 'PRT', 'SVK', 'SVN', 'SUR', 'TZA', 'THA', 'ZWE', 'ARG', 'AUS', 'GTM', 'IDN', 'LTU', 'MUS', 'NIC', 'SGP', 'LKA', 'VEN', 'AZE', 'BGD', 'CPV', 'CRI', 'TLS', 'KAZ', 'KGZ', 'LUX', 'not found', 'MDG', 'MRT', 'FSM', 'MNE', 'MOZ', 'SMR', 'SYC', 'TJK', 'UZB', 'AFG', 'SLV', 'NLD', 'NZL', 'PHL', 'LCA', 'SSD', 'CHE', 'TLS', 'BFA', 'KOR', 'SAU', 'SLE', 'ZAF', 'CIV', 'GNB', 'LIE', 'GBR', 'ESH', 'MKD', 'COD', 'not found', 'PNG', 'GNQ', 'DOM', 'not found', 'ATG', 'not found', 'TTO', 'ARE', 'KNA', 'STP', 'BIH', 'CAF', 'VCT']
CODES_ISO2 = ['US', 'TD', 'CU', 'FJ', 'IR', 'IQ', 'LA', 'ML', 'OM', 'PE', 'TG', 'BJ', 'Unknown code', 'CL', 'CN', 'EG', 'GA', 'GH', 'HT', 'IN', 'IT', 'JP', 'KE', 'LY', 'MT', 'NP', 'NE', 'QA', 'WS', 'ES', 'SD', 'SY', 'YE', 'AO', 'BZ', 'BT', 'BR', 'BN', 'CA', 'CY', 'FR', 'GM', 'GR', 'GN', 'GY', 'IL', 'JE', 'JO', 'XK', 'KW', 'LV', 'MW', 'MX', 'MC', 'NO', 'PA', 'PL', 'RU', 'RW', 'RS', 'SE', 'TR', 'UG', 'ZM', 'AL', 'DZ', 'AD', 'AM', 'AT', 'BS', 'BH', 'BY', 'BE', 'BO', 'BI', 'KM', 'HR', 'CZ', 'DK', 'EC', 'ER', 'EE', 'FI', 'GE', 'DE', 'GD', 'HU', 'IS', 'IE', 'JM', 'LB', 'LS', 'LR', 'MD', 'MA', 'NA', 'NG', 'RO', 'SN', 'SO', 'TW', 'TN', 'UA', 'UY', 'VU', 'VN', 'BB', 'BW', 'BG', 'KH', 'CM', 'CO', 'DJ', 'DM', 'SZ', 'ET', 'GG', 'VA', 'HN', 'KI', 'MY', 'MV', 'MN', 'PK', 'PY', 'PT', 'SK', 'SI', 'SR', 'TZ', 'TH', 'ZW', 'AR', 'AU', 'GT', 'ID', 'LT', 'MU', 'NI', 'SG', 'LK', 'VE', 'AZ', 'BD', 'CV', 'CR', 'TL', 'KZ', 'KG', 'LU', 'Unknown code', 'MG', 'MR', 'FM', 'ME', 'MZ', 'SM', 'SC', 'TJ', 'UZ', 'AF', 'SV', 'NL', 'NZ', 'PH', 'LC', 'SS', 'CH', 'TL', 'BF', 'KR', 'SA', 'SL', 'ZA', 'CI', 'GW', 'LI', 'GB', 'EH', 'MK', 'CD', 'Unknown code', 'PG', 'GQ', 'DO', 'Unknown code', 'AG', 'Unknown code', 'TT', 'AE', 'KN', 'ST', 'BA', 'CF', 'VC']

#Next arrays copied from the internet
africa_country_list = ['ZM', 'BF', 'TZ', 'EG', 'UG', 'TN', 'TG', 'SZ', 'SD', 'EH', 'SS', 'ZW', 'ZA', 'SO', 'SL', 'SC', 'SN', 'ST', 'SH', 'RW', 'RE', 'GW', 'NG', 'NE', 'NA', 'MZ', 'MA', 'MU', 'MR', 'ML', 'MW', 'MG', 'LY', 'LR', 'LS', 'KE', 'CI', 'GN', 'GH', 'GM', 'GA', 'DJ', 'ER', 'ET', 'GQ', 'BJ', 'CD', 'CG', 'YT', 'KM', 'TD', 'CF', 'CV', 'CM', 'BI', 'BW', 'AO', 'DZ']
europe_country_list = ["AUT","BEL","BGR","HRV","CYP","CZE","DNK","EST","FIN","FRA","DEU","GRC","HUN","IRL","ITA","LVA","LTU","LUX","MLT", "NLD","POL","PRT","ROU","SVK","SVN","ESP","SWE"]
asia_country_list = ['AE', 'AF', 'AM', 'AP', 'AZ', 'BD', 'BH', 'BN', 'BT', 'CC', 'CN', 'CX', 'CY', 'GE', 'HK', 'ID', 'IL','IN', 'IO', 'IQ', 'IR', 'JO', 'JP', 'KG', 'KH', 'KP', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'MM', 'MN','MO', 'MV', 'MY', 'NP', 'OM', 'PH', 'PK', 'PS', 'QA', 'SA', 'SG', 'SY', 'TH', 'TJ', 'TL', 'TM', 'TW','UZ', 'VN', 'YE',]
south_america_country_list = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PE', 'PY', 'SR', 'UY', 'VE']

class dataInDay:
    """
    Class to create the image of a given day
    """
    def __init__(self, day, type, region):
        """
        Parametres:
            -Day: string (year-month-day)
                 the day of which it is going to create the image
            -Type: one of the following:
                -cases: daily covid cases
                -relative_cases: daily cases by 100.000 people
                -5days_relative_cases: cases by 100.000 people in the last 5 days (average)                

            -Region: one of the following:
                -world
                -europe
                -africa
                -asia
                -south_america
        """
        if type not in ["cases", "relative_cases", "5days_relative_cases"]:
            print("Not supported type")
            return
        
        if type=="5days_relative_cases":
            if day < "2020-01-27":
                print("For this type, dat must be from 2020-01-07 to 2022-03-04")
                return

        if day > "2022-03-04":
            print("Date must be before the 2022-03-04")
            return

        if day <"2020-01-23":
            print("Date must be after the 2020-01-23")
            return

        if region not in ["africa", "world", "europe", "asia", "south_america"]:
            print("Region must be one of the following: africa, europe, asia, south_america, world")
            return

        self.day = day
        self.type = type
        self.region = region

        covidData = self.loadCovidData()
        mapInfo = self.loadMapInfo()

        #Merge into the same dataframe the info of covid and map
        self.generalData = covidData.merge(mapInfo, how="left")
        self.generalData = GeoDataFrame(self.generalData)

        if self.region=="africa":
            self.generalData = self.generalData[self.generalData['ISO2'].isin(africa_country_list)]
        elif self.region=="europe":
            self.generalData = self.generalData[self.generalData['ISO3'].isin(europe_country_list)]
        elif self.region=="asia":
            self.generalData = self.generalData[self.generalData['ISO2'].isin(asia_country_list)]
        elif self.region=="south_america":
            self.generalData = self.generalData[self.generalData['ISO2'].isin(south_america_country_list)]


        self.plot()
        


    def loadCovidData(self):
        """
        Function to load the covid data.
        It reads the information from general.json (created in getData.py)
        Returns: all covid data of given day as a numpy dataframe with coloumns:
            country_name, iso2, iso3, covid data (depends on the type)
        """
        if self.type=="cases":
            covidData = {
                "country_name": [],
                "ISO3": [], 
                "ISO2": [],
                "covid_cases":[]
            }
        elif self.type=="relative_cases":
            covidData = {
                "country_name": [],
                "ISO3": [], 
                "ISO2": [],
                "relative_covid_cases":[]
            }
        elif self.type=="5days_relative_cases":
            covidData = {
                "country_name": [],
                "ISO3": [], 
                "ISO2": [],
                "five_days_relative_covid_cases":[]
            }


        with open('GENERAL.json') as f:
            rawData = json.load(f)

        x=0
        for country in rawData[self.day]:
            if CODES_ISO3[x]!="not found" and CODES_ISO3[x] not in ["XKX", "AND", "VAT", "MNE"]:                    
                    if self.type=="cases":
                        covidData["covid_cases"].append(rawData[self.day][country])

                    elif self.type=="relative_cases":
                        relativeCases = self.getRelativeCases(rawData[self.day][country], CODES_ISO3[x])
                        if relativeCases!=None:
                            covidData["relative_covid_cases"].append(relativeCases)
                        else:
                            continue

                    elif self.type=="5days_relative_cases":
                        five_days_relative_covid_cases = self.get5DaysRelativeCases(rawData, CODES_ISO3[x], country)
                        covidData["five_days_relative_covid_cases"].append(five_days_relative_covid_cases)
        

                    covidData["country_name"].append(country)
                    covidData["ISO3"].append(CODES_ISO3[x])
                    covidData["ISO2"].append(CODES_ISO2[x])
            x+=1

        return pd.DataFrame(covidData)

    def loadMapInfo(self):
        """
        Loads the information of the map by a shapefile.
        Returns a dataframe with all the info
        """
        SHAPE_RESTORE_SHX = "YES"
        SHAPEFILE = './mapsData/ne_10m_admin_0_countries.shp'
        geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
        geo_df.columns = ['country', 'ISO3', 'geometry']
        geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)

        return geo_df

    def loadEuropeMapInfo(self):
        pass
        SHAPEFILE = './europeShapefile/NUTS_RG_20M_2021_3035.shp'
        geo_df = gpd.read_file(SHAPEFILE)

        print(geo_df)

    def plot(self):
        """
        Function to plot (with geopandas) the information of the merged dataframe
        It finally stores the image (with the day as title)
        """
        if self.type=="cases":
            col = 'covid_cases'
            title = f'COVID-19 cases {self.day}'

        elif self.type=="relative_cases":
            col = "relative_covid_cases"
            title = f'COVID-19 cases by 100.000 people {self.day}'
        elif self.type=="5days_relative_cases":
            col = "five_days_relative_covid_cases"
            title = f'COVID-19 cases by 100.000 people {self.day} in the last 5 days'

        df = self.generalData
        source = 'Source: la narrativa'
        vmin = df[col].min()
        vmax = df[col].max()


        fig, ax = plt.subplots(1, figsize=(20, 8))
        ax.axis('off')

        df.plot(column=col, ax=ax, edgecolor='0.8', linewidth=1, cmap="Reds")

        ax.set_title(title, fontdict={'fontsize': '25', 'fontweight': '3'})
        ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', 
                    verticalalignment='bottom', fontsize=10)
        sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap="Reds")

        sm._A = []
        cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
        cbar = fig.colorbar(sm, cax=cbaxes)

        if self.type=="cases":
            plt.savefig(f"./images/{self.region}/daily_cases/{self.day}")
        elif self.type=="relative_cases":
            plt.savefig(f"./images/{self.region}/relative_daily_cases/{self.day}")
        elif self.type=="5days_relative_cases":
            plt.savefig(f"./images/{self.region}/5days_relative_cases/{self.day}")
        

        plt.close()
        


    def getRelativeCases(self, cases, iso3):
        """
        Get the cases by 100.000 people

        Parametres:
            -cases: covid cases that day (int)
            -iso3: iso3 code of the country (str)

        Returns: relative cases (int)
        """
        population = POPULATION[iso3]
        
        return (cases/population)*100000


    def get5DaysRelativeCases(self, rawData, iso3, country_name):
        """
        Gets the average cases by 100.000 people in the last 5 days

        Parametres:
            rawData: the info from general.json as a json object (json)
            iso3: iso3 code of the required country (str)
            country_name: name of the country (as it appears on general.json) (str)

        Returns: 5 days average of relative cases (int)
        """
        day = datetime.datetime.strptime(self.day, '%Y-%m-%d')
        
        sumOfCases = 0
        for x in range(5):
            day_str = day.strftime('%Y-%m-%d')
            sumOfCases+=self.getRelativeCases(rawData[day_str][country_name], iso3)
            day=day-datetime.timedelta(1)

        return sumOfCases/5


class Video:
    """
    Class to make the video of a specific type 
    (Types are explained in dataInDay class)
    """
    def __init__(self, type, region):
        """
        Parametres:
            -Type: one of the types explained in dataInDay class
            -Regon: one of the regions explained in dataInDay class
        """
        self.type = type
        self.region = region

        self.createVideo()

    def createVideo(self):
        """
        Function to create the video.
        It takes the images from the neccesary path and saves the video
        on current directory as .avi. It might be neccesary then to convert it to mp4
        with ffmpeg.
        """
        if self.type=="cases":
            image_folder = f'./images/{self.region}/daily_cases'
        elif self.type=="relative_cases":
            image_folder = f'./images/{self.region}/relative_daily_cases'
        elif self.type=="5days_relative_cases":
            image_folder = f'./images/{self.region}/5days_relative_cases'

        
        video_name = f'{self.type}_{self.region}_video.avi'

        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 3, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        

    
def runSimulation(type, region):
    """
    Function to create images of all of the days that we have data
    """
    filenames = [file.strip(".json") for file in os.listdir('./jsons')]
    for file in filenames:
        dataInDay(file, type, region)
        

if __name__ == "__main__":    
    #type="5days_relative_cases"
    #region = "south_america"
    #runSimulation(type, region)
    #Video(type, region)
    pass



#ffmpeg -i input.avi output.mp4

