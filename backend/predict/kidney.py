import pickle
import pandas as pd

model_name = 'decision_tree' 
# model_name = 'logistic_regression'
# model_name = 'naive_bayes'
# model_name = 'svc'
# model_name = 'knn'
# model_name = 'neuralnetwork' 


 # test = 'test1'
test = 'test2'


df = pd.read_csv(f'BackEnd/resource/topics/kidney/input/predict\{test}.csv')
# print(df)

with open(f'BackEnd/resource/topics/kidney/model_files/{model_name}.pkl', 'rb') as f:
    dt_model = pickle.load(f)

file = open(r"BackEnd/resource/topics/kidney/obj/dle.obj",'rb')
dle_loaded = pickle.load(file)
file.close()

file = open(r"BackEnd/resource/topics/kidney/obj/categoryList",'rb')
category_column = pickle.load(file)
file.close()

# print('category_column',category_column)

df[category_column] = df[category_column].apply(lambda x: dle_loaded[x.name].transform(x))

y_pred         = dt_model.predict(df)

if y_pred==0:
    print('Your kidney is normal')
elif y_pred==1:
    print('Your kidney is not normal')
else:
    print('Error')
