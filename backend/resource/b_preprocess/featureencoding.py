from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

def label_encoder(dataframe,category_column):
    dle = defaultdict(LabelEncoder)
    dataframe[category_column] = dataframe[category_column].apply(lambda x: dle[x.name].fit_transform(x))

    return dataframe , dle