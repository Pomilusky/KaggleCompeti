import pandas as pd


###############################################################################################
def num_NaNs(df, n=0):
    """ This function recives as an input a DataFrame and the output is a dictionari with the Dataframe columns that have 
    NaNs as a key and the number of NaNs as the Value. In order to make the results easier to read I have added a parameter n,
    it allows to restric the number of NaNs in columns, so for instance if we say n=100 it is going to add only the columns with over a 
    hundred NaNs. 
    Inputs: df -----> The DataFrame
            n  -----> minimum number of NaNs
    Output: dict({cols: num.Nans})"""
    NaNs_dict = dict({column: df[column].isna().sum() for column in df.columns})
    keys = []
    for k, v in NaNs_dict.items():
        if v < n:
            keys.append(k)
    for k in keys:
        NaNs_dict.pop(k)
    return NaNs_dict
###############################################################################################
columns_2drop = ['listing_url', 'scrape_id', 'last_scraped', 'host_id', 'host_url', 'region_id', 'region_name', 'region_parent_id', 'region_parent_name', 
'region_parent_parent_id','region_parent_parent_name', 'license', 'picture_url', 'host_thumbnail_url','calendar_updated','requires_license','last_searched']
def Clean_columns(df, colms = columns_2drop, inpl = False):
    return df.drop(columns = colms, inplace=inpl)
###############################################################################################
