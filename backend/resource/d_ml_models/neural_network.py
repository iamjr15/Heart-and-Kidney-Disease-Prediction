from sklearn.neural_network import MLPClassifier

def NeuralNetwork(X_train,y_train):
    NN = MLPClassifier(hidden_layer_sizes=(100,100,100),activation='logistic',solver='adam',max_iter=500)
    NN.fit(X_train, y_train)

    return NN