![](https://raw.githubusercontent.com/arbgar/metis/main/NLP/Project/Deliverable/Header.png)

*Photo created with [The GDELT Project](https://www.gdeltproject.org/)*

# Climate Change around the World

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) in Paris France.  From this conference came the Paris Agreement, also known as the Paris Accord and Paris Climate Accord.  The Agreement set goals to minimize the rise in global temperature as well as emissions reductions.  196 parties signed on to the Agreement.  Recently World Leaders reconvened at the [COP26  United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland.  The meeting comes as expected results have not been achieved and commitments are wavering.  

# Analysis

This project will revisit the [Climate Change around the World Natural Language Processing](https://github.com/arbgar/metis/blob/main/NLP/Project/Final%20Deliverable/README.md) analysis which reviewed world news coverage surrounding the 2021 United Nations Climate Change Conference to better understand world opinions about this shared challenge. In doing so, the analysis identified key topics by country and geographic sub-region. Subsequent analysis assessed the subjectivity, and polarity associated with those topics. The analysis helped scope the challenges in and commitment to resolving climate change issues. The preliminary outcomes of the analysis yielded an understanding of world opinion and commitment to climate change for an organization such as the [United Nations Dag Hammarskjöld Library](https://www.un.org/en/library). 

Final post-conference analysis will extend the previous modeling to provide a user facing web application that United Nations Committees could use to help address the crisis through world opinion. The project will extend the previous modeling as follows:

- Collect final, post-conference news headlines,
- Include a pipeline to collect headlines daily and reflect an updated analysis,
- Improve translation of non-English headlines,
- Consider clustering to identify deeper trends, 
- Consider time series aspects to identify deeper trends, and
- Represent the analysis on a user facing web application allowing parameter selection and display of resulting analysis.

# Data Description

This project will use the [GDELT Project](https://www.gdeltproject.org) to access news from around the world. It will leverage their API to add to the 55,614 articles two months before and one week after the start of the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland to obtain over 100,000 articles. Initially keying on the term **COP26** which made it easy to find related articles regardless of article origin, I may need to extend the search criteria to get ongoing reporting on climate change. 

The data includes the news article headline, URL, country of origin, language, and date / time. Using Google Translate, I will convert the information to English.

# Tools

The previous toolset will be updated for pipeline processing and web deployment to include MongoDB or SQLite and Flask or Streamlit on Heroku.  I don't believe the dataset will require big data tools such as cloud processing or Spark but that will be evaluated by the MVP.

# MVP Objective

The MVP will rehost the existing project in a pipeline with web analysis.  Refined modeling will be considered for the final deliverable as time permits.  

