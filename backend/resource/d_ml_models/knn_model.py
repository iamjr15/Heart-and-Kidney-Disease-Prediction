from sklearn.neighbors import KNeighborsClassifier

def KNN(X_train,y_train):
    knn = KNeighborsClassifier()
    knn.fit(X_train,y_train)

    return knn