from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
import datetime

POPULATION = {'USA': 319259000, 'TCD': 13211000, 'CUB': 11210064, 'FJI': 859178, 'IRN': 77966400, 'IRQ': 36004552, 'LAO': 6693300, 'MLI': 15768000, 'OMN': 4089076, 'PER': 30814175, 'TGO': 6993000, 'BEN': 9988068, 'CHL': 17819054, 'CHN': 1367110000, 'EGY': 87668100, 'GAB': 1711000, 'GHA': 27043093, 'HTI': 10745665, 'IND': 1263930000, 'ITA': 60769102, 'JPN': 127080000, 'KEN': 41800000, 'LBY': 6253000, 'MLT': 416055, 'NPL': 27646053, 'NER': 17138707, 'QAT': 2269672, 'WSM': 187820, 'ESP': 46507760, 'SDN': 37289406, 'SYR': 22964324, 'YEM': 25956000, 'AGO': 24383301, 'BLZ': 349728, 'BTN': 755030, 'BRA': 203586000, 'BRN': 393372, 'CAN': 35540419, 'CYP': 858000, 'FRA': 66078000, 'GMB': 1882450, 'GRC': 10992589, 'GIN': 10628972, 'GUY': 784894, 'ISR': 8268400, 'JEY': 99000, 'JOR': 6666960, 'KWT': 3268431, 'LVA': 1991800, 'MWI': 15805239, 'MEX': 119713203, 'MCO': 36950, 'NOR': 5156450, 'PAN': 3713312, 'POL': 38496000, 'RUS': 146233000, 'RWA': 10996891, 'SRB': 7186862, 'SWE': 9737521, 'TUR': 76667864, 'UGA': 34856813, 'ZMB': 15023315, 'ALB': 2895947, 'DZA': 38700000, 'ARM': 3009800, 'AUT': 8527230, 'BHS': 319031, 'BHR': 1316500, 'BLR': 9475100, 'BEL': 11225469, 'BOL': 10027254, 'BDI': 9530434, 'COM': 763952, 'HRV': 4267558, 'CZE': 10521600, 'DNK': 5655750, 'ECU': 15888900, 'ERI': 6536000, 'EST': 1315819, 'FIN': 5470437, 'GEO': 4490500, 'DEU': 80783000, 'GRD': 103328, 'HUN': 9879000, 'ISL': 328170, 'IRL': 6378000, 'JAM': 2717991, 'LBN': 4104000, 'LSO': 2098000, 'LBR': 4397000, 'MDA': 3557600, 'MAR': 33465000, 'NAM': 2113077, 'NGA': 178517000, 'ROU': 19942642, 'SEN': 13508715, 'SOM': 10806000, 'TWN': 23424615, 'TUN': 10982754, 'UKR': 42973696, 'URY': 3404189, 'VUT': 264652, 'VNM': 89708900, 'BRB': 285000, 'BWA': 2024904, 'BGR': 7245677, 'KHM': 15184116, 'CMR': 20386799, 'COL': 47907800, 'DJI': 886000, 'DMA': 71293, 'SWZ': 1106189, 'ETH': 87952991, 'GGY': 63085, 'HND': 8725111, 'KIR': 106461, 'MYS': 30430500, 'MDV': 341256, 'MNG': 2987733, 'PAK': 188410000, 'PRY': 6893727, 'PRT': 10477800, 'SVK': 5415949, 'SVN': 2064966, 'SUR': 534189, 'TZA': 47421786, 'THA': 64871000, 'ZWE': 13061239, 'ARG': 42669500, 'AUS': 23696900, 'GTM': 15806675, 'IDN': 252164800, 'LTU': 2927310, 'MUS': 1261208, 'NIC': 6134270, 'SGP': 5469700, 'LKA': 20277597, 'VEN': 30206307, 'AZE': 9552500, 'BGD': 157486000, 'CPV': 518467, 'CRI': 4713168, 'TLS': 1172390, 'KAZ': 17377800, 'KGZ': 5776570, 'LUX': 549700, 'MDG': 21842167, 'MRT': 3545620, 'FSM': 101351, 'MOZ': 25041922, 'SMR': 32743, 'SYC': 89949, 'TJK': 8161000, 'UZB': 30492800, 'AFG': 26023100, 'SLV': 6401240, 'NLD': 16881000, 'NZL': 4547900, 'PHL': 100697400, 'LCA': 184000, 'SSD': 11384393, 'CHE': 8183800, 'BFA': 17322796, 'KOR': 50423955, 'SAU': 30770375, 'SLE': 6205000, 'ZAF': 54002000, 'CIV': 23821000, 'GNB': 1746000, 'LIE': 37132, 'GBR': 64105654, 'ESH': 586000, 'MKD': 2058539, 'COD': 69360000, 'PNG': 7398500, 'GNQ': 1430000, 'DOM': 10378267, 'ATG': 86295, 'TTO': 1328019, 'ARE': 9446000, 'KNA': 55000, 'STP': 187356, 'BIH': 3791622, 'CAF': 4709000, 'VCT': 109000}
CODES_ISO3 = ['USA', 'TCD', 'CUB', 'FJI', 'IRN', 'IRQ', 'LAO', 'MLI', 'OMN', 'PER', 'TGO', 'BEN', 'not found', 'CHL', 'CHN', 'EGY', 'GAB', 'GHA', 'HTI', 'IND', 'ITA', 'JPN', 'KEN', 'LBY', 'MLT', 'NPL', 'NER', 'QAT', 'WSM', 'ESP', 'SDN', 'SYR', 'YEM', 'AGO', 'BLZ', 'BTN', 'BRA', 'BRN', 'CAN', 'CYP', 'FRA', 'GMB', 'GRC', 'GIN', 'GUY', 'ISR', 'JEY', 'JOR', 'XKX', 'KWT', 'LVA', 'MWI', 'MEX', 'MCO', 'NOR', 'PAN', 'POL', 'RUS', 'RWA', 'SRB', 'SWE', 'TUR', 'UGA', 'ZMB', 'ALB', 'DZA', 'AND', 'ARM', 'AUT', 'BHS', 'BHR', 'BLR', 'BEL', 'BOL', 'BDI', 'COM', 'HRV', 'CZE', 'DNK', 'ECU', 'ERI', 'EST', 'FIN', 'GEO', 'DEU', 'GRD', 'HUN', 'ISL', 'IRL', 'JAM', 'LBN', 'LSO', 'LBR', 'MDA', 'MAR', 'NAM', 'NGA', 'ROU', 'SEN', 'SOM', 'TWN', 'TUN', 'UKR', 'URY', 'VUT', 'VNM', 'BRB', 'BWA', 'BGR', 'KHM', 'CMR', 'COL', 'DJI', 'DMA', 'SWZ', 'ETH', 'GGY', 'VAT', 'HND', 'KIR', 'MYS', 'MDV', 'MNG', 'PAK', 'PRY', 'PRT', 'SVK', 'SVN', 'SUR', 'TZA', 'THA', 'ZWE', 'ARG', 'AUS', 'GTM', 'IDN', 'LTU', 'MUS', 'NIC', 'SGP', 'LKA', 'VEN', 'AZE', 'BGD', 'CPV', 'CRI', 'TLS', 'KAZ', 'KGZ', 'LUX', 'not found', 'MDG', 'MRT', 'FSM', 'MNE', 'MOZ', 'SMR', 'SYC', 'TJK', 'UZB', 'AFG', 'SLV', 'NLD', 'NZL', 'PHL', 'LCA', 'SSD', 'CHE', 'TLS', 'BFA', 'KOR', 'SAU', 'SLE', 'ZAF', 'CIV', 'GNB', 'LIE', 'GBR', 'ESH', 'MKD', 'COD', 'not found', 'PNG', 'GNQ', 'DOM', 'not found', 'ATG', 'not found', 'TTO', 'ARE', 'KNA', 'STP', 'BIH', 'CAF', 'VCT']
CODES_ISO2 = ['US', 'TD', 'CU', 'FJ', 'IR', 'IQ', 'LA', 'ML', 'OM', 'PE', 'TG', 'BJ', 'Unknown code', 'CL', 'CN', 'EG', 'GA', 'GH', 'HT', 'IN', 'IT', 'JP', 'KE', 'LY', 'MT', 'NP', 'NE', 'QA', 'WS', 'ES', 'SD', 'SY', 'YE', 'AO', 'BZ', 'BT', 'BR', 'BN', 'CA', 'CY', 'FR', 'GM', 'GR', 'GN', 'GY', 'IL', 'JE', 'JO', 'XK', 'KW', 'LV', 'MW', 'MX', 'MC', 'NO', 'PA', 'PL', 'RU', 'RW', 'RS', 'SE', 'TR', 'UG', 'ZM', 'AL', 'DZ', 'AD', 'AM', 'AT', 'BS', 'BH', 'BY', 'BE', 'BO', 'BI', 'KM', 'HR', 'CZ', 'DK', 'EC', 'ER', 'EE', 'FI', 'GE', 'DE', 'GD', 'HU', 'IS', 'IE', 'JM', 'LB', 'LS', 'LR', 'MD', 'MA', 'NA', 'NG', 'RO', 'SN', 'SO', 'TW', 'TN', 'UA', 'UY', 'VU', 'VN', 'BB', 'BW', 'BG', 'KH', 'CM', 'CO', 'DJ', 'DM', 'SZ', 'ET', 'GG', 'VA', 'HN', 'KI', 'MY', 'MV', 'MN', 'PK', 'PY', 'PT', 'SK', 'SI', 'SR', 'TZ', 'TH', 'ZW', 'AR', 'AU', 'GT', 'ID', 'LT', 'MU', 'NI', 'SG', 'LK', 'VE', 'AZ', 'BD', 'CV', 'CR', 'TL', 'KZ', 'KG', 'LU', 'Unknown code', 'MG', 'MR', 'FM', 'ME', 'MZ', 'SM', 'SC', 'TJ', 'UZ', 'AF', 'SV', 'NL', 'NZ', 'PH', 'LC', 'SS', 'CH', 'TL', 'BF', 'KR', 'SA', 'SL', 'ZA', 'CI', 'GW', 'LI', 'GB', 'EH', 'MK', 'CD', 'Unknown code', 'PG', 'GQ', 'DO', 'Unknown code', 'AG', 'Unknown code', 'TT', 'AE', 'KN', 'ST', 'BA', 'CF', 'VC']
ISO2_CODES_BY_COUNTRY = {
   "africa":['AO', 'BF', 'BI', 'BJ', 'BW', 'CD', 'CF', 'CG', 'CI', 'CM', 'CV', 'DJ', 'DZ', 'EG', 'EH', 'ER', 'ET','GA', 'GH', 'GM', 'GN', 'GQ', 'GW', 'KE', 'KM', 'LR', 'LS', 'LY', 'MA', 'MG', 'ML', 'MR', 'MU', 'MW','MZ', 'NA', 'NE', 'NG', 'RE', 'RW', 'SC', 'SD', 'SH', 'SL', 'SN', 'SO', 'ST', 'SZ', 'TD', 'TG', 'TN','TZ', 'UG', 'YT', 'ZA', 'ZM', 'ZW'],
   "europe":['AD', 'AL', 'AT', 'AX', 'BA', 'BE', 'BG', 'BY', 'CH', 'CZ', 'DE', 'DK', 'EE', 'ES', 'EU', 'FI', 'FO','FR', 'FX', 'GB', 'GG', 'GI', 'GR', 'HR', 'HU', 'IE', 'IM', 'IS', 'IT', 'JE', 'LI', 'LT', 'LU', 'LV','MC', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'RU', 'SE', 'SI', 'SJ', 'SK', 'SM','TR', 'UA', 'VA'],
   "asia":['AE', 'AF', 'AM', 'AP', 'AZ', 'BD', 'BH', 'BN', 'BT', 'CC', 'CN', 'CX', 'CY', 'GE', 'HK', 'ID', 'IL','IN', 'IO', 'IQ', 'IR', 'JO', 'JP', 'KG', 'KH', 'KP', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'MM', 'MN','MO', 'MV', 'MY', 'NP', 'OM', 'PH', 'PK', 'PS', 'QA', 'SA', 'SG', 'SY', 'TH', 'TJ', 'TL', 'TM', 'TW','UZ', 'VN', 'YE'],
   "south_america":['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PE', 'PY', 'SR', 'UY', 'VE'],
   "north_america":['AG', 'AI', 'AN', 'AW', 'BB', 'BL', 'BM', 'BS', 'BZ', 'CA', 'CR', 'CU', 'DM', 'DO', 'GD', 'GL', 'GP','GT', 'HN', 'HT', 'JM', 'KN', 'KY', 'LC', 'MF', 'MQ', 'MS', 'MX', 'NI', 'PA', 'PM', 'PR', 'SV', 'TC','TT', 'US', 'VC', 'VG', 'VI'],
   "oceania":['AS', 'AU', 'CK', 'FJ', 'FM', 'GU', 'KI', 'MH', 'MP', 'NC', 'NF', 'NR', 'NU', 'NZ', 'PF', 'PG', 'PN','PW', 'SB', 'TK', 'TO', 'TV', 'UM', 'VU', 'WF', 'WS']
}


