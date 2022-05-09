
class configs:
    startdate = '2021-06-08'
    enddate = '2021-07-20'
    saveDir = './weatherData/'
    parameters = 'T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN'
    inputFile_path = './Country_city_postcodes.csv'
    usePostCodes = True
    useMultiprocess = True

### Descrption parameters: https://power.larc.nasa.gov/#resources
### https://power.larc.nasa.gov/docs/tutorials/parameters/