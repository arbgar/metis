![](https://github.com/arbgar/metis/blob/main/Regression/Project/Deliverables/FID_Logo.png)

# Flip It DC

My initial analysis is to predict the price of homes for sale and then look at the delta to the tax record to determine potential value (to buy, fixup, and sell). To gather the data, I scraped approximately 1025 observations of 75 potential features from [homesnap.com](https://www.homesnap.com).

After limiting the regression features to the most complete, straightforward numerical features, I started by using a target of Price/SqFt.  I quickly found limited correlation with some collinearity with other numerical features in the dataset as shown below. 

![](https://github.com/arbgar/metis/blob/main/Regression/Project/Deliverables/image-20210927181406202.png)

A quick review of the data also showed that real estate agents do not enter data consistently. Before proceding with the analysis, I opted to gather additional, more consistent numerical features in the dataset. With this I again selected the most complete, straightforward, numerical features again using pairplot and heatmap.

![](https://github.com/arbgar/metis/blob/main/Regression/Project/Deliverables/image-20210928161148298.png)

Then doing an initial LASSO regression model adds to the understanding of the most impactful features in the model for the training data.  Next steps are to downselect the features accordingly and complete cleaning, before progressing with linear regression, validation data, and feature engineering.

![](https://github.com/arbgar/metis/blob/main/Regression/Project/Deliverables/image-20210928161605367.png)
