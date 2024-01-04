from package import *
from resource.topics.heart import get_features_target

model_list = ['knn','decision_tree','logistic_regression','naive_bayes','svc','neuralnetwork' ]

topic      = Path(__file__).stem

dataframe  = load_csv(topic)

X, y       = get_features_target(dataframe)

X_train, X_test, y_train, y_test = get_train_test_split(X,y)

model_compare = train_models(X_train,y_train,X_test,y_test,model_list,topic)

save_result(model_compare,topic)