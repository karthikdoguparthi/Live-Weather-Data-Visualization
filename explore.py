
# explore.py
import os, requests, json
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("NOAA_TOKEN")
headers = {"token": TOKEN}

def api(endpoint, **params):
    root = "https://www.ncdc.noaa.gov/cdo-web/api/v2"
    r = requests.get(f"{root}/{endpoint}", headers=headers, params=params)
    r.raise_for_status()
    return r.json()

# 3.1 List datasets (temperature, precipitation, normals…)
datasets = api("datasets", limit=100)["results"]
print(json.dumps(datasets, indent=2)[:2000])  # peek at the first 2 KB

# 3.2 List location categories and locations (e.g. CITY, STATE, COUNTY)
cats = api("locationcategories", limit=100)["results"]
print(cats)

# 3.3 List the first 10 NYC stations
nyc_stations = api("stations", locationid="CITY:US360019", datasetid="GHCND", limit=10)["results"]
print(json.dumps(nyc_stations, indent=2))