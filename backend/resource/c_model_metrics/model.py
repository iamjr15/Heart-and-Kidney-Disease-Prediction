from resource.d_ml_models import DecisionTree, Logistic_Regression, NaiveBayes, SVM, KNN, NeuralNetwork
from resource import save_model

def build_model(X_train, y_train,model_name,topic):

    if model_name == 'decision_tree':
        model = DecisionTree(X_train, y_train)
    elif model_name == 'logistic_regression':
        model = Logistic_Regression(X_train, y_train)
    elif model_name =='naive_bayes':
        model = NaiveBayes(X_train, y_train)
    elif model_name =='svc':
        model = SVM(X_train,y_train)
    elif model_name =='knn':
        model = KNN(X_train,y_train)
    elif model_name =='neuralnetwork':
        model = NeuralNetwork(X_train,y_train)
    
    path = f'BackEnd/resource/topics/{topic}/model_files/{model_name}.pkl'
    save_model(model,path)
    
    return model