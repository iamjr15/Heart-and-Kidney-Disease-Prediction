from sklearn.linear_model import LogisticRegression

def Logistic_Regression(X_train, y_train):
    LogisticReg = LogisticRegression()
    LogisticReg.fit(X_train, y_train)

    return LogisticReg