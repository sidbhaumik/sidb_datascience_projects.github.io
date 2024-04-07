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
   Building a movie database.
  
      **Dataset used**: http://www.omdbapi.com/?
      
      **Python Libraries used**: urllib, json

      **Method used**:
       Building a Movie Database Program by Reading an API:
   
       1. It imports necessary libraries like urllib, json.
   
       2. It loads a secret API key from a JSON file for the OMDb (Open Movie Database) API.
   
       3. It defines utility functions to:
            Print movie data from a JSON response
            Download and save a movie poster locally
            Search for a movie by name, print its details, and save the poster
   
       4. It tests the search functionality with movies like "Titanic" and an invalid name.
     
7. **Predicting Fuel Efficiency**:
   This document focuses on building a linear regression model to predict fuel efficiency (miles per gallon) of automobiles using
   the auto-mpg dataset. 
     
      **Dataset used**: auto-mpg.csv
      
      **Python Libraries used**: pandas,seaborn, matplotlib,scipy,sklearn

      **Method used**:
      1. Data Loading and Preprocessing:
         
         a. The dataset is loaded into a Pandas dataframe.
         
         b. Exploratory data analysis is performed, including checking correlations and creating visualizations.
         
         c. Missing values in the 'horsepower' column are handled.
         
         d. The data is split into training and testing sets.
         
      3. Linear Regression Model:
         
         a. A linear regression model is trained on the training data.
         
         b. Performance metrics like RMSE (root mean squared error), MAE (mean absolute error), and R-squared are calculated
            for both training and testing data.
         
         c. The coefficients of the linear regression model are printed.
         
      5. XGBoost Regression Model:
         
         a. An XGBoost regression model is built using GridSearchCV for hyperparameter tuning.
         
         b. The XGBoost model's performance is evaluated using RMSE, MAE, and R-squared on both training and testing data.
         
      7. Results and Comparison:
         
         a. The XGBoost model performs better than the linear regression model, with lower RMSE and MAE values on
               both training and testing data.
         
      9.  The R-squared value for the XGBoost model is slightly higher than the linear regression model, indicating a better fit.

 8.  **Recommendation System**:
        Movie recommendation program allows users to get personalized movie recommendations based on their input.
      **Dataset used**: movies.csv,ratings.csv
      
      **Python Libraries used**: pandas,fuzzywuzzy,sklearn

      **Method used**:
      The code implements a movie recommender system using the MovieLens dataset, which includes movie ratings and titles.
      The main steps are:
        a. Load and merge the ratings and movies data into a single DataFrame.
        b. Create a pivot table with movie titles as rows, user IDs as columns, and ratings as values.
        c. Fill in missing rating values with 0.
        d. Create a TF-IDF vector representation of the movie titles.
        e. Calculate a cosine similarity matrix between the movie title vectors.
        f. Define a function to get the closest matching movie title based on fuzzy string matching.
        g. Define a function to generate top N recommendations for a given movie title by finding the most similar movies
            based on the cosine similarity matrix.

         The recommender system allows the user to input a movie title, and it will:
           a. Find the closest matching movie title.
           b. Use the cosine similarity to find the top 10 most similar movies.
           c. Print the recommended movie titles.

        The key aspects of the recommender system are preprocessing the data, creating a matrix of movie similarities,
        and using fuzzy matching to handle user input.

   9. **Sentiment Analysis**:
        This code demonstrates how to perform sentiment analysis on movie reviews using two different libraries (TextBlob and VADER), 
        as well as how to create bag-of-words and TF-IDF representations of the text data, which can be useful for further machine learning          tasks.

        **Dataset used**: labeledTrainData.tsv
      
         **Python Libraries used**: pandas,numpy,nltk,textblob

         **Method used**:
         1. Data Preprocessing:
            The code reads in a TSV dataset containing movie reviews and their corresponding sentiment labels.
            It cleans the text by converting to lowercase, removing punctuation, and tokenizing the words.
            It also removes stop words and applies stemming to the text.
         2. Sentiment Analysis using TextBlob:
            The code uses the TextBlob library to generate a sentiment polarity score for each review, ranging from -1 to 1.
            It then categorizes the reviews as "POSITIVE" or "NEGATIVE" based on the polarity score.
            The accuracy of the TextBlob-based sentiment analysis is calculated and reported.
         3. Sentiment Analysis using VADER:
            The code uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) library to generate sentiment scores for each review.
            It categorizes the reviews as "POSITIVE" or "NEGATIVE" based on the compound sentiment score.
            The accuracy of the VADER-based sentiment analysis is calculated and reported.
         4. Bag-of-Words Representation:
            The code creates a bag-of-words matrix from the preprocessed text using the CountVectorizer from scikit-learn.
            It also creates a TF-IDF (Term Frequency-Inverse Document Frequency) matrix from the preprocessed text.
            The dimensions of the bag-of-words and TF-IDF matrices are displayed.

   10.  **Top 100 ebooks titles**:
           This code demonstrates how to scrape data (top 100 ebook titles) from a website (Project Gutenberg) using Python
           and common libraries like BeautifulSoup and regex.
          
         **Dataset used**: https://www.gutenberg.org/browse/scores/top
      
         **Python Libraries used**: urllib.request, urllib.parse, urllib.error,requests,BeautifulSoup

         **Method used**:
         1. The code extracts the top 100 ebooks from the Project Gutenberg website.
         2. It follows these main steps:
                     Ignores SSL certificate errors to access the website.
                     Reads the HTML content of the top 100 ebooks page.
                     Finds all the href links on the page.
                     Uses regular expressions to extract the numeric file numbers for the top 100 ebooks.
                     Extracts the titles of the top 100 ebooks from the HTML content.
         3. Specifically, the code:
                     Loops through the href links to find the file numbers for the top 100 ebooks.
                     Searches the HTML content to find the section with the "Top 100 EBooks yesterday" heading.
                     Extracts the titles of the top 100 ebooks by looping through the lines of text after the heading and using regular
                     expressions to remove the non-title text.
                     Prints the list of the top 100 ebook titles.
         4. The key aspects of the code are:
                     Handling the SSL certificate issue to access the website.
                     Using BeautifulSoup to parse the HTML content.
                     Leveraging regular expressions to extract the desired information (file numbers and titles).
                     Iterating through the HTML content to find the relevant sections and extract the data.

   11.  **Weather App**:
          The code implements a simple and user-friendly weather application that retrieves and displays current weather
           and 36-hour forecast data for any US city or zip code using the OpenWeatherMap API.
                  
         **Dataset used**:
          https://api.openweathermap.org/data/2.5/weather
        
           https://api.openweathermap.org/data/2.5/forecast
        
         **Python Libraries used**: requests, json, time

         **Method used**:
         1. The main functionality is contained in the main() function, which:
               Prompts the user to enter a zip code or city/country name.
               Calls two helper functions to retrieve the current weather data and the extended 36-hour forecast data.
               Displays the current weather information and the 36-hour forecast.
               Prompts the user to enter another location or exit the program.
         2. The weather_current() function:
               Constructs the API request URL based on the user input (zip code or city/country).
               Makes a GET request to the OpenWeatherMap API to retrieve the current weather data.
               Handles any errors that may occur during the request.
               Formats and prints the current weather information.
         3. The weather_extended() function:
               Constructs the API request URL for the 36-hour forecast based on the user input.
               Makes a GET request to the OpenWeatherMap API to retrieve the extended forecast data.
               Handles any errors that may occur during the request.
               Formats and prints the 36-hour forecast information.
         4. The convert_temp() function is a helper function that converts temperatures from Kelvin to Fahrenheit and Celsius.
         5. The try_web() function is a helper function that handles various types of errors that may occur during the API requests,
               such as HTTP errors, connection errors, timeout errors, and other exceptions.
         6. The current_formatted() and ext_formatted() functions format the current weather and extended forecast data, respectively,
                 for easy display to the user.
         7. The more_weather() function allows the user to enter another location or exit the program.
     
   
