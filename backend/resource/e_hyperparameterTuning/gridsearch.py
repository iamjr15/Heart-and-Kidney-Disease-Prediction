
from sklearn.model_selection import GridSearchCV

def hyperparamter_tuning(model,grid_param,X_train, y_train):
    grid_search_model = GridSearchCV(model, grid_param, cv = 5, n_jobs = -1, verbose = 1)
    grid_search_model.fit(X_train, y_train)
    best_estimator = grid_search_model.best_estimator_

    return best_estimator