def index(request):
    return render(request, "visualitation/index.html") 

def images(request):
    return render(request, "visualitation/images.html")

def stats(request):
    return render(request, "visualitation/stats.html")

def videos(request):
    return render(request, "visualitation/videos.html")

def aboutData(request):
    return render(request, "visualitation/aboutData.html")


def get_data(request, start_date, end_date, type, region):
    region = region.lower()
    region = region.replace(" ", "_")
    with open('C:\\Users\lmoli\Desktop\PROGRAMACIÓN\proyectoBio\\GENERAL.json') as f:
        rawData = json.load(f)

    current_date = start_date

    dataForGraphic = {
        "start_date":start_date,
        "end_date":end_date,
        "data":{}
    }

    
    while current_date <= end_date:
        dataForGraphic["data"][current_date] = 0
        if type=="Daily cases":
            x=0
            for country in rawData[current_date]:
                if region!="world":
                    if CODES_ISO2[x] not in ISO2_CODES_BY_COUNTRY[region]:
                        x+=1
                        continue

                dataForGraphic["data"][current_date] += rawData[current_date][country]
                x+=1    

        if type=="Daily cases by 100.000 people":
            relative_cases = getRelativeCases(rawData, current_date, region)
            dataForGraphic["data"][current_date] = relative_cases

        elif type=="Cases by 100.000 people in last 5 days":
            total_sum = 0
            dayObj = datetime.datetime.strptime(current_date, '%Y-%m-%d')
            for x in range(5):
                total_sum+=getRelativeCases(rawData, dayObj.strftime('%Y-%m-%d'), region)
                dayObj = dayObj-datetime.timedelta(1)

            dataForGraphic["data"][current_date] = round(total_sum/5, 3)


        current_dateObj = datetime.datetime.strptime(current_date, '%Y-%m-%d')
        current_date=(current_dateObj+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    return JsonResponse(dataForGraphic)


def getRelativeCases(rawData, current_date, region):
    region_population = 0
    region_total_cases = 0
    x=0
    for country in rawData[current_date]:
        if region!="world":
            if CODES_ISO2[x] not in ISO2_CODES_BY_COUNTRY[region]:
                x+=1
                continue

        try:
            region_population+=POPULATION[CODES_ISO3[x]]
            region_total_cases+=rawData[current_date][country]
        except KeyError:
            pass
        
        x+=1

    return round((region_total_cases/region_population)*100000, 3)
