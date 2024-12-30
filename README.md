# Ecommerce Customer Churn prevention

## **Summary:**

**Main objective:** Use Data Science and Machine Learning techniques in order to predict customer churn and identify those things that make customers churn from the ecommerce

**Key insights:** 

- Features such as Tenure and Complain had a great impact in the model, and during the Exploratory Data Analysis, it was observed that lower Tenure customers are more likely to churn, and customers who complained recently are also likely to churn. 
- People from City Tier 2 and 3 are more likely to churn
- 9 from the 17 original features were selected for the best model. Feature engineering was crucial for improving the model finding complex relationships between the data.

## **Introduction:**

For any business getting new customers and keeping old ones is key to keep getting profit and make the business grow. With all the social media phenomenom, it is common that people recommend, review, or even just post a photo using merchandise that everyone can see and maybe get interested on it. For ecommerces, this is specially important, since they don't have physical shops, this could be a great way to get "free advertising".

It is crucial to keep customers who bought merchandise from the ecommerce, in order to keep getting profit and don't reduce income, or they can recommend the products to other people, generating new customers. Also, it is important to indague what are the reasons for a customer to churn, since it can help to improve the service, product quality, delivery methods and other aspects.

## **Business objectives:**

**Main objective:** Identify customers at risk of churn.

**Secondary objectives:** Improve customer retention taking preventive and corrective actions on the reasons that made customers churn. Identify behavior patterns associated with customer churn.

# Suggestions for business

* Tenure had great impact in the model. From observed on EDA, customers with low tenure are more likely to churn, it's important to explore why they churned and to evaluate strategies to improve the experience of the newer customers.

* Complain has also importance in the model, considering that people who complained recently are more likely to churn as observed on EDA, it is important to take preventive and corrective actions over customer complains. Investigate the reasons that make customers complain and correct them before they do it; also improve complain solving to give a better experience to the customers.

* Considering that Marital Status had signifficant impact in the model, could be an option to study what categories or products do the people from each marital status buy, in order to make personalized offers for each one. Also, it's important to distinguish if they are Male or Female, considering that the gender was an important feature too.

* From EDA, it was also observed that people from CityTier 2 and 3 are considerably more likely to churn. It is important to investigate the reasons applying strategies as survey for people from all 3 city tiers who churned.

## Frameworks used:

![pandas](ecommerce_customer_churn_prevention/images/pandas.png) ![sklearn](ecommerce_customer_churn_prevention/images/sklearn.png) ![seaborn](ecommerce_customer_churn_prevention/images/seaborn.png) ![pingouin](ecommerce_customer_churn_prevention/images/logo_pingouin.png) ![optuna](ecommerce_customer_churn_prevention/images/optuna-logo.png) ![xgboost](ecommerce_customer_churn_prevention/images/xgboost-logo.png)

## Data source:

This dataset was taken from Kaggle: [Ecommerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data)

**Author:**

William Pabon, Data Scientist

[LinkedIn](https://www.linkedin.com/in/wiferpagri/)

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so ecommerce_customer_churn_prevention can be imported.
    │
    └── ecommerce_customer_churn_prevention               <- Source code for use in this project.
        ├── __init__.py    <- Makes ecommerce_customer_churn_prevention a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---
Project based on the [cookiecutter conda data science project template](https://github.com/Wiferpagri/cookiecutter-conda-data-science).
