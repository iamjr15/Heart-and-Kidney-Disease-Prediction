def get_features_target(dfh):
    X = dfh.drop(columns='target', axis=1)
    y = dfh['target']

    return X, y