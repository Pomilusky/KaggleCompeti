import pandas as pd
from geopy.geocoders import Nominatim
import reverse_geocoder 
from langdetect import detect, DetectorFactory
import re
DetectorFactory.seed = 3

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
not_rel = ['id', 'scrape_id', 'last_scraped', 'name','picture_url', 'host_id', 'host_url','host_location', 'license',
'host_name','instant_bookable','neighborhood_overview']
def Clean_columns(df, colms = not_rel, inpl = False):
    return df.drop(columns = colms, inplace=inpl)

###############################################################################################
def city_country_fun(df):
    df['coord'] = df.apply(lambda x: (x['latitude'], x['longitude']), axis=1)
    df.drop(columns=['latitude','longitude'], inplace=True)
    geo_info = reverse_geocoder.search(list(df.coord))
    countries = [i['cc'] for i in geo_info]
    cities = [i['name'] for i in geo_info]
    df['city'] = cities
    df['cc'] = countries
    df.drop(columns=['coord'], inplace=True)
    return df
###############################################################################################

def detect_lan(df, serie):
    app = []
    for i in df[serie]:
        if type(i) == str:
            try:
                app.append(detect(i))
            except:
                app.append('Unknown')
        else:
            app.append('Unknown')
    return app

###############################################################################################

def bath_clean(s):
    if re.findall('(?i)(shared)|(half)',str(s)):
        return 0
    
    else:
        if re.findall('\d',str(s)): return re.findall('\d',s)[0]
        else: return 0

###############################################################################################
