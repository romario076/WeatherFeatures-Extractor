# Historical weather exctractor
Using this tool it is possible to extract lots of features based on weather metereology, solar cooking and others.
It is very good additional source for preparing features into machine learning problems. 

Source: https://power.larc.nasa.gov/#page-top

Parameters and features description: https://power.larc.nasa.gov/#resources
<hr>
Using config.py file it is possible to manage this weather extractor:
<li> Specify 'startday' and 'endday' for which you want to get weather or other variables, depends which you will specify.
<li> Specify 'saveDir' - directory where will be saved you results. For each country separate file.
<li> Use 'parameters' to specify which features you want to extract. List of available feature in the link above. 'parameters' - should be a string witj comma seperator between features.
<li> 'inputFile_path' - path to csv file which contains input information. If file contains post codes it should has columns: Country, PostCode. If file not contains postcodes, but has geo coordinates, it should contain columns: Country, latitude, longitude.
<li> 'usePostCodes' - if it is true then for extracting will be using postcodes, and they should be present in 'inputFile_path', if false, then 'inputFile_path' should contain latitude, longitude columns with geographical coordinates.
<li> 'useMultiprocess' - if true, then extraction logic will be based on multiprocess approach, if false - simple in the loop.
  
<hr>
  
To run the extractor create your 'inputFile_path', depends on your needs, check config.py and run extractWeater.py. 
All results will be stored to the location which you specified in configs.py
