import streamlit as st
import pandas as pd 
import pickle
from sklearn.tree import DecisionTreeClassifier
from PIL import Image

with open(r'BackEnd\resource\topics\kidney\model_files\decision_tree.pkl', 'rb') as f:
    dt_model = pickle.load(f)

file = open(r"BackEnd\resource\topics\kidney\obj\dle.obj",'rb')
dle_loaded = pickle.load(file)
file.close()

file = open(r"BackEnd\resource\topics\kidney\obj\categoryList",'rb')
category_column = pickle.load(file)
file.close()




def prediction(df,dle_loaded,category_column,dt_model):
    df[category_column] = df[category_column].apply(lambda x: dle_loaded[x.name].transform(x))

    y_pred         = dt_model.predict(df)

    if y_pred==0:
        result = 'kidney is normal'
    elif y_pred==1:
        result = 'kidney is not normal (ckd)'
    else:
        result = 'Error'


    return result

def app():

    st.title("Diagnosis of Kidney disease")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Chronic Kidney Disease</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    status_1 = ['normal','abnormal']
    status_2 = ['notpresent','present']
    option_1 = ['yes','no']
    option_2 = ['good','poor']

    age = st.number_input('Age in years', 1, 100, "min", 1)
    age = int(age)
    blood_pressure = st.number_input('Blood Pressure in mm/Hg')
    specific_gravity        = st.number_input('Specific gravity -(1.005,1.010,1.015,1.020,1.025)')
    albumin                 = st.number_input('albumin - (0,1,2,3,4,5)')
    sugar                   = st.number_input('sugar - (0,1,2,3,4,5)')
    red_blood_cells         = st.selectbox('Red blood cells',options = status_1)
    pus_cell                = st.selectbox('pus cell',options = status_1)
    pus_cell_clumps         = st.selectbox('Pus Cell clumps',options = status_2)
    bacteria                = st.selectbox('bacteria',options = status_2)
    blood_glucose_random    = st.number_input('blood glucose random in mgs/dl ')
    blood_urea              = st.number_input('blood urea in mgs/dl')
    serum_creatinine	    = st.number_input('serum creatinine in mgs/dl')
    sodium                  = st.number_input('sodium in mEq/L')
    potassium	            = st.number_input('potassiumin mEq/L')
    haemoglobin	            = st.number_input('haemoglobin in gms')
    packed_cell_volume	    = st.number_input('packed cell volume')
    white_blood_cell_count	= st.number_input('white blood cell count in cells/cumm')
    red_blood_cell_count	= st.number_input('red blood cell count in millions/cmm')
    hypertension	        = st.selectbox('hypertension',options = option_1)
    diabetes_mellitus	    = st.selectbox('diabetes mellitus',options = option_1)
    coronary_artery_disease	= st.selectbox('coronary artery disease',options = option_1)
    appetite	            = st.selectbox('appetite',options = option_2)
    peda_edema	            = st.selectbox('peda edema',options = option_1)
    aanemia                 = st.selectbox('aanemia',options = option_1)

    input_dict = {'age':[age],
    'blood_pressure':[blood_pressure],
    'specific_gravity':[specific_gravity],
    'albumin':[albumin],
    'sugar':[sugar],
    'red_blood_cells':[red_blood_cells],
    'pus_cell':[pus_cell],
    'pus_cell_clumps':[pus_cell_clumps],
    'bacteria':[bacteria],
    'blood_glucose_random':[blood_glucose_random],
    'blood_urea':[blood_urea],
    'serum_creatinine':[serum_creatinine],
    'sodium':[sodium],
    'potassium':[potassium],
    'haemoglobin':[haemoglobin],
    'packed_cell_volume':[packed_cell_volume],
    'white_blood_cell_count':[white_blood_cell_count],
    'red_blood_cell_count':[red_blood_cell_count],
    'hypertension':[hypertension],
    'diabetes_mellitus':[diabetes_mellitus],
    'coronary_artery_disease':[coronary_artery_disease],
    'appetite':[appetite],
    'peda_edema':[peda_edema],
    'aanemia':[aanemia]
    }
    df = pd.DataFrame(input_dict)

    result=""
    if st.button("Predict"):
        result=prediction(df,dle_loaded,category_column,dt_model)   # predict_note_authentication
    st.markdown(f'<span style="font-size:20px;">**:green[{result} ]**</span>', unsafe_allow_html=True)
    # **:blue[colored]**
    if st.button("About"):
        # st.text("Lets Learn")
        st.text("Built by Jigyansu Rout - UG24 - ASHOKA UNIVERSITY")
