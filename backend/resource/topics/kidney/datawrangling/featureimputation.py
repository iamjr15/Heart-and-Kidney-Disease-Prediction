from resource import label_encoder,save_object
import pandas as pd

def random_value_imputation(feature ,dfk):
    random_sample = dfk[feature].dropna().sample(dfk[feature].isna().sum())
    random_sample.index = dfk[dfk[feature].isnull()].index
    dfk.loc[dfk[feature].isnull(), feature] = random_sample

    return dfk
    
def impute_mode(feature, dfk):
    mode = dfk[feature].mode()[0]
    dfk[feature] = dfk[feature].fillna(mode)

    return dfk


def transform(dfk, numeric_column, category_column,topic):

    dfk['class'] = dfk['class'].map({'ckd': 1, 'not ckd': 0})
    dfk['class'] = pd.to_numeric(dfk['class'], errors='coerce')
    
    for col in numeric_column:
        dfk = random_value_imputation(col,dfk)

    dfk = random_value_imputation('red_blood_cells',dfk)
    dfk = random_value_imputation('pus_cell',dfk)

    for col in category_column:
        dfk = impute_mode(col,dfk)

    dfk, object = label_encoder(dfk,category_column)

    path = f"BackEnd/resource/topics/{topic}/obj/dle.obj"
 
    save_object(object,path)
 
    return dfk

