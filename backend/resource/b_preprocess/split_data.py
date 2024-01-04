from sklearn.model_selection import train_test_split

def get_train_test_split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

    return X_train, X_test, y_train, y_test