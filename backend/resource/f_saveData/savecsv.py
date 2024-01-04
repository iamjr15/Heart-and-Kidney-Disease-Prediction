def save_result(df,topic):
    df.to_csv(f'BackEnd/resource/topics/{topic}/result/model_compare.csv')