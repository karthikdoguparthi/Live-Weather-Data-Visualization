# download_noaa.py
import os, time, requests, pandas as pd
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("NOAA_TOKEN")

HEADERS = {"token": TOKEN}
BASE_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"

def download_all(params, max_records=None, pause=1.1):
    """
    params: dict of API parameters (datasetid, startdate, etc.)
    max_records: optional hard cap (for development)
    pause: seconds to wait between calls to stay under the 1 req/sec default
    """
    records, offset = [], 1
    while True:
        this_params = params | {"offset": offset}
        resp = requests.get(BASE_URL, headers=HEADERS, params=this_params)
        if resp.status_code == 429:
            # too many requests; NOAA usually tells you how long to wait
            wait = int(resp.headers.get("Retry-After", "60"))
            print(f"Rate-limited. Sleeping {wait}s…")
            time.sleep(wait)
            continue
        resp.raise_for_status()
        batch = resp.json().get("results", [])
        if not batch: break
        records.extend(batch)
        print(f"Fetched {len(batch):4}  | total {len(records):6}")
        if max_records and len(records) >= max_records:
            records = records[:max_records]
            break
        offset += len(batch)
        time.sleep(pause)
    return pd.DataFrame.from_records(records)

if __name__ == "__main__":
    params = {
        "datasetid": "GHCND",
        "stationid": "GHCND:USW00094728",  # Central Park sample
        "startdate": "2024-01-01",
        "enddate":   "2024-12-31",
        "units": "metric",
        "limit": 1000,
    }
    df = download_all(params)
    df.to_csv("central_park_2024_raw.csv", index=False)