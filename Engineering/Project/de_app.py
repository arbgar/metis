"""
Make sure to install streamlit with `pip install streamlit`.

To run this app:

1. cd into this directory
2. pipenv shell
3. Requirements.txt in directory
4. Run `streamlit run de_app.py`
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sqlalchemy  import create_engine

# HEADER

st.image("https://raw.githubusercontent.com/arbgar/metis/main/NLP/Project/Deliverable/Header.png",
	width=700,
        )

st.write('''
*Photo created with [The GDELT Project](https://www.gdeltproject.org/)*


# Climate Change around the World

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) in Paris France.  From this conference came the Paris Agreement, also known as the Paris Accord and Paris Climate Accord.  The Agreement set goals to minimize the rise in global temperature as well as emissions reductions.  196 parties signed on to the Agreement.  Recently World Leaders reconvened at the [COP26  United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland.  The meeting comes as expected results have not been achieved and commitments are wavering.  

This project reviews world news coverage surrounding the 2021 United Nations Climate Change Conference to better understand world opinions about this shared challenge. In doing so, the analysis identifies key topics by country and geographic sub-region. Subsequent analysis assessed the subjectivity, and polarity associated with those topics. The analysis helps scope the challenges in and commitment to resolving climate change issues. The outcomes yield an understanding of world opinion and commitment to climate change for an organization such as the [United Nations Dag Hammarskjöld Library](https://www.un.org/en/library). 
''')

# CONNECT DATABASE: COUNTRIES AND MAP COUNTRIES

# engine       = create_engine("sqlite:///Documents/GitHub/metis/Engineering/Project/hl.db")

# locations = pd.read_sql('SELECT DISTINCT lat, lon FROM headlines LEFT JOIN region_country ON country=CountryorArea',con = engine)

# locations['lat'] = locations['lat'].astype(float) 
# locations['lon'] = locations['lon'].astype(float) 

# st.dataframe(locations) 
    
# st.map(locations.loc[:,['lat','lon']],zoom(3))

	# CONNECT DATABASE: REGIONS AND PLOT ARTICLE QUANTITY

try:
	engine       = create_engine("sqlite:///Documents/GitHub/metis/Engineering/Project/hl.db")

	regions = pd.read_sql("SELECT RegionName, country, COUNT(arttitle) FROM headlines LEFT JOIN region_country ON country=CountryorArea GROUP BY RegionName, country",con = engine)

	regions.rename(columns={'RegionName': 'Region', 'country': 'Country', 'COUNT(arttitle)': 'Article Count'}, inplace=True)
except:
	st.write('db read')

try:
	st.sidebar.write('Which Region would you like to analyze?')
	region = st.sidebar.radio('',('Africa', 'Americas', 'Asia', 'Europe', 'Oceania'))

	st.sidebar.write('Countries within the Region:')

	st.sidebar.dataframe(regions.loc[regions['Region']==region][['Country']],225)
except:
	st.write('sidebar')
	
# CONNECT DATABASE: REGIONS AND PLOT ARTICLES, SENTIMENT, and SUBJECTIVITY OVER TIME

try:

	sentiment = pd.read_sql("SELECT RegionName, COUNT(arttitle), SUBSTRING(date_time,1,8) AS Date, AVG(sentiment), AVG(polarity) FROM headlines LEFT JOIN region_country ON country=CountryorArea GROUP BY RegionName, Date",con = engine)

	sentiment.rename(columns={'RegionName': 'Region', 'COUNT(arttitle)': 'Article Count','AVG(sentiment)': 'Subjectivity', 'AVG(polarity)':'Polarity'}, inplace=True)
except:
	st.write('db read 2')

try:
	st.write('### Article Count Sep - Nov 2021, COP26 (30 Oct - 12 Nov 2021)')
	st.line_chart(sentiment.loc[sentiment['Region']==region][['Article Count']])

	st.write('### Subjective and Polarity Sep - Nov 2021, COP26 (30 Oct - 12 Nov 2021)')
	st.write('Subjectivity 0: Objective, 1: Subjective')
	st.write('Polarity -1: Negative, 1 Positive')
	st.line_chart(sentiment.loc[sentiment['Region']==region][['Subjectivity', 'Polarity']])
except:
	st.wrte('plots')
# PART 2

# st.write(
# '''
# You can use markdown syntax to style your text

# Headers:
# # Main Title 
# ## Sub Title 
# ### header 

# **bold text**

# *italics*

# Ordered List

# 1. Apples 
# 2. Oranges 
# 3. Bananas 

# [This is a link](https://docs.streamlit.io/en/stable/getting_started.html)


# '''
# )

# PART 3

# st.write(
# '''
# ## Seattle Home Prices
# We can import data into our streamlit app using pandas read_csv then display the resulting dataframe with st.dataframe()

# ''')

# data = pd.read_csv('SeattleHomePrices.csv')
# data = data.rename(columns={'LATITUDE': 'lat', 'LONGITUDE': 'lon'})
# st.dataframe(data)

# PART 4

# st.write(
# '''
# ### Graphing and Buttons
# Lets graph some of our data with matplotlib. We can also add buttons to add interactivity to our app.
# '''
# )

# fig, ax = plt.subplots()

# ax.hist(data['PRICE'])
# ax.set_title('Distribution of House Prices in $100,000s')

# show_graph = st.checkbox('Show Graph', value=True)

# if show_graph:
#     st.pyplot(fig)

# PART 5
    
# st.write(
# '''
# ### Mapping and Filtering Our Data
# We can also use streamlits built in mapping functionality.
# We can use a slider to filter for houses within a particular price range as well.
# '''
# )

# price_input = st.slider('House Price Filter', int(data['PRICE'].min()), int(data['PRICE'].max()), 100000 )

# price_filter = data['PRICE'] < price_input
# st.map(data.loc[price_filter, ['lat', 'lon']])



