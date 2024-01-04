import pandas as pd
from resource import column_format_validation, save_object
from resource.topics.kidney.datawrangling.datacleaning import data_cleaning

def preprocess(dfk,topic):

    dfk.drop('id', axis = 1, inplace = True)

    dfk.columns = ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell',
                'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium',
                'potassium', 'haemoglobin', 'packed_cell_volume', 'white_blood_cell_count', 'red_blood_cell_count',
                'hypertension', 'diabetes_mellitus', 'coronary_artery_disease', 'appetite', 'peda_edema',
                'aanemia', 'class']

    dfk['packed_cell_volume']       = pd.to_numeric(dfk['packed_cell_volume'], errors='coerce')
    dfk['white_blood_cell_count']   = pd.to_numeric(dfk['white_blood_cell_count'], errors='coerce')
    dfk['red_blood_cell_count']     = pd.to_numeric(dfk['red_blood_cell_count'], errors='coerce')

    numeric_column, category_column = column_format_validation(dfk)

    category_column.remove('class')
 
    dfk = data_cleaning(dfk)
    
    path = f"BackEnd/resource/topics/{topic}/obj/categoryList"
 
    save_object(category_column,path)

    return dfk, numeric_column, category_column
