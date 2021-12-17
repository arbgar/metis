![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Header.png?raw=true)

 *Photo created with [The GDELT Project](https://www.gdeltproject.org/)*

# Climate Change around the World

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) in Paris France. From this conference came the Paris Agreement, also known as the Paris Accord and Paris Climate Accord. The Agreement set goals to minimize the rise in global temperature as well as emissions reductions. 196 parties signed on to the Agreement. Recently World Leaders reconvened at the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland. The meeting comes as expected results have not been achieved and commitments are wavering.

## Design

This project reviewed world news coverage surrounding the 2021 United Nations Climate Change Conference to better understand world opinions about this shared challenge. In doing so, the analysis identified key topics by country and geographic region. Subsequent analysis assessed the subjectivity, and polarity associated with those topics. The analysis helps scope the challenges in and commitment to resolving climate change issues. The outcomes of the analysis yield an understanding of world opinion and commitment to climate change for an organization such as the [United Nations Dag Hammarskjöld Library](https://www.un.org/en/library). The resulting **COP26 Headline Analyzer** is a tool that United Nations Committees could use to help understand the crisis through world opinion.

## Data

I chose the [GDELT Project](https://www.gdeltproject.org/) for the news dataset. I leveraged their API to scrape 109,390 headlines during September, October, and November around the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference), 30 October - 12 November, 2021 in Glasgow Scotland. I keyed on the term **COP26** which was easy to find regardless of article origin. The data included the news article headline, URL, country of origin, language, and date / time. Using Google Translate, I converted the information to English. To simplify the graphics, I mapped countries into the [United Nations designated Regions and Developed / Developing Classification](https://unstats.un.org/unsd/methodology/m49/overview/).

## Algorithms

The news  headlines were relatively easy to analyze with standard Natural Language Processing (NLP) techniques with a TfidVectorizer and NMF Model to select the top 20 topics. There were many sensational articles among the hard news about climate change.  I found that pre-cleaning the data to remove the terms Glasgow, COP26, and world leaders' names reduced the importance of the trivial news headlines and surfaced the core climate change topics without pre-seeding the anchors.   

## Tools

- [GDELT API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) for news headline collection
- Beautiful Soup to scrape the resulting html 
- Google Translate to translate the articles to English as needed
- SQLite SQLAlchemy and DB Browser for all datasets  
- Pandas and Numpy for analysis
- RegEx for final cleaning 
- Textblob for sentiment analysis
- scikit-learn TfidVectorizer for tokenization and  English stopword removal
- scikit-learn Non-negative Matrix Factorization Model for topic modeling
- Streamlit for web application presentation
- Tableau for NLP visualization:
  -  [World Map of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/nlp_map/Dashboard1)
  - [Characterization of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/de_headlines/Dashboard1)
  - [Positive / Negative Sentiment of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/de_headlines/Dashboard2#2)
  - [Top Topics by Region with Sentiment](https://public.tableau.com/app/profile/alison.garrett/viz/de_local/Dashboard1)

## Communication

The *Climate Change around the World* presentation summarizes the findings in graphical format including the following key elements:

- **COP26 United Nations Climate Change Conference** which introduces the climate change challenge
- **Understanding World Opinion** which introduces the purpose of the report
- **The GDELT Project: Worldwide News Feed** which overviews the news source and dataset
- **COP26 Headline Analyzer** which is a video of the web application in use
- **Headlines More Positive** shows overall news headline polarity two months prior and 1 week after the start of the conference
- **Regional Topics** which samples top topics by sub-region including polarity
- **Next Steps** which overviews finalizing the analysis and preparing a final report post conference

The presentation is targeted as a quick look for United Nations committees who want to understand world opinion based on news headlines. The COP26 Headline Analyzer tool would be used to support UN committee action.
