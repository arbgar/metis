![](https://github.com/arbgar/metis/blob/main/EDA/Project/WDA_logo.png)

# Maximizing WTWY Registration

The core question we are attempting to answer is the best deployment of the WTWY street team to NYC MTA subway stations to maximize the number of people who register with the WTWY.  Secondary questions include maximizing the registrants who will (1) be interested in the WYWT programs, (2) attend the gala and (3) contribute to the cause.

To begin to explore these questions, we assessed over 3 months of NYC MTA subway data to determine the daily station entrance and exit traffic.  The process for this exploration was as follows:

- Import url datasets into Jupyter notebook pandas.
- Added column DATE_TIME / datetime64[ns] datatype.
- Exported raw data to csv.
- Imported csv data into a database using sqlite.
- Brought database into pandas dataframe.
- Explored database using DB Browser, SQL Alchemy.
- Explored dataframe using pandas.
- Selected REGULAR data as cleaning approach will handle audit anomalies.
- Calculated the MEAN / STD ENTRIES / EXITS for each unique SCP; noted turnstiles get reset periodically.
- Dropped turnstile data outside a STD; noted that some of the larger stations may have lost fidelity because of the turnstile resets. 
- Dropped 11 rows of remaining anomalies.
- For each unique SCP by DATE, calculated added TRAFFIC per audit and established the TRAFFIC per DATE.
- Validated data using DB Browser and outlier masking.
- Selected a two month dataset, 19 June - 13 August 2021.

After cleaning the data and selecting a representative two month dataset, we found the top 25 stations as shown below.

![](https://github.com/arbgar/metis/blob/main/EDA/Project/top_25.png)



Subsequently we assessed each top station by date and time as well as station entrance location to identify target days, times, and locations for the street team as shown below.

![](https://github.com/arbgar/metis/blob/main/EDA/Project/penn_entrance.png)

![](https://github.com/arbgar/metis/blob/main/EDA/Project/penn_date.png)

As some of these locations could, by themselves, overwhelm the WYWT street team resources, we have investigated added factors to refine these targets.  We have found that technology oriented university and corporation populations may be most interested in the WYTY programs. Our upcoming work will refine these targets by considering these available datasets:

NYC Subway Entrances: (https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56)

NYC Universities:

https://www.ny.com/academia/colleges.html

https://www.usnews.com/best-colleges/search?_sort=distance&_sortDirection=asc&location=New+York%2C+NY&distance=50&study=Engineering&_mode=table

NYC Corporations:

https://data.cityofnewyork.us/browse?limitTo=datasets&q=corporations&sortBy=relevance

https://en.wikipedia.org/wiki/List_of_companies_based_in_New_York_City

https://en.wikipedia.org/wiki/List_of_tech_companies_in_the_New_York_metropolitan_area

https://en.wikipedia.org/wiki/List_of_New_York_companies

## Open Approach / Tool Questions

1. Address Station / Line / Entrance location approach
2. Review sufficiency of cleaning methodology for purpose
3. Resolve warnings:
   - SettingWithCopyWarning: 
     A value is trying to be set on a copy of a slice from a DataFrame.
   - UserWarning: Boolean Series key will be reindexed to match DataFrame index.