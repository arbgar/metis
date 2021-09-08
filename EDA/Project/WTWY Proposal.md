![](https://github.com/arbgar/metis/blob/main/EDA/Project/WDA_logo.png)

# Introduction:

***Women in Data Analysis*** **(WDA)** is pleased to present this data analytics proposal to **WomenTechWomenYes (WTWY) . **The WTWY objective is to introduce their new and inclusive organization by engaging New Yorkers as they pass through the New York City (NYC) Metropolitan Transit Authority (MTA) subway system.  WTWY has a street team dedicated to this engagement.  The street team's objective is to,

- Introduce the organization and its programs,
- Identify those who may be interested in increasing women in technology, 
- Collect contact information and signatures of program support from those who register their interest with WTWY,
- Extend invitations to the summer gala by emailing free tickets to the registrants, 
- Solicit funds to support the WTWY programs, and 
- Build awareness and outreach channels.

WTWY engaged WDA to optimize the placement of the WTWY street team in service of these objectives.

# Question:

The core question we will attempt to answer is, 

- What is the best deployment of the WTWY street team to NYC MTA subway stations to maximize the the number of people who register with WTWY?

Since WYWT is assuming that maximizing the number of registrants will maximize the number of people who will (1) be interested in the WYWT programs, (2) attend the gala and (3) contribute to the cause, secondary questions include,

- Are those who register interested in women in technology?
- Are those who register likely to attend the gala?
- Are those who register likely to contribute to the cause?

The following contributors will be factored into answering these questions:

- Which NYC MTA subway stations have the most traffic?
  - Day of the week,
  - Time of day, and
  - Inbound / outbound.

- Which NYC MTA subway station boroughs have commuters with these characteristics?
  - Technology,
  - Women empowerment,
  - Affluence / Philanthropy , and
  - Societal traditions.

Answering these questions will help WTWY optimize the deployment of the WYWT street team to maximize registrants to meet objectives.

# Data Description:

The core dataset in this analysis is the NYC MTA turnstile data.  This data and supporting information is available to the public at http://web.mta.info/developers/turnstile.html. Once we have this dataset, we will assess the traffic per station based on the day and time by aggregating the turnstile information per station including the inbound / outbound data characteristics. This provides an initial target list uninformed by the station borough characteristics.

Based on this initial information we will pull NYC borough datasets from public sources such as,

- Subway Entrances (https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56)
- NYC Census Data (https://www.census.gov/quickfacts/newyorkcitynewyork)
- NYC Open Data (https://opendata.cityofnewyork.us)

By looking for individual, business, and educational institution datasets which can be cross referenced by borough with subway stations we can refine the assessment by considering subway stations which may have commuters more interested in women in technology and philanthropy.

# Tools:

As many of these datasets are large, we will ingest the raw datasets into an SQL database. Working in DB Browser, we will select, clean, and summarize the data into manageable datasets.  Subsequent assessment and refinement using Python via SQLAlchemy and pandas will leverage many of the standard SQL commands, particularly across tables based on borough. Finally the data will be visualized through Matplotlib for presentation in PowerPoint and written description in markdown.

# MVP Objective:

WDA will provide a Minimum Viable Product (MVP) prior to the Final Presentation / Written Description to provide a directional assessment confirming the questions based on the available data.  The MVP will provide an initial analysis of the MTA turnstile data to identify which NYC MTA subway stations have the most traffic. The MVP will also provide an initial assessment of subway station borough datasets and how they may refine the straight commuter traffic based assessment.