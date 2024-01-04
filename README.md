# [ML/AI] Heart and Kidney Disease Prediction

## Data Set Sources
- Heart: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- Kidney: [UCI Chronic Kidney Disease Dataset](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)

Both topics are binary classification types.

## Folder Structure
This project comprises two folders: `backend` and `frontend`. Python was used for the backend, while Streamlit was used for the frontend.

### Backend Folder
The backend code is designed for scalability, allowing the addition of multiple projects using common code. To train new classification problems, add newtopic.py under `backend/train` and corresponding resources under `backend/resource/topics/newtopic`.

#### Common Packages and Steps
The common packages and steps are located in resource files under the resource folder. Examples include CSV loading, object loading, column formatting, feature encoding, model metrics, machine learning, neural networks, and hyperparameter tuning.

#### Input Folder
Both training and prediction input files reside in corresponding topic folders. For instance, the kidney train and test input files are found at:
| Task        | File Path                                               |
|-------------|---------------------------------------------------------|
| train       | backend/resource/topics/kidney/input/train/kidney.csv   |
| prediction  | backend/resource/topics/kidney/input/predict/test1.csv  |

#### Training
To train any topic, follow the template located in `backend/train`. For example, to train the kidney dataset, execute the following command: `python backend\train\kidney.py`.

#### Prediction
To predict any topic, follow the template in `backend/predict`. For instance, to predict kidney normal/abnormal status, execute: `python backend\predict\kidney.py`.

#### Feature Importance for Kidney Dataset
  ![feature](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/03e75f57-7c0c-4cae-861b-c44cd9de5d4c)

### Model Performance Metrics Comparison for Heart and Kidney
- **Heart**
  ![modelperfheart](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/f3ff1bdd-4085-472c-a493-c7a923930658)
  
- **Kidney**
  ![modelperfkidney](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/d43622ee-fcef-4328-b9d1-c443ca2dceea)

### Frontend Folder
Run the frontend via `streamlit run frontend/app.py`. Find the screenshots below:

#### Key Feature: App Navigation Option
![appnav](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/d35bb6fb-dce8-4211-8eca-b6608941563a)


#### Heart Screenshots
- ![heart1](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/92e2ce60-7d2a-45f7-9800-fa0e5f60177a)
- ![heart2](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/4179653c-9709-4eff-92bf-755c612ee007)
- ![heart3](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/f265ba9a-7a52-4b88-a5b5-ae8c01e81b2e)

#### Kidney Screenshots
- ![kidney1](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/e1f0168f-83fa-4a28-a183-48fc8933d0fb)
- ![kidney2](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/6c2c0885-f95c-48f4-9bba-d9e75d99e899)
- ![kidney3](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/961d08ec-cba0-4959-9177-5f2c05af0e6b)
- ![kidney4](https://github.com/iamjr15/Heart-and-Kidney-Disease-Prediction/assets/48449428/e59a2166-d3d5-4483-ba21-97006a37e04a)
