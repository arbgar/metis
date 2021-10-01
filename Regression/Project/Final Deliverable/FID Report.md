![](https://github.com/arbgar/metis/blob/main/Regression/Project/Final%20Deliverable/FID_Logo.png)

# Flip-It DC

## Under-valued Historic Homes Quick Look 

**Retro Renovations** specializes in renovating homes built between 1920 and 1960, restoring them to their previous grandeur while focusing on livability for today's families. To augment their custom renovation work, Retro Renovations maintains a Flip-It branch which focuses on rapidly buying, renovating, and selling well positioned real estate properties for a sizable return on investment. 

Initial corporate scouting showed potential in the Washington DC market leading to the new **Flip-It DC** subsidiary. As the Find-It Analyst for Flip-It DC, my job is to identify local real estate trends and recommend properties for renovation.

Now underway, Flip-It DC is eager to begin work on its first purchases / renovations.  Until the Sales Price Model is fully operational, the team requested a real estate market quick look, with initial target property recommendations for further review and final selection.

## Design

Real estate information, largely sourced from the Multiple Listing Service (MLS),  is widely available across many commercial apps.  These apps provide ready access to every detail about a property. Combining this property information  with the local government real estate property records yields an initial, high quality assessment without ever seeing the property.

The challenge of flipping homes is to find under-valued properties among the thousands of properties in a local market.  This is where modeling comes in.  By modeling the predicted Target Sales Price for a property based on its features, and comparing this price to its Asking Price and the local government Property Assessment, the analyst can easily identify under-valued properties.

These price diescrepancies can be caused by many factors other than under-valuation; most notably by a seller overpricing their property.  However, by finding an Asking Price and / or a Tax Assessment signficantly under the Target Sales Price, property condition will be one of several key reasons for the discrepancy.  

By reviewing the properties more closely, the analyst can quickly identify properties where minimal renovations will bring the property to at least average, if not luxury, condition yielding a significant return on investment when sold at / above the predicted Target Sales Price.

## Data

**[HomeSnap](https://www.homesnap.com/)** features accurate, real-time MLS data and enhanced property features to make it easy to search for and share properties. With easy access to underlying datasets through authorized web scraping, HomeSnap provides a complete dataset for the analysis. 

While HomeSnap allows the web scraping, more challenging is how the web pages are generated. Scraping requires a two step process to first identify the properties in the historic areas of the Washington DC area and then individually select each property to pull the details.  

Using Selenium to operate the web pages, Beautiful Soup to scrape, generous delays with repetition, and data aggregation yields a sufficient dataset  of 1020 properties, mostly in Northwest DC with scattered similar properties in ajoining Northern Virginia and Maryland.  The properties have a minimum of 74 core features and have been active in the real estate market over the past 6 months.  They are divided roughly as 50% Sold, 25% Under Contract, and 25% For Sale.  DC Property Records provides the information for minimal dataset clean-up. 

Unfortunately the Under Contract Price does not reflect the actual Contract Price.  Therefore the 25% Under Contract observations had to be considered in the For Sale (predicted) split. This limited the number of observations for the train / validate / test dataset likely limiting the fit of the model.  A next step will be to add more observations and rerun the model.

## Algorithms

The analysis focused on property sales price by modeling and then predicting the sales price based on key home features. This modeling,

- Helps the Flip It DC *Buy-It Agents* determine which properties may be under-valued, and 
- Provides a renovated price point for the *Profit-From-It Analysts* to consider resale potential.  

*Exploratory Data Analysis (EDA):* With 74 features, many categorical, EDA is an important first step in the modeling process. Through subject matter expertise these 74 features are downselected to 54 features. Focusing initially on consistent, numerical features which have largely complete datasets yields 25 potential features for the model.  Through correlation analysis via pair plots, heatmaps, and LARS path regression, the following 11 features are the starting point for linear regression: Longitude, Latitude, Year Built, Fireplaces, Levels, Square Feet, Garage Spaces, Tax Total Finished Square Feet, Bedrooms, Bathrooms, Lot Square Feet.

*Regression Modeling:*  The Sold dataset is the core regression modeling train/validate/test dataset. Dividing the dataset into train (60%), validate (20%) and test (20%) using a random state selections gives a repeatable dataset which  is also randomly adjustable to reassess the limited observations. Using this initial feature set and linear regression yields a 0.84 R-squared result.  However, given the tightly coupled features of property size and interior characteristics, multi-colinearity must be addressed. Eliminating features and limiting the Sales Price to $3.6M (2 sigma) to eliminate very unusual outlier properties yields a 0.42 R-squared result. 

To improve this result, a square factor polynomial regression significantly improves the model fit while limiting the collinearity.  This result is logical as it addresses an unusal property value spike with longitude for neighborhoods near the north-south Rock Creek National Park as well as the interelationship between the property features.

Further feature refinement explores categorization of the Structure Type, separating the more desireable Single Family and Semi-Detached properties from the Outer and Inner Row-homes.  

Finally Lasso regression surfaces those few features that have the most impact on the Sales Price.  Not surprisingly the most significant feature set is Baths followed by Levels / Semi-Detached which is a very quick way to select the largest house in the most desireable configuration.  Following that, Longitude squared selects the properties near the Rock Creek National Park.  These neighborhoods are known for their premium pricing.

Using this model yields an R-squared of 0.72 train and 0.64 validate. Randomizing the train and validate dataset yields similar results, some slightly better and some slightly worse.  Using the test data yields a final MAE of $209K wiht an R-squared of 0.68 for the Sales Price Model.

Next steps for the Sales Price Model are to increase the number of Sold observations in the dataset and explore additional feature categorization to refine locations and add impactful high-priced features to the model. These steps should improve the fit and reduce collinearity.

*Prediction:* With the Sales Price Model complete, prediction is a straightforward analysis of predicting the Target Sales Price based on the For Sale / Under Contract property features.  The model provides the average sales price for a property based on historical data.  What it doesn't account for is property condition which will significantly affect sales price.  

By comparing this Target Sales Price to the Asking Price and Property Assessment, under-valued  properties are evident. A straight comparison along with a downselect on DC historic homes yields exactly four properties which all appear to be good canidates for Flip-It DC.  Total potential profit is $0.3M - $2.0M with an error of $0.2M

## Tools

- Selenium and Beautiful Soup for web scraping
- Numpy and Pandas for data cleaning and manipulation 
- scikit-learn including Linear Regression, Polynomial Regression, and LASSO/LARs Regression for modeling
- Matplotlib and Seaborn for visualization
- Excel for minor data tagging and dataset aggregation

## Communication

The Flip-It DC presentation summarizes the findings in graphical format including the following key elements:

- **Flip-It methodology** which quickly sifts through large datasets for under-valued properties
- Quick look **Sales Price Model** which predicts a Target Sales Price given 9 features of which 3 are key
- **Four recommended properties** for purchase / renovation / resale with a potential for $2M profit
- Options for **model refinement** including a larger dataset and considering categorization of the Zip Code and Legal Subdivision features
