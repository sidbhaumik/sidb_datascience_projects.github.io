**Predicting Fuel Efficiency**: This document focuses on building a linear regression model to predict fuel efficiency (miles per gallon) of automobiles using the auto-mpg dataset.

**Dataset used**: auto-mpg.csv

**Python Libraries used**: pandas,seaborn, matplotlib,scipy,sklearn

**Method used**:

Data Loading and Preprocessing: 

  a. The dataset is loaded into a Pandas dataframe. 
  
  b. Exploratory data analysis is performed, including checking correlations and creating visualizations. 
  
  c. Missing values in the 'horsepower' column are handled. 
  
  d. The data is split into training and testing sets.
  
Linear Regression Model: 

  a. A linear regression model is trained on the training data. 
  
  b. Performance metrics like RMSE (root mean squared error), MAE (mean absolute error), and R-squared are calculated for both training and testing data. 
  
  c. The coefficients of the linear regression model are printed.
  
XGBoost Regression Model: 

  a. An XGBoost regression model is built using GridSearchCV for hyperparameter tuning. 
  
  b. The XGBoost model's performance is evaluated using RMSE, MAE, and R-squared on both training and testing data.
  
Results and Comparison: 

  a. The XGBoost model performs better than the linear regression model, with lower RMSE and MAE values on both training and testing data.
  
The R-squared value for the XGBoost model is slightly higher than the linear regression model, indicating a better fit.
