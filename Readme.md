# Live-Weather-Data-Visualization

🌦️ Weather Data Analytics using NOAA API & Tableau

Real-Time Climate Insights from Central Park, New York

🔍 Abstract
  
This project focuses on leveraging publicly available government weather data from the NOAA Climate Data Online (CDO) API to perform end-to-end analytics and dashboarding. The primary objective was to extract real-time and historical weather observations for Central Park, clean and transform the data, and present key insights through 10 interactive Tableau dashboards.

❗ Problem Statement
  
Climate variability and unpredictable weather events demand better data-driven insights for planning and awareness. However, raw meteorological data is often technical, scattered, or not human-friendly. This project addresses that gap by transforming complex, raw weather data into interactive visual stories that are useful for both technical users (climate researchers, analysts) and general decision-makers (urban planners, event organizers, local communities).

✅ Proposed Solution

1. Use NOAA’s developer-friendly Climate Data API to fetch accurate, structured weather data.
2. Automate the ingestion process and maintain secure access through a local token environment.
3.	Perform data cleaning and transformation to prepare the dataset for analysis.
4.	Engineer meaningful weather metrics like Discomfort Index, frequency of special weather events, and correlations between temperature, humidity, and precipitation.
5.	Create 10 Tableau dashboards to visualize patterns, anomalies, and seasonal shifts.

🔄 Workflow Overview
	
1. API Token Configuration -->	
	•	Registered and retrieved API token from NOAA CDO Portal.
	•	Configured Python scripts and a secure environment in VS Code.
2. Data Extraction -->	
	•	Used Python and the requests library to extract JSON and CSV-format data from the NOAA endpoint for Central Park, NY.
3. Data Cleaning & Transformation -->	
	•	Removed nulls, scaled temperature units (tenths of °C to °C), formatted timestamps, and converted categorical codes (e.g., WT01-WT08).
	•	Built calculated fields for advanced metrics such as the Discomfort Index.
4. Feature Engineering -->	
	•	Aggregated and grouped by time (day, week, month).
	•	Extracted patterns in humidity, wind direction, snow depth, etc.
5. Data Visualization (Tableau) -->	
	•	Designed 10 interactive dashboards with slicers, tooltips, color encodings, and dual-axis/heatmap visuals.

Full Forms and Units of Column Names

Abbreviation and Full Form	Unit / Format	Description
1. date	Date	YYYY-MM-DD	Calendar date of the observation
2. ADPT	Average Dew Point Temperature	°C or tenths of °C	Mean dew point temp for the day
3. ASLP	Altimeter Setting Pressure	hPa	Air pressure corrected to sea level
4. ASTP	Station Pressure	hPa	Actual barometric pressure at the station
5. AWBT	Average Wet Bulb Temperature	°C	Daily average wet bulb temperature
6. AWND	Average Wind Speed	tenths of m/s	Daily average wind speed
7. PGTM	Peak Gust Time	HHMM (local time)	Time of the strongest wind gust
8. PRCP	Precipitation	tenths of mm	Daily total precipitation
9. RHAV	Relative Humidity - Average%	%	Daily average relative humidity
10. RHMN	Relative Humidity - Minimum%	%	Minimum relative humidity observed
11. RHMX	Relative Humidity - Maximum%	Maximum relative humidity observed
12. SNOW	Snowfall	mm or tenths of mm	Daily snowfall total
13. SNWD	Snow Depth	mm	Depth of snow on ground
14. TMAX	Maximum Temperature	tenths of °C	Highest temperature of the day
15. TMIN	Minimum Temperature	tenths of °C	Lowest temperature of the day
16. WDF2	Wind Direction (2-min)	degrees (0–360)	Direction of fastest 2-minute wind
17. WDF5	Wind Direction (5-min)	degrees (0–360)	Direction of fastest 5-minute wind
18. WSF2	Wind Speed (2-min)	tenths of m/s	Fastest 2-minute sustained wind speed
19. WSF5	Wind Speed (5-min)	tenths of m/s	Fastest 5-minute sustained wind speed
20. WT01	Weather Type: Fog / Ice Fog / Freezing Fog	Binary (0 or 1)	1 = Event occurred
21. WT02	Weather Type: Heavy Fog	Binary	1 = Visibility < 1/4 mile
22. WT03	Weather Type: Thunderstorm	Binary	1 = Thunderstorm occurred
23. WT06	Weather Type: Hail	Binary	1 = Hail occurred
24. WT08	Weather Type: Smoke / Haze	Binary	1 = Smoke/haze observed


📊 Project Highlights
Dashboard -->	Focus Area
1. Temperature Trends	--> TMAX, TMIN, AWBT over time
2. Rainfall vs Snowfall	--> PRCP and SNOW comparison
3. Wind Rose Chart	--> WDF and WSF patterns
4. Humidity Lines	--> RHMX, RHAV, RHMN
5. Discomfort Index	--> Heat-Humidity Stress
6. Snowfall vs Depth	--> Dual-axis analysis
7. Weather Events	--> WT01-WT08 Frequency
8. Seasonal Heatmap	--> PRCP & TMAX by calendar
9. Correlation Plot	--> TMAX vs PRCP insights
10. KPI Summary	--> Overview metrics and icons

🧰 Tools & Techniques Used
1. Category	--> Tools/Technologies
2. Programming	--> Python (requests, json, pandas)
3. Data Source	--> NOAA CDO API
4. API Integration	--> NOAA Climate Data Online (CDO)
5. Environment --> Setup	VS Code, virtualenv, .env token file
6. Data Processing	--> Excel, Python, CSV manipulation
7. Visualization	--> Tableau Desktop
8. Calculated Metrics --> Discomfort Index, Wind Categories, Humidity Ranges
9. Design Techniques	--> Dual-axis charts, Polar plots, Heatmaps, KPIs

📌 Conclusion

This project demonstrates how public climate data can be transformed into actionable, real-time visual insights with the right combination of programming, data cleaning, and dashboard design. The resulting Tableau dashboards serve not only as analytical tools but also as communication assets, bridging the gap between data science and public awareness.


📎 Future Work

1. Automate live dashboard refresh using Tableau Public APIs or Tableau Bridge
2. Expand to multi-city comparisons
3. Integrate forecasting models using NOAA’s forecast endpoints or ML

Few Example Dashboards:

<img width="1470" height="847" alt="Pasted Graphic 11" src="https://github.com/user-attachments/assets/a3ed550e-90b7-42f8-8150-0f34ce1bcbc5" />
<img width="1470" height="847" alt="Pasted Graphic 14" src="https://github.com/user-attachments/assets/0d18c843-904b-49fd-8d25-13ba6036461e" />
<img width="1470" height="847" alt="Pasted Graphic 17" src="https://github.com/user-attachments/assets/4119b069-17df-483d-90dd-6765d2e2c6db" />
