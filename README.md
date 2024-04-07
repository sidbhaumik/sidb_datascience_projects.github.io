# Data Science Projects
This repo contains projects covering various Data Science concepts like Data exploration and analysis, visualization, machine learning, Etc.

# Project List
1. **Forecasting EV Landscape**: This project looks at the Electric Vehicle population and sales across United States, explores the historical data, challenges, competition, market situation and predicts the future trend and growth in US market.
   
   **Dataset used**: US_Electric_fuel_vehicles.csv, https://en.wikipedia.org/wiki/Electric_car
   
   **Python Libraries used**: Pandas, NumPy,Matplotlib, beautifulsoup,scikit-learn
   
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
   
