# Download osm large file in chunks 

import requests

from datetime import date
today = date.today()
yr =str(today.year)
mn =str(today.month)
day =str(today.day)

file_name =yr+mn.zfill(2)+day.zfill(2)+"_myanmar_osm.zip"



url1 ='https://download.geofabrik.de/asia/myanmar-latest-free.shp.zip'
r = requests.get(url1,stream = True)
with open("20191020-myanmar-osm.zip","wb") as osm:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            osm.write(chunk)
            print("1024")
