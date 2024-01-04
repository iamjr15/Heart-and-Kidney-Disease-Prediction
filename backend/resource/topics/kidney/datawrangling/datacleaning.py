def data_cleaning(dfk):

    dfk['diabetes_mellitus'].replace(to_replace = {'\tno':'no','\tyes':'yes',' yes':'yes'},inplace=True)

    dfk['coronary_artery_disease'] = dfk['coronary_artery_disease'].replace(to_replace = '\tno', value='no')

    dfk['class'].replace(to_replace = {'ckd\t': 'ckd', 'notckd': 'not ckd'}, inplace = True)

    return dfk