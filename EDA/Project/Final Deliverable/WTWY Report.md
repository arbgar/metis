![](https://github.com/arbgar/metis/blob/main/EDA/Project/WDA_logo.png)

# Maximizing WTWY Registration

## Engaging Technology Oriented Academia 

This fall WTWY is engaging New Yorkers to introduce their women in technology programs. WTWY deployed street teams to the busiest subway stations to introduce WTWY and register those who are interested.

Early returns from this canvasing are promising, however WTWY observed low engagement with NYC colleges and universities. Because students and professors foster creative energy, WTWY asked WDA to assess the results to date and refine the street team deployment to improve college and university engagement.

This project analyzes publicly available NYC datasets including [Colleges](https://www.ny.com/academia/colleges.html), [Station Locations](https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56), and [Turnstiles](http://web.mta.info/developers/turnstile.html) to assess street team deployment and provide refinement recommendations.

## Design

Central to this analysis is identification of technology oriented colleges and universities located in NYC. By assessing the impact of the college and university along with their location relative to the MTA subway stations, we identify target subway stations for canvasing.  After comparing these targets to the list of busiest subway stations, we identify additional high traffic stations with a college and university population.

## Data

*Fall 2018 MTA Turnstile Dataset:* 2.78M rows of MTA Turnstile data from 08/25/2018 through 11/30/2018. 14 columns uniquely identifying the turnstiles per station, audit date and time, entry and exit counts, and historical line references used to support location identification and linkages.

*Summer 2021 MTA Turnstile Dataset:* 2.93M rows of MTA Turnstile data from 05/29/2021 through 09/04/2021. 14 columns uniquely identifying the turnstiles per station, audit date and time, entry and exit counts, and historical line references used to support location identification and linkages.

*NYC Colleges and Universities Dataset:* 77 rows of college and university information, one row per institution.  12 columns consisting of name, address, latitude and longitude, url, and city building / lot designators.  This dataset was augmented with the Technology flag to designate institution technology impact.

*NYC MTA Station Location Dataset:* 1866 rows of unique NYC MTA station location including 30 columns of data including station information, latitude and longitude of entrances used to link to the university, route and line numbers, various descriptive characteristics, and historical reference information

## Algorithms

*Current Street Team Deployment:* This analysis uses MTA Turnstile data to identify the high traffic stations during the summer of 2021.  Traffic is defined as the total Entries and Exits at each Station.

*College and University Locations:*  Based on the US News & World College report, the NYC College and University dataset is tagged for Technology as follows:

- Lead: Technology focus and impact, and
- Yes: Technology focus.

Institutions that Lead in Technology are then mapped to the nearest MTA subway station using Latitude / Longitude.

*Refined Street Team Deployment:* This analysis uses MTA Turnstile data to identify the daily Traffic at the college and university locations during Fall 2018.  This pre-covid dataset will most resemble the Fall 2021 Traffic as we return to inperson learning and activities.  From this analysis WDA selected the three university stations with the highest traffic, not already in the current street team deployment.  By segmenting the traffic at these stations into day of the week and four hour shifts, WDA recommended station, day, and time windows for added street team deployment. 

## Tools

- SQLite, SQLAlchemy and DB Browser for database creation and query
- Numpy and Pandas for data cleaning and manipulation 
- Matplotlib and Seaborn for plotting
- Excel pivot and lookup for minor data tagging and station name mapping

## Communication

The WTWY presentation summarizes the findings in graphical format identifying,

- Current street team deployment engagement with colleges and universities;
- Recommendations, including day and time, for three additional stations to capture the Columbia University, NYU Polytechnic Institute, and NYC City Techn populations; and
- Options for additional deployment subway stations, days, and times should WTWY want added street teams for college and university engagement.
