def get_features_target(dfk):
    features = [col for col in dfk.columns if col != 'class']
    target = 'class'

    X = dfk[features]
    y = dfk[target]

    return X, y