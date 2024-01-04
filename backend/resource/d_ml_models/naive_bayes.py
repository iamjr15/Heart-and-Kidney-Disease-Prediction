from sklearn.naive_bayes import GaussianNB

    
def NaiveBayes(X_train, y_train):
    NB = GaussianNB()
    NB.fit(X_train,y_train)

    return NB