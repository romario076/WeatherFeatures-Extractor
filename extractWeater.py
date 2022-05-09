
from extractor_help_function import *
from config import configs
import warnings
warnings.filterwarnings("ignore")
urllib3.disable_warnings()
pd.set_option('display.max_rows', 100)

### Read input file. Read data with postcodes
# If file contains post codes it should has columns: Country, PostCode
# If file not contains postcodes, but has geo coordinates, it should contain columns: Country, latitude, longitude
data = pd.read_csv(configs.inputFile_path, delimiter=';')

if configs.usePostCodes:
    data = data[data.Country.isin(['DE','FR','ES','UA'])]
    data = data.groupby('Country', as_index=False).head(10)

    ### Get coordinates using post codes
    dataToGetWeather = getCoordinates(citiesDf=data)
else:
    dataToGetWeather = data.copy()
print('Estimated time: ', np.round(dataToGetWeather.shape[0] * 2 / 3600, 3), ' hours\n')

if not os.path.exists(configs.saveDir):
  os.makedirs(configs.saveDir)

st0 = datetime.now()
countries = dataToGetWeather.Country.unique()
for country in countries:
    geoCountry = dataToGetWeather[dataToGetWeather.Country==country]
    if configs.useMultiprocess:
        temperature_data_df = getWeather_multiporcess(geoCountry=geoCountry, country=country)
    else:
        temperature_data_df = getWeather_in_loop(geoCountry=geoCountry, country=country)
    temperature_data_df.to_csv(configs.saveDir+"/"+country+'.csv', index=False)
print("\nTotal Time:", datetime.now()-st0)


