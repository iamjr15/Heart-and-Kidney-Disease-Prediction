from sklearn.tree import DecisionTreeClassifier
from resource.e_hyperparameterTuning import hyperparamter_tuning

grid_param = {
        'criterion' : ['gini', 'entropy'],
        'max_depth' : [3, 5, 7, 10],
        'splitter' : ['best', 'random'],
        'min_samples_leaf' : [1, 2, 3, 5, 7],
        'min_samples_split' : [1, 2, 3, 5, 7],
        'max_features' : [ 'sqrt', 'log2']
    }

def DecisionTree(X_train, y_train):
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    dtc = hyperparamter_tuning(dtc,grid_param,X_train, y_train)

    return dtc
