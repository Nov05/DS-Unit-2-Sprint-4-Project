import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

url_img1 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/roughly%20compare%20models.png?raw=true"
url_img2 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/train_test_data_split.png?raw=true"
url_img3 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/prediction%20random%20forest.png?raw=true"

block1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Process
            
            &nbsp;
            #### Data Wrangling and Feature Engineering
            
            1. Merge data from the two CSV files into one data frame;   
            2. Count how many breakdown codes there are in a project, and make it a new feature. Usually the more breakdown codes a projects has, the larger and the more complex the project is;
            3. Divide the Developer Performance into 10 levels, and make it a new feature. Usually the better performance a developer has, the less effort is estimated for a task;  
            4. Hours' distributions are highly skewed, hence we calculate their log values to make it easir for our models.
            5. Use Actual Hours (log) as the target feature. This will be a regression problem.  
            6. We want to predict effort for different projects, different developers, etc. So those columns will be dropped. Instead, we want to keep feature `Category`, `SubCategory`, `Priority`, `HoursEstimate`(log) and engineered feature Breakdown Numbers, Developer Performance Level to train our models.  
            
            &nbsp;
            #### Baseline Prediction
            
            Use HourEstimate (log) median (1.3862) as prediction, and calculate the Mean Squared Logarithmic Error (MSLE) score, so we have a baseline score `1.1627`. Also if we calculate the MSLE score for HoursEstimate and HoursActual, we will have another baseline score `0.752`. We expect our models to have lower scores.
            
            &nbsp;
            #### Data Spliting
            
            Randomly split the data into trainval data (80%) and test data (20%). Check their distributions, and they shouldn't be very different.
            """
        ),
        html.Img(id='img2', src=url_img2, width="700px"),
        
        dcc.Markdown(
            """
            &nbsp;
            #### Modeling
            
            1. Roughly compare the following models and choose Random Forests.
            * kn = K-Neighbors
            * dt = Decision Tree
            * rf = Random Forest
            * et = Extra Trees
            * ada = Ada Boost
            * gb = Gradient Boosting
            """
        ),
        html.Img(id='img1', src=url_img1, width="700px"),  
        
        dcc.Markdown(
            """
            &nbsp;
            
            2. Build a pipepline.
            ```
            ###############################################
            # Pipeline preprocessor
            ###############################################
            numeric_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())])
            onehot_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                ('onehot', ce.OneHotEncoder(drop_invariant=True, use_cat_names=True))]) 
            ordinal_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                ('ordinal', ce.OrdinalEncoder())])
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numeric_transformer, numeric_features),
                    ('one', onehot_transformer, categorical_features)
                ])
            ###############################################
            # Pipeline regressor
            ###############################################                
            pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('rf', RandomForestRegressor(
                               n_estimators=29,
                               max_depth=6,
                               random_state=random_state, 
                               n_jobs=n_jobs)), 
                          ])  
            ```
            3. Use `sklearn.model_selection.RandomizedSearchCV()` to find proper parameters.
            
            &nbsp;
            #### Evaluation
            
            Our model's RMSE score is 0.647 over all.
            """
        ),
        html.Img(id='img3', src=url_img3, width="700px"),
        
        dcc.Markdown(
            """
            &nbsp;
            #### Links  
            
            **Data Source**  
            SiP Dataset https://github.com/Derek-Jones/SiP_dataset  
            **GitHub Repository**  
            https://github.com/nov05/DS-Unit-2-Sprint-4-Project  
            **Colab Notebook**  
            https://colab.research.google.com/drive/1bhy_G9Dttgb2XoI8veIpnru_oO4W3Pcf  
            """
        ),        
    ],
)

blankrow = dbc.Col(
    [
        dcc.Markdown(
            """
            &nbsp;
            """
        ),
    ],
    md=4,
)

layout = dbc.Row([block1])