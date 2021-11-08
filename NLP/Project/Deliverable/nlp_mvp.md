![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Header.png?raw=true)

​															      															*Photo created with [The GDELT Project](https://www.gdeltproject.org/)*

# Climate Change around the World

To begin this project I researched the [GDELT Project](https://www.gdeltproject.org) ,  [News API](https://newsapi.org) (the new Google News API), and the [Bing News API](https://english.api.rakuten.net/microsoft-azure/api/bing-news-search) datasets with the the objective of identifying 1000 news articles or news summaries of 100 words or more. The News and Bing News APIs had daily data restrictions which made sufficient collection difficult.  The GDELT Project was more open to retrieving large datasets and also provided a more robust collection of world news articles. 

Opting for the GDELT Project database, I leveraged their API to scrape over 1500 article urls over the 2 week period surrounding the start of the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland.  The data included the news article title, url, country of origin, language, and date / time. Using Google Translate, I converted the information to English.

From that information I began scraping the individual new articles from the source websites.  This proved to be very time consuming as many websites refused the connection or took a long time to respond.  After a day of trying, I had under 100 news articles.  

To ensure I have sufficient information to do the project, today I decided to change course and work with the news article titles. Most have good information similar to a tweet.  To make this work I downloaded an additional 2 months of data or about 36,000 articles.  The charts below give an overview of the data.  Overnight I will pick up the full 2 weeks of data, versus the 1000 minimum, at the start of the conference.

Summarizing, my interest in the GDELT data put me a bit behind in starting the NLP work. However, I expect to move quickly now that I have a clean dataset.

![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Country.png?raw=true)



![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Language.png?raw=true)
