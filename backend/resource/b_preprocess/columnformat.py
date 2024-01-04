
def Column_Unique_Values(dfk,category_column):
    for count, col in enumerate(category_column):
        print(f"{count+1}) {col} has {dfk[col].unique()} values\n")


def column_format_validation(dfk):    
    numeric_column  = [col for col in dfk.columns if dfk[col].dtype != 'object']
    category_column = [col for col in dfk.columns if dfk[col].dtype == 'object']
    
    return numeric_column, category_column

