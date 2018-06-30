import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
FILE_NAME = 'housing'
TAR_FILE_NAME = FILE_NAME + '.tgz'
CSV_FILE_NAME = FILE_NAME + '.csv'
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/" + TAR_FILE_NAME


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    tar_file_name = TAR_FILE_NAME
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, tar_file_name)
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_file_name = CSV_FILE_NAME
    csv_file = os.path.join(housing_path, csv_file_name)
    return pd.read_csv(csv_file)

def preview_data(data):
    data.hist(bins=50, figsize=(25, 15))
    plt.show()

# creating a test set
# 1. Using random sampling
# 2. Using informed sampling

def split_train_test(data, test_ratio, random_seed=42):
    rgen = np.random.RandomState(random_seed)
    shuffled_indices = rgen.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

# using informed split

def informed_split_train_test(data, test_ratio, random_seed):
    data['income_cat'] = np.ceil(data['median_income'] / 1.5)
    data['income_cat'].where(data['income_cat'] < 5, 5.0, inplace=True)

    split = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=42)

    for train_index, test_index in split.split(data, data['income_cat']):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]
    for set in (strat_train_set, strat_test_set):
        set.drop('income_cat', inplace=True, axis=1)
    return strat_train_set, strat_test_set

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


class ShowData(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=0):
        return self

    def transform(self, X, y=0):
        print(X.shape)
        return X