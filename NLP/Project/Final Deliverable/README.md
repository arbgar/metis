![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Header.png?raw=true)

 *Photo created with [The GDELT Project](https://www.gdeltproject.org/)*

# Climate Change around the World

In 2015 World Leaders came together at the [COP21 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/Paris_Agreement) in Paris France. From this conference came the Paris Agreement, also known as the Paris Accord and Paris Climate Accord. The Agreement set goals to minimize the rise in global temperature as well as emissions reductions. 196 parties signed on to the Agreement. Recently World Leaders reconvened at the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland. The meeting comes as expected results have not been achieved and commitments are wavering.

## Design

This project reviewed world news coverage surrounding the 2021 United Nations Climate Change Conference to better understand world opinions about this shared challenge. In doing so, the analysis identified key topics by country and geographic sub-region. Subsequent analysis assessed the subjectivity, and polarity associated with those topics. The analysis helps scope the challenges in and commitment to resolving climate change issues. The preliminary outcomes of the analysis yield an understanding of world opinion and commitment to climate change for an organization such as the [United Nations Dag Hammarskjöld Library](https://www.un.org/en/library). Final post-conference analysis could then yield a report that United Nations Committees use to help address the crisis through world opinion.

## Data

I chose the [GDELT Project](https://www.gdeltproject.org/) for the news dataset. I leveraged their API to scrape 55,614 articles two months before and one week after the start of the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland. I keyed on the term **COP26** which was easy to find regardless of article origin. The data included the news article headline, URL, country of origin, language, and date / time. Using Google Translate, I converted the information to English.

From that information I began scraping the individual new articles from the source websites. This proved to be very time consuming as many websites refused the connection or took a long time to respond so I opted to do the analysis from the headlines as characterized below.  

<img src="https://github.com/arbgar/metis/blob/main/NLP/Project/Final%20Deliverable/world.png?raw=true" style="zoom: 50%;" />

To simplify the graphics, I mapped countries into the [United Nations designated Sub-Regions](https://unstats.un.org/unsd/methodology/m49/overview/).

<img src="https://github.com/arbgar/metis/blob/main/NLP/Project/Final%20Deliverable/articles.png?raw=true" style="zoom: 67%;" />

## Algorithms

The news  headlines were relatively easy to analyze with standard Natural Language Processing (NLP) techniques.  The initial selection of CoreVectorizer / LDA Model did not yield good results as this information is more similar to tweets.  Changing to a TfidVectorizer / NMF Model yielded much better results.  After getting initial results, iteration with a CorEx Model confirmed anchors and yielded the final 20 topics. With this information, the results were easily visualized with Tableau through an Excel dataset.

In addition to this model iteration, I iterated on data cleaning.  There were many sensational articles among the hard news about climate change.  I found that pre-cleaning the Excel dataset to remove the terms Glasgow, COP26, and world leaders' names reduced the importance of the trivial news headlines and surfaced the core climate change topics without pre-seeding the anchors.  In the end, the NMF Model results were most relevant and are the basis for the final report and visualization. 

Interestingly, the NMF Model quickly identified the non-English topics that the translator missed and dumped them in their own topic.  This made it easy to weed them out after verifying the topics were similar to the existing topics. A final analysis would assure that all headlines were properly translated and counted in the results.

I did attempt to lemmatize the code, but it was taking a long time without significant value add. 

![](https://github.com/arbgar/metis/blob/main/NLP/Project/Final%20Deliverable/Algorithms.png?raw=true)

## Tools

- [GDELT API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) for news headline collection
- Selenium / Beautiful Soup to scrape the resulting html 
- [Google Translate Widget](https://developers.google.com/search/blog/2020/05/google-translates-website-translator) to translate the articles to English as needed
- Excel for dataset joining, pre-cleaning, and support to final visualization using Pivot and Lookup 
- Pandas and Numpy for analysis
- RegEx for final cleaning 
- Textblob for sentiment analysis
- scikit-learn TfidVectorizer for tokenization and  English stopword removal
- scikit-learn Non-negative Matrix Factorization Model and CorEx Topic Modeler for topic modeling
- Tableau for NLP visualization:
  -  [World Map of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/nlp_map/Dashboard1)
  - [Characterization of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/nlp_articles/Dashboard1)
  - [Positive / Negative Sentiment of News Headlines](https://public.tableau.com/app/profile/alison.garrett/viz/nlp_polarity_time/Dashboard1)
  - [Top Topics by Sub-Region with Sentiment](https://public.tableau.com/app/profile/alison.garrett/viz/nlp_region_topic_polarity/Dashboard1)

## Communication

The *Climate Change around the World* presentation summarizes the findings in graphical format including the following key elements:

- **COP26 United Nations Climate Change Conference ** which introduces the climate change challenge
- **Understanding World Opinion** which introduces the purpose of the report
- **The GDELT Project: Worldwide News Feed** which overviews the news source and dataset
- **Headlines More Positive** shows overall news headline polarity two months prior and 1 week after the start of the conference
- **Regional Topics** which samples top topics by sub-region including polarity
- **Next Steps** which overviews finalizing the analysis and preparing a final report post conference

The presentation is targeted as a quick look for United Nations committees who want to understand world opinion based on news headlines. The final report would be used to support UN committee action.
