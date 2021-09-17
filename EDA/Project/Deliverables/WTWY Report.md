![](https://github.com/arbgar/metis/blob/main/EDA/Project/WDA_logo.png)

# Maximizing WTWY Registration

## Engaging Technology Oriented Academia 

This fall WTWY is engaging New Yorkers to introduce their women in technology programs. WTWY deployed street teams to the busiest subway stations to introduce WTWY and register those who are interested.

Early returns from this canvasing are promising, however WTWY observed low engagement with NYC colleges and universities. Because students and professors foster creative energy, WTWY asked WDA to assess the results to date and refine the street team deployment to improve college and university engagement.

This project analyzes publicly available NYC datasets including [Colleges](https://www.ny.com/academia/colleges.html), [Station Locations](https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56), and [Turnstiles](http://web.mta.info/developers/turnstile.html) to assess street team deployment and provide refinement recommendations.

## Design

Central to this analysis is identification of technology oriented colleges and universities located in NYC. By assessing the impact of the college and university along with their location relative to the MTA subway stations, we identify target subway stations for canvassing.  After comparing these targets to the list of busiest subway station, we identify additional high traffic stations with a college and university population .

## Data

This project is based on the following datasets:

Summer 2021 Turnstile: 

## Algorithms

*Current Street Team Deployment:* This analysis uses MTA Turnstile data to identify the high traffic stations during the summer of 2021.  Traffic is defined as the total Entries and Exits at each Station.

*College and University Locations:*  Based on the US News & World College report, the NYC College and University dataset is tagged for Technology as follows:

- Lead: Technology focus and impact, and
- Yes: Technology focus.

Institutions that Lead in Technology are then mapped to the nearest MTA subway station using Latitude / Longitude.

*Refined Street Team Deployment:* This analysis uses MTA Turnstile data to identify the daily Traffic at the college and university locations during Fall 2018.  This pre-covid dataset will most resemble the Fall 2021Traffic as we return to inperson learning and activities.  From this analysis WDA selected the three university stations with the highest traffic, not already in the current street team deployment.  By segmenting the traffic at these stations into day of the week and four hour shift, WDA recommended station, day, and time windows for added street team deployment. 

## Tools

- SQLite, SQLAlchemy and DB Browser for database creation and query
- Numpy and Pandas for data cleaning and manipulation 
- Matplotlib and Seaborn for plotting

## Communication

The WTWY presentation summarizes the findings in graphical form identifying,

- Current street team deployment engagement with colleges and universities,
- Recommendations, including day and time, for three additional stations to capture the Columbia University, NYU Polytechnic Institute, and NYC City Techn populations, and
- Options for additional deployment subway stations, days, and times should WTWY have added street teams for college and university engagement.
