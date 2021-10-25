![](https://github.com/arbgar/metis/blob/main/Classification/Project/Deliverable/72e1aeaa-09b2-4240-9e44-f91f88ef200eOriginal.png?raw=true)

​																																*Photo by [NPS / Victoria Stauffenberg](https://www.nps.gov/media/photo/view.htm?id=72e1aeaa-09b2-4240-9e44-f91f88ef200e)*

# Saving our Nation's Bridges

To begin this project, I downloaded the [National Bridge Inventory](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) a dataset consisting of 732,552 bridges with 123 features.  The first challenge was to wrangle the dataset into a DB Browser SQL database that is suitable to support modeling.  Assessing the most valuable data, I selected *Permanent* *Interstate* routes that carry *Mainline* service on the *Base Highway Network / National Highway System*.  This selection reduced the bridge dataset to 45,962 with 123 features.

Next, I undertook a significant EDA activity.  Because the data is collected by state by many different assessors using a characters-based data definition, the first thing I did is create a Data Dictionary to identify the relevant features by feature group, including Basic, Design, Maintenance, Location, Traffic, and Plan.  This resulted in 21 total features and 1 binary target comprised of 4 Condition features. With that Data Dictionary, I was then able to make the dataset complete and consistent as shown below.   

###### Bridge Locations

![](https://github.com/arbgar/metis/blob/main/Classification/Project/Deliverable/conus.png?raw=true)

###### Bridge Age

![](https://github.com/arbgar/metis/blob/main/Classification/Project/Deliverable/age.png?raw=true)

###### Bridge Type

![](https://github.com/arbgar/metis/blob/main/Classification/Project/Deliverable/type.png?raw=true)

The government classifies a bridge as “structurally deficient”  when any of four bridge components,

- DECK_CONDITION
- SUPERSTRUCTURE_CONDITION,
- SUBSTRUCTURE_CONDITION, or
- CULVERT_CONDITION

are rated as *POOR*, meaning a condition rating of 4 or worse on a scale of 0 to 9.  Therefore, my target is a binary True / False based on whether the overall rating of the bridge is structurally deficient. Unfortunately,  the dataset selected yielded a very unbalanced dataset with only 1364 bridges rated as POOR.  Initial Logistic Regression models scored over 97% on any feature set because of this imbalance. 

Next steps are to use the Class Imbalance techniques learned today to address the imbalance in the dataset, rerunning the models accordingly.  Subsequent steps include model selection and feature engineering as there are actually four distinct ratings that can make a bridge structurally deficient.  Each rating will likely be driven by a different set of features. I expect the modeling to progress more quickly now that the data is in good condition in the database.
