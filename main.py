# https://docs.python.org/3/library/json.html
# This library will be used to parse the JSON data returned by the API.
import json
# This Library will be used for creating the Datetime input of the API
import time
import datetime
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request

apikey = "229f000b2712074b8d397e9c2e5d1e58" 
today = datetime.date.today()

# Schleife für jeden Tag des letzten Jahres
for i in range(1):
    # Datum für den aktuellen Tag berechnen
    day = today - datetime.timedelta(days=i)

    # Startzeitpunkt für den aktuellen Tag
    start = datetime.datetime.combine(day, datetime.time.min).isoformat()

    # Endzeitpunkt für den aktuellen Tag
    end = datetime.datetime.combine(day, datetime.time.max).isoformat()

    # Hier können Sie Ihren Code für jeden Tag einfügen
    # Beispiel: Drucken des Start- und Endzeitpunkts
    url = f"https://gnews.io/api/v4/search?q=ukraine war&lang=en&max=100&expand=content&apikey={apikey}"


    with urllib.request.urlopen(url) as response:
        response_data = json.loads(response.read().decode("utf-8"))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open("responses/data.json."+timestr,"w") as file:
        json.dump(response_data, file)

