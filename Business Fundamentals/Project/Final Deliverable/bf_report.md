![](https://github.com/arbgar/metis/blob/main/Business%20Fundamentals/Project/Deliverable/bf_Picture.png)

# Delivering to Washington DC Food Deserts

## Leveraging Unofficial Community Solutions 

Washington DC has long suffered from Food Deserts, that is, residential areas without access to fresh and nutritious food. DC Hunger Solutions in its recent report, [Still Minding the Grocery Gap in DC: 10th Anniversary Grocery Store Report](https://www.dchunger.org/wp-content/uploads/2021/01/StillMindingGroceryGap.pdf) states that, 

*Increasing the number of full-service grocery stores and corner stores selling healthy foods is an important strategy for turning food deserts into oases with opportunities to buy healthy foods.*  

This report, which highlights the widening grocery store gap between 2010 and 2020,  comes during a global pandemic, further limiting access to food sources. One recommendation from DC Hunger Solutions is for Officials to, 

*... study what unofficial community solutions have already been developed. An answer to food access in Wards 7 and 8 might already exist and just needs to be formalized and scaled. This also ensures any program is building power for residents.*

Fortunately, there are companies like [4P Foods](https://4pfoods.com/), a start-up with a new model of agriculture and a mission to, *Eat Good Food, Change the World: People, Planet, Prosperity, Purpose are the four P’s of 4P Foods.*4P Foods focuses on support to local farmers while ensuring the community has equitable access to the food they produce. During the pandemic 4P Food initially struggled financially with the loss of their wholesale market. But then, delivery sales accelerated, propelling them to 3-fold growth with over 3500 home deliveries each week. ***What if 4P Foods could leverage this success to help eliminate the Washington DC Food Deserts?***

## Design

Food Deserts are a significant challenge in the United States, both in rural and urban communities.  The USDA defines a Food Desert as a low-income census tract where a substantial number or substantial share of residents do not have easy access to a supermarket or large grocery store. Generally, this distance is 0.5 miles in urban locations and 10 miles in rural locations.  The challenge is so severe in Washington DC, particularly in Wards 7 and 8, that DC Hunger Solutions has set closing gaps at a distance of 1 mile as its goal.

Supporting the DC Hunger Solutions approach, this analysis sets the definition of a Food Desert at 1600 meters (approximately 1 mile) and assesses the impact to all, not just low income, populations.  For the DC Hunger Solutions community approach to be viable, there will need to be residents of all economical situations.  The pilot nature of the recommended program along with the need for limited additional infrastructure for a company like 4P Foods, makes this assessment and subsequent possible while limiting the risk of overextending.

## Data

The Federal and DC governments have  large datasets gathered from 10-year census activities, last completed in 2020 and regular American Community Survey (ACS) assessments.  This information forms the back bone of the analysis:

- [DC Open Data 2020 Census Data](https://opendata.dc.gov/datasets/DCGIS::census-blocks-in-2020/about) 6014 records with 32 attributes of DC Demographic data
- [DC Open Data Address Points](https://opendata.dc.gov/datasets/DCGIS::address-points/about) 148,709 records with 50 attributes of DC Address data

DC also maintains detailed shape files and supporting attributes on its Public Schools, Farmers Markets, and Grocery Stores: 

- [DC Open Data Public Schools](https://opendata.dc.gov/datasets/DCGIS::public-schools/about) 122 record shapefile with 32 attributes of Elementary School data
- [DC Open Data Public School Attendance Areas](https://opendata.dc.gov/datasets/DCGIS::school-attendance-zones-elementary/about) 74 record shapefile with 4 attributes of Elementary School Attendance Zone data
- [DC Open Data Farmers Market Locations](https://opendata.dc.gov/datasets/DCGIS::farmers-market-locations/about) 62 record shapefile with 14 attributes of Farmers Market data
- [DC Open Data Grocery Store Locations](https://opendata.dc.gov/datasets/DCGIS::grocery-store-locations/about) 79 record shapefile with 26 attributes of Grocery Store data

Supporting this analysis is the Food Desert specific USDA analysis based on Census and ACS datasets:

- [USDA Food Access Research Atlas](https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/) and [2010 to 2020 Census Tract Crosswalk](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.html) 3130 records with 40 attributes of Food Access Demographic data; updated regularly based on 2010 Census Tracts
- [USDA Community Supported Agriculture Directory](https://www.ams.usda.gov/local-food-directories/csas) 939 records of 5 attributes detailing Community Supported Agriculture (CSA) organizations

## Algorithms

Food Deserts are a relatively straight forward analysis to complete.  The biggest challenge is to filter large quantities of residential and demographic data for distance to fresh, good-quality food sources to identify areas and populations that need solutions.  From that assessment, community organizations already positioned in the area of need are selected and pilot programs developed leveraging the strengths of the organization in the community. Standard distance calculation in the X-Y coordinate system along with Pivots and Lookups provide the assessment.  Shapefiles with overlaid Marks in Latitude and Longitude provide the visuals.

![](https://github.com/arbgar/metis/blob/main/Business%20Fundamentals/Project/Final%20Deliverable/Algorithms.png)

## Tools

- Excel for data analysis focusing on Pivot and Lookup functions.  Note that the datasets involved were quite large requiring some ingenuity to complete the required analysis.  
- Tableau for visualization:
  - [Residential Address Analysis](https://public.tableau.com/app/profile/alison.garrett/viz/bf_78_analysis/Ward7)
  - [Grocery Stores by Ward](https://public.tableau.com/app/profile/alison.garrett/viz/bf_ward_grocery/Sheet2)
  - [Need Analysis](https://public.tableau.com/app/profile/alison.garrett/viz/bf_need/Dashboard1)
  - [Delivery Areas](https://public.tableau.com/app/profile/alison.garrett/viz/Wards-PS/Sheet2)

## Communication

The Delivering to Washington DC Food Deserts presentation summarizes the findings in graphical format including the following key elements:

- **Introduction** to the challenges of Food Deserts; with additional presentation time this chart could be expanded significantly
- Overview of  **4P Foods**, an innovative startup bringing a new agricultural model of support to local farmers and positive impact to the local community
- **Serving the Community** which highlights the most underserved residential addresses in Ward 7 and 8 along with the Elementary Schools who could serve as fresh, good quality food delivery hubs
- **4P Foods Business Return** which shows that even for a modest  customer base on limited income, this can bring Revenue to 4P Foods
- **Recommendations** for next steps including partnering with DC Hunger Solutions to design a phased pilot program approach 
