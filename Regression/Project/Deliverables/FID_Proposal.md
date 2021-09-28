![](https://github.com/arbgar/metis/blob/main/Regression/Project/Deliverables/FID_Logo.png)

# Flip It DC

**Retro Renovations** specializes in renovating homes built between 1920 and 1960, restoring them to their previous grandeur while focusing on livability for today's families.  To augment their custom renovation work, Retro Renovations maintains a **Flip It** branch which focuses on rapidly buying, renovating, and selling well positioned real estate properties for a sizable return on investment.  Initial corporate scouting showed potential in the Washington DC market leading to the new **Flip It DC** subsidiary.  As the *Find-It Analyst* for Flip It DC, my job is to identify local real estate trends and properties for renovation.

# Analysis

My initial analysis will focus on sales price, that is modeling and then predicting the sales price based on key home features.  This will allow the Flip It DC *Buy-It Agents* to determine a competitive offer and the *Profit-From-It Analysts* to consider resale potential. Subsequent analysis may include sales statistics such as time on market to identify a lowest purchase price strategy.

# Data Description

[HomeSnap](https://www.homesnap.com/) features accurate, real-time MLS data and enhanced property features to make it easy to search for and share properties.  With easy access to underlying datasets through web scraping, HomeSnap provides a complete dataset for the analysis.  To develop a robust model of at least 1000 observations with 12 features, we will focus on the [Cleveland Park](https://www.homesnap.com/homes/DC/Washington/Cleveland-Park/t_7/ctp_1/st_7/c_38.937777,-77.060263/z_14) neighborhood.

# Tools

HomeSnap has a homepage from which users select various parameters including location, property type, and sales status, for their property search. From these parameters, the homepage generates a target list of properties in real time.  I will leverage Selenium to scrape the property list for addresses and then use Beautiful Soup to scrape the detailed property information using address-based URLs. Once I have the needed Cleveland Park dataset, I will perform multiple linear regression analyses, including validation and testing, using scikit-learn.  

# MVP Objective

The Flip It DC CEO is eager to understand the Cleveland Park market.  She has asked for an initial    Minimum Viable Product (MVP) presentation prior to the Final Presentation / Written Description to get a sense of the potential.  The MVP will provide an initial analysis of the Cleveland Park HomeSnap data by analyzing sales price based on key property features.  The MVP will also assess the feasibility of including  real estate sales trends such as the time on the market.