![](https://github.com/arbgar/metis/blob/main/NLP/Project/Deliverable/Header.png?raw=true)

​															      														*Photo created with [The GDELT Project](https://www.gdeltproject.org/)*

# Climate Change around the World

To begin this project I improved the previously developed collection, translation, region mapping, storage, and modeling of the  [GDELT Project](https://www.gdeltproject.org) dataset associated with the [COP26 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2021_United_Nations_Climate_Change_Conference) in Glasgow Scotland.  The data included the news article title, URL, country of origin, language, and date / time.  

The new workflow shown in the following figure can run as two separate python applications without intermediate operator interaction.  The results are now in a three table SQLite database:

- **Headlines** (native language and English translation), source, date_time, country, subjectivity and polarity
- **Region_Country** mapping per the United Nations
- **Topics** with the topic mapped to the Headline

![](https://github.com/arbgar/metis/blob/main/Engineering/Project/Deliverable/workflow.png?raw=true)

What remains is to develop the Streamlit app to receive user input and update the visualization based on user input. The apps are designed to update automatically, but the database will need to be cloud hosted to do that.  I will include that step if I have time.
