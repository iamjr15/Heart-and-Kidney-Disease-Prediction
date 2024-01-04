from resource.c_model_metrics.model import build_model
from resource.c_model_metrics.metrics_plot import metrics
import pandas as pd

def train_models(X_train,y_train,X_test,y_test,model_list,topic):
    model_compare = pd.DataFrame()
    for model_name in model_list:
        model         = build_model(X_train,y_train,model_name,topic)
        model_compare = metrics(X_train,y_train,X_test,y_test,model,model_name,topic,model_compare)

    return model_compare