![](https://github.com/arbgar/metis/blob/main/Classification/Project/Final%20Deliverable/Bridge.png?raw=true)

*Photo by* *[Wikimedia Commons / Haha169](https://commons.wikimedia.org/wiki/File:San_Francisco_Oakland_Bay_Bridge_Western_Span.jpg)*

# Saving our Nation's Bridges

The American Road & Transportation Builders Association (ARTBA) reported that, *[There are 171.5 million daily crossings on over 45,000 structurally deficient U.S. bridges in poor condition.](https://artbabridgereport.org/about)*  The Bridge Condition rating of Poor, Fair, and Good is based on four discrete bridge component condition observations: 

- Deck, 
- Superstructure
- Substructure, and
- Culvert.

The government classifies a bridge that is in Poor Condition as a bridge that is **Structurally Deficient**. 

Fortunately, ARTBA and others have gained the attention of lawmakers who are earmarking $3.265B for a 5-year Bridge Reinvestment Program under the proposed Infrastructure Investment and Jobs Act. While this is significant funding, it is likely insufficient to address current deficiencies, let alone the deficiencies that are developing in Bridges in Fair Condition.

This project developed a Bridge Condition Model which classifies National Highway System (NHS) Bridges by their features and provides a probability of Structural Deficiency in an individual NHS Bridge.  With this information, organizations such as the American Society for Civil Engineers can augment the existing Inspection based assessments with analysis predicting Structural Deficiency.  This added information will help prioritize Bridge renovation, repair and replacement as well as make the case for additional infrastructure investment.

## Design

 

## Data

The Federal government has a [National Bridge Inventory (NBI)](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) which is updated annually by each State and Territory.  This inventory consists of 732,552 bridges with 123 features including,

- Basic Information,
- Design, 
- Maintenance, 
- Location, 
- Traffic Patterns, and 
- Future Plans.

The first challenge was to wrangle the dataset into a DB Browser SQL database that is suitable to support modeling. Assessing the most valuable data, I selected Permanent Interstate routes that carry Mainline service on the Base Highway Network / National Highway System. This selection reduced the bridge dataset to 45,962 with 123 features.

Next, I undertook a significant EDA activity. Because the data is collected by state by many different assessors using a characters-based data definition, the first thing I did is create a Data Dictionary to identify the relevant features by feature group. This resulted in 21 total features and 1 binary target comprised of 4 Condition features. With that Data Dictionary, I was then able to make the dataset complete. Key updates include, 

- Correcting missing or incorrect information using the existing dataset or the internet,
- Replacing coordinates with a decimal coordinate system, and
- Simplifying the character-based categorical designations to a sequential numeric designation.

Going into modeling I started with a logical set of features that could most impact Bridge Condition. From the analysis and modeling I developed the final set.

## Algorithms

Bridge Features are a relatively simple modeling exercise once the data is prepared.  The biggest challenge is the imbalance of the dataset and finding the set of features based on the limited binary target of Structurally Deficient.

![](https://github.com/arbgar/metis/blob/main/Classification/Project/Final%20Deliverable/Algorithm.png?raw=true)

## Tools

- DB Browser and SQL Alchemy for the NBI Database including data analysis, cleansing, and selection
- Excel for the Data Dictionary including limited data analysis focusing on Pivot and Lookup functions
- Pandas and Numpy for analysis
- scikit-learn and imbalanced-learn for modeling
- Matplotlib and Seaborn for modeling visualization
- Tableau for EDA visualization:
  - [NHS Bridge Geographical Representation](https://public.tableau.com/app/profile/alison.garrett/viz/Book1_16355089243510/Sheet1)
  - [NHS Bridge Categorization](https://public.tableau.com/app/profile/alison.garrett/viz/NBI_25_1/Dashboard1)

## Communication

The *Saving our Nation's Bridges* presentation summarizes the findings in graphical format including the following key elements:

- **Introduction** to the issue of Structural Deficiency in United States Bridge Infrastructure
- Overview of  **The State of the National Highway System**, categorizing the issues in our largest transportation network
- **Modeling** which describes the selected Ensemble Random Forest Classifier and parameters
- **Feature Importance** which shows which features are most important when modeling the probability of Structural Deficiency
- **Fair Condition Bridges with High Probability Features** samples a few of the bridges which may have a higher probability of Structural Deficiency
- **Recommendations** for next steps to use the Model to augment the existing Inspection process

The presentation is targeted for technical organizations such as the American Society of Civil Engineers who  support and advocate for Infrastructure Improvement.
