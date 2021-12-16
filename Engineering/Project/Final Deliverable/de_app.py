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

st.set_page_config(page_title="COP26 Headline Analyzer", page_icon=None, layout="wide", initial_sidebar_state="auto")

st.image("https://github.com/arbgar/metis/blob/main/Engineering/Project/Final%20Deliverable/COP26.png?raw=true", use_column_width = "always")

st.write('''
*Photo from [COP26](https://ukcop26.org/), data from [The GDELT Project](https://www.gdeltproject.org)*

## Climate Change around the World 

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) 
in Paris France.  196 parties signed on to the Paris Agreement to minimize the rise in global temperature and reduce emissions. Recently 
World Leaders reconvened at the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference), 
30 Oct - 12 Nov 2021, in Glasgow Scotland. This project reviews COP26 world news headlines to gauge world opinion of and commitment to climate change. 
''')

# SIDEBAR SELECTORS AND COLUMN SET_UP

st.sidebar.write('Which Region would you like to analyze?')
region = st.sidebar.radio('',('Africa', 'Americas', 'Asia', 'Europe', 'Oceania'))
	
st.sidebar.write('Developed or Developing countries?')
develop = st.sidebar.radio('',('Developed', 'Developing'))

col1, col2 = st.beta_columns(2)


# CONNECT DATABASE: REGIONS AND ARTICLE QUANTITY BY COUNTRY

engine = create_engine("sqlite:///Documents/GitHub/metis/Engineering/Project/hl.db")

regions = pd.read_sql("SELECT RegionName, Develop, country, COUNT(arttitle) FROM headlines LEFT JOIN region_country ON country=CountryorArea GROUP BY RegionName, country",con = engine)

regions.rename(columns={'RegionName': 'Region', 'country': 'Country', 'COUNT(arttitle)': 'Articles'}, inplace=True)

st.sidebar.write('Countries Selected:')

st.sidebar.dataframe(regions.loc[(regions['Develop']==develop) & (regions['Region']==region)][['Country','Articles']],400)
	
# CONNECT DATABASE: REGIONS AND PLOT ARTICLES, POLARITY, and SUBJECTIVITY OVER TIME

sentiment = pd.read_sql("SELECT RegionName, Develop, COUNT(arttitle), SUBSTRING(date_time,1,8) AS Date, AVG(sentiment), AVG(polarity) FROM headlines LEFT JOIN region_country ON country=CountryorArea GROUP BY RegionName, Date",con = engine)

sentiment.rename(columns={'RegionName': 'Region', 'COUNT(arttitle)': 'Articles','AVG(sentiment)': 'Subjectivity', 'AVG(polarity)':'Polarity'}, inplace=True)

with col1:
	st.write('**Number of News Articles (Sep - Nov 2021)**')
	st.line_chart(sentiment.loc[(sentiment['Region']==region) & (sentiment['Develop']==develop)][['Articles']])

with col2:
	st.write('**Subjectivity and Polarity of Headlines (Sep - Nov 2021)**')
	st.line_chart(sentiment.loc[(sentiment['Region']==region) & (sentiment['Develop']==develop)][['Subjectivity', 'Polarity']])
	st.write('**Subjectivity** 0: Objective, 1: Subjective **Polarity** -1: Negative, 1 Positive')

# CONNECT DATABASE: TOP TOPICS BY COUNTRY

top_topics = pd.read_sql("SELECT RegionName, Develop, country, Topic, COUNT(Topic) FROM topics LEFT JOIN region_country ON country=CountryorArea GROUP BY RegionName, country, Topic",con = engine)

top_topics.rename(columns={'RegionName': 'Region', 'country': 'Country', 'COUNT(Topic)': 'Count'}, inplace=True)
top_topics.sort_values(by = ['Country','Count'], ascending = False, inplace = True)
top_five = top_topics.groupby('Country').head(5)
top_five.sort_values(by = ['Country'], inplace = True)

st.write('**Top Five News Headline Topics by Country**')
st.table(top_five.loc[(top_five['Region']==region) & (top_five['Develop']==develop)][['Country', 'Topic']])




