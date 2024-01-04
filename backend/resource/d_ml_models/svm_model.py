from sklearn.svm import SVC

def SVM(X_train, y_train):
    svc = SVC(kernel = 'linear',probability=True)
    svc.fit(X_train, y_train)

    return svc