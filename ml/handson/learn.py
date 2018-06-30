from load_data import load_housing_data,informed_split_train_test
from load_data import ShowData,DataFrameSelector, CombinedAttributesAdder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

import pandas as pd
import numpy as np

#Models
from sklearn.linear_model import LinearRegression

housing = load_housing_data()

train_set, test_set = informed_split_train_test(housing.copy(), 0.2, 42)

# transformations

A = train_set.drop("median_house_value", axis=1)
y = train_set["median_house_value"].copy()

# Categorical Encoder
X =  pd.get_dummies(A)

num_pipeline = Pipeline([
        #('selector', DataFrameSelector(num_attribs)),
        ('imputer', Imputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler())
    ])

# cat_pipeline = Pipeline([
#         ('selector', DataFrameSelector(cat_attribs)),
#         #('cat_encoder', CategoricalEncoder(encoding="onehot-dense"))
#     ])

# full_pipeline = FeatureUnion(transformer_list=[
#         ("num_pipeline", num_pipeline),
#         #("cat_pipeline", cat_pipeline)
#     ])

housing_prepared = num_pipeline.fit_transform(X)

# Models

# 1. Linear Model

#model = LinearRegression()
#model.fit(housing_prepared, y)

### Test model
some_data = X.iloc[:5]
some_labels = y.iloc[:5]
prepared_data = num_pipeline.transform(some_data)

#housing_preds = model.predict(prepared_data)

from sklearn.metrics import mean_squared_error

#lin_mse = mean_squared_error(some_labels, housing_preds)
#lin_mse = np.sqrt(lin_mse) # Not satisfying

# from sklearn.tree import DecisionTreeRegressor

# tree_model = DecisionTreeRegressor()

# tree_model.fit(housing_prepared, y)

# preds = tree_model.predict(prepared_data)
# tree_mse = mean_squared_error(some_labels, preds)
# tree_mse = np.sqrt(tree_mse)

from sklearn.model_selection import cross_val_score

#scores = cross_val_score(tree_model, housing_prepared, y, scoring='neg_mean_squared_error', cv=10)

# rmse = np.sqrt(-scores)

def print_scores(scores):
    print(scores)
    print("Mean: ", scores.mean())
    print("STD: ", scores.std())

# print_scores(rmse)

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor()
# forest_reg.fit(housing_prepared, y)

# preds = forest_reg.predict(prepared_data)

# forest_mse = mean_squared_error(some_labels, preds)

# forest_mse_scores = cross_val_score(forest_reg, housing_prepared, y, scoring='neg_mean_squared_error', cv=10)

# forest_rmse_scores = np.sqrt(-forest_mse_scores)

# print_scores(forest_rmse_scores)


from sklearn.model_selection import GridSearchCV

param_grid = [
    {'n_estimators': [50, 100, 150], 'max_features': [7, 8, 9]},
    #{'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]}
]

grid_search = GridSearchCV(forest_reg, param_grid, cv=10, scoring='neg_mean_squared_error')

grid_search.fit(housing_prepared, y)

final_model = grid_search.best_estimator_

X_test = test_set.drop("median_house_value", axis=1)
y_test = test_set["median_house_value"].copy()

X_test_prepared =  num_pipeline.transform(X_test)

final_pred = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_pred)
final_rmse = np.sqrt(-final_mse)

print(final_rmse)

# feature_importances = grid_search.best_estimator_.feature_importances_


