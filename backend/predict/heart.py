import pickle
import pandas as pd

model_name = 'decision_tree' 
# model_name = 'logistic_regression'
# model_name = 'naive_bayes'
# model_name = 'svc'
# model_name = 'knn'
# model_name = 'neuralnetwork' 

test = 'test1'
# test = 'test2'


df = pd.read_csv(f'BackEnd/resource/topics/heart/input/predict/{test}.csv')
# print(df)

model_path = f'BackEnd/resource/topics/heart/model_files/{model_name}.pkl'

with open(model_path, 'rb') as f:
    model = pickle.load(f)

y_pred    = model.predict(df)

if y_pred==0:
    print('Your heart is normal')
elif y_pred==1:
    print('Your heart is not normal')
else:
    print('Error')
