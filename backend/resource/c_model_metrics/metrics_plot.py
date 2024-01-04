from sklearn.metrics import confusion_matrix,classification_report, accuracy_score, roc_auc_score, roc_curve
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

def metrics(X_train,y_train,X_test,y_true,model,model_name,topic,compare_df):
    y_pred         = model.predict(X_test)
    test_accuracy  = accuracy_score(y_true,  y_pred).round(4)*100
    train_accuracy = accuracy_score(y_train, model.predict(X_train)).round(4)*100
    
    roc_auc        = roc_auc_score(y_true,y_pred).round(3)

    cm             = confusion_matrix( y_true, y_pred )
    df_cm          = pd.DataFrame(cm,index=['Actual No','Actual Yes'],columns=['Predicted No','Predicted Yes'])
        
    class_report   = classification_report( y_true, y_pred, output_dict = True )
    precision      = class_report['weighted avg']['precision']
    recall         = class_report['weighted avg']['recall']
    f1_score       = class_report['weighted avg']['f1-score']
    accuracy       = class_report['accuracy']
    
    if len(compare_df) == 0 :
        compare_df = pd.DataFrame(columns = ['Accuracy','Train Accuracy','Test Accuracy','Precision','Recall','f1-score','roc_auc_score'])
    
    compare_df.loc[model_name] = [accuracy,train_accuracy,test_accuracy,precision,recall,f1_score,roc_auc]
    
    print(f"Train Accuracy of {model_name} is {train_accuracy}")
    print(f"Test Accuracy of {model_name} is {test_accuracy} \n")

    print('-'*30)
#     df_cm
    print(f"Confusion Matrix :- \n{df_cm}\n")
    print('-'*30)
    print(f"Classification Report :- \n {classification_report( y_true, y_pred )}")
    print('-'*30)
    print(f'roc_auc_score is {roc_auc}')
    fpr, tpr, thresholds = roc_curve(y_true, model.predict_proba(X_test)[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label=f'{model_name}(area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.savefig(f'BackEnd/resource/topics/{topic}/plots/roc/{model_name}_ROC')
    # plt.show()
    
    return compare_df