# Data Science Projects
This repo contains projects covering various Data Science concepts like Data exploration and analysis, visualization, machine learning, Etc.

# Project List
1. **Forecasting EV Landscape**: This project looks at the Electric Vehicle population and sales across United States, explores the historical data, challenges, competition, market situation and predicts the future trend and growth in US market.
   
   **Dataset used**: US_Electric_fuel_vehicles.csv, https://en.wikipedia.org/wiki/Electric_car
   
   **Python Libraries used**: Pandas, NumPy,Matplotlib, Seaborn, beautifulsoup,scikit-learn
   
   **ML techniques used**: Regression analysis, Predictive analysis, Cluster analysis, Correlation analysis, Categorical analysis
   
2. **Indian_restaurants_program**: The goal is to find the best US city out of 4 given choices with the highest Indian restaurants density.
   
   . Chicago,IL
   
   . Miami, FL
   
   . New York, NY
   
   . Los Angeles,CA.

   **Method used**: I have used the **Four Square API** through the venues channel.
   I used the near query to get venues in the cities.
   Also, I have used the CategoryID 4bf58dd8d48988d10f941735 to show only Indian restaurants.
   
   Foursquare limits us to maximum of 100 venues per query. I repeated this request for the 4 U.S cities and got their top 100 venues.
   I only saved the name and coordinate data from the result and plotted them on the map using **Folium** for visual inspection.
   
   Next, to get an indicator of the density of Indian restaurants, I calculated a center coordinate of the venues to get the
   mean longitude and latitude values.
   Then I calculated the **mean of the Euclidean distance** from each venue to the mean coordinates.
   This was my indicator - **mean distance to the mean coordinate.**

3.  **Exploring Neighborhoods in the city of Toronto**:
      Exploring Toronto neighborhood.Generate maps to visualize the neighborhoods and how they cluster together.
      
      **Dataset used**:
      https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
    
      http://cocl.us/Geospatial_data

      **Python Libraries used**: Pandas, NumPy,Matplotlib, Seaborn, beautifulsoup,sklearn, folium

    **Method used**:
    1. Data is scraped from Wikipedia to get a list of postal codes and neighborhoods in Toronto.
    2. Using the Foursquare API, nearby venues for each neighborhood are obtained and categorized.
    3. The neighborhoods are clustered into 5 groups based on the types of venues present, using K-means clustering.
    4. The most common venue categories for each neighborhood are identified and tabulated.
    5. Geographic coordinates are obtained for each neighborhood using geocoding.
    6. An interactive Folium map is generated, with markers indicating the neighborhoods color-coded by their cluster assignment.
  
4. **Boston Housing Market Analysis**:
   This document analyzes the Boston housing market dataset.

   **Dataset used**:
      Boston_housing.csv

   **Python Libraries used**: Pandas, NumPy,Matplotlib

    **Method used**:
    The key steps and findings are:
      1. The Boston housing dataset is read from a CSV file, containing information on variables like crime rate, age of homes,
         rooms per dwelling, etc.
      3. Histograms are plotted for all variables in the new DataFrame using a loop.
      4. Scatter plots are created to visualize the relationship between crime rate (and its log value) vs housing prices.
      5. Some useful statistics are calculated:
         Mean rooms per dwelling: 6.28
         Median age of homes: 77.5 years
         Mean distance to 5 Boston employment centers: 3.8
      6. The percentage of houses with a low price (<$20,000) is calculated as 41.5%.
      
      The analysis provides insights into the Boston housing market by exploring the distributions of different variables,
      their relationships with housing prices, and calculating summary statistics.
   
5. **Movie Database**:
  
      **Dataset used**: http://www.omdbapi.com/?
      
      **Python Libraries used**: urllib, json

      **Method used**:
       Building a Movie Database Program by Reading an API
      
         1. It imports necessary libraries like urllib, json.
         2. It loads a secret API key from a JSON file for the OMDb (Open Movie Database) API.
         3. It defines utility functions to:
            Print movie data from a JSON response
            Download and save a movie poster locally
            Search for a movie by name, print its details, and save the poster
         4. It tests the search functionality with movies like "Titanic" and an invalid name.
     
   6. 
      
   
