from src.function.data_function import read_temp_change

def RankImpact(nannee, npays,ascending=False):
    max_Year = 2019
    min_Year = max_Year - nannee
    max_Year_col = "Y"+str(max_Year)
    min_Year_col = "Y"+str(min_Year)
    res = read_temp_change()
    res = res.loc[(res[max_Year_col].notna()) & (res[min_Year_col].notna())]
    res['Impact Since'] = abs(res[max_Year_col] - res[min_Year_col])

    # Get the list of columns
    columns_list = res.columns.tolist()

    # Print the list of columns
    print(columns_list)


    res = res.loc[:, ['Country Code','Country Name eng','Country Name fr', 'Impact Since']]
    res = res.sort_values(by='Impact Since', ascending=ascending)
    res = res.head(npays)
    return res