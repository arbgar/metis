![](https://github.com/arbgar/metis/blob/main/NLP/Deliverable/nlp_picture.png?raw=true)

​															      								*Photo by [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) and [Utsav Srestha](https://unsplash.com/@utsavsrestha?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash*

# Climate Change around the World

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) in Paris France.  From this conference came the Paris Agreement, also known as the Paris Accord and Paris Climate Accord.  The Agreement set goals to minimize the rise in global temperature as well as emissions reductions.  196 parties signed on to the Agreement.  Recently World Leaders reconvened at the [COP26  United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland.  The meeting comes as expected results have not been achieved and commitments are wavering.  

# Analysis

This project will review world news coverage surrounding the 2021 United Nations Climate Change Conference to better understand world opinions about this shared challenge.  In doing so, the analysis will identify key topics by country or geographic region.  Subsequent analysis will assess the sentiment associated with those topics.  This analysis will help to scope the challenges in and commitment to resolving climate change issues.  The outcome of the analysis will yield recommendations to foreign service officials and lawmakers.

# Data Description

This project will use the [GDELT Project](https://www.gdeltproject.org) to access news from around the world.  Should the dataset not be suited to this analysis, the project will leverage the [Google News API](https://developers.google.com/news-search/) and the [Bing News API](https://english.api.rakuten.net/microsoft-azure/api/bing-news-search).  The objective is to identify 1000 news articles or news summaries of 100 words or more.

# Tools

The analysis will be completed in Jupyter Notebook / Python using Pandas.  Natural Language Processing  will use scikit-learn CountVectorizer or TfidfVectorizer to pre-process the text, NMF or LDA for topic modeling, and K-means for clustering.  Visualization will be via Matplotlib, Seaborn, and Tableau. 

# MVP Objective

The MVP will present an initial pre-processed news dataset with topics.  

