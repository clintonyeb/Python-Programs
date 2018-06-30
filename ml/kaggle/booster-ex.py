import pandas as pd

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

y = train_data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = train_data[predictors]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

def find_estim(estimator, rate):
    model = XGBRegressor(n_estimators=estimator, learning_rate=rate)
    model.fit(X_train, y_train, early_stopping_rounds=3, eval_set=[(X_test, y_test)], verbose=False)
    metrics = mean_absolute_error(y_test, model.predict(X_test))
    return metrics

##def gen_est(n):
##    n *= 10
##    yield n
##for est in range(10, 1000, 10):
##    print(est, ': ', find_estim(est, 0.05))


print(find_estim(120, 0.5)) 