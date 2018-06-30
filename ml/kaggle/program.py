import pandas as pd

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

y = train_data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = train_data[predictors]

from sklearn.tree import DecisionTreeRegressor

classifier = DecisionTreeRegressor()

# test_X = test_data[predictors]

# print(classifier.predict(test_X))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
classifier.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(y_test, classifier.predict(X_test)))

def get_mae(max_leaf_nodes, X_train, y_train, X_test, y_test, random_state):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=random_state)
    model.fit(X_train, y_train)
    return mean_absolute_error(y_test, model.predict(X_test))

for leaf_node in [5, 50, 500, 5000]:
    print(get_mae(leaf_node, X_train, y_train, X_test, y_test, 0))

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)
print()
print(mean_absolute_error(y_test, model.predict(X_test)))

print()

