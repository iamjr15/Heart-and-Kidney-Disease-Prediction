import streamlit as st
import pandas as pd 
import pickle
from sklearn.tree import DecisionTreeClassifier

from PIL import Image


with open(r'BackEnd\resource\topics\heart\model_files\decision_tree.pkl', 'rb') as f:
    dt_model = pickle.load(f)




def prediction(df,dt_model):
    
    y_pred         = dt_model.predict(df)

    if y_pred==0:
        result = 'Heart is normal'
    elif y_pred==1:
        result = 'Heart is not normal,   > 50% diameter narrowing  (in any major vessel: attributes 59 through 68 are vessels)'
    else:
        result = 'Error'

    return result

def app():
    st.title("Diagnosis of heart disease")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Angiographic Disease Status
</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    status_1 = ['normal','abnormal']
    status_2 = ['notpresent','present']
    option_2 = ['good','poor']

    age = st.number_input('Age in years', 1, 120, "min", 1)
    age = int(age)
    gender = {1: "male", 0: "female"}
    def format_func(option1):
        return gender[option1]
    sex = st.selectbox("Gender", options=list(gender.keys()), format_func=format_func)

    cpt = {0:'asymptomatic',1:'atypical angina',2:'non-anginal pain',3:'typical angina'} 
    
    def format_func(option1):
        return cpt[option1]   
   
    cp = st.selectbox("chest pain type", options=list(cpt.keys()), format_func=format_func)

    trestbps = st.number_input('resting blood pressure (in mm Hg on admission to the hospital)')
    
    chol = st.number_input('serum cholestoral in mg/dl')
    fbs = st.number_input('fbs: (fasting blood sugar > 120 mg/dl)')
   
    ecg = {0:'normal',1:'having ST-T wave abnormality',2:'showing probable or definite left ventricular hypertrophy by Estes\' criteria'} 
    
    def format_func(option1):
        return ecg[option1]
    restecg = st.selectbox("resting electrocardiographic results", options=list(ecg.keys()), format_func=format_func)
     
    thalach = st.number_input('thalach: maximum heart rate achieved')

    exop = {1:'yes',0:'no'}
    def format_func(option1):
        return exop[option1]

    exang = st.selectbox('exang: exercise induced angina ',options =list(exop.keys()), format_func=format_func)

    oldpeak = st.number_input('oldpeak: ST depression induced by exercise relative to rest')

    slp = {1:'upsloping',2:'flat',3:'downsloping'}
    def format_func(option1):
        return slp[option1]

    slope = st.selectbox('slope: the slope of the peak exercise ST segment',options =list(slp.keys()), format_func=format_func)

    ca_opt = [0,1,2,3]
    ca = st.selectbox('ca: number of major vessels (0-3) colored by flourosopy',options = ca_opt)

    thalopt = {3 : 'normal', 6 :'fixed defect', 7 :'reversable defect'}
    def format_func(option1):
        return thalopt[option1]

    thal = st.selectbox('slope: the slope of the peak exercise ST segment',options =list(thalopt.keys()), format_func=format_func)


    input_dict = {'age':[age],
    'sex':[sex],
    'cp':[cp],
    'trestbps':[trestbps],
    'chol':[chol],
    'fbs':[fbs],
    'restecg':[restecg],
    'thalach':[thalach],
    'exang':[exang],
    'oldpeak':[oldpeak],
    'slope':[slope],
    'ca':[ca],
    'thal':[thal]
        }
    df = pd.DataFrame(input_dict)
    # print(df)

    result=""
    if st.button("Predict"):
        result=prediction(df,dt_model)   # predict_note_authentication
    st.markdown(f'<span style="font-size:20px;">**:green[{result} ]**</span>', unsafe_allow_html=True)
    # **:blue[colored]**
    if st.button("About"):
        # st.text("Lets Learn")
        st.text("Built by Jigyansu Rout - UG24 - ASHOKA UNIVERSITY")
