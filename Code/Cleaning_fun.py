import pandas as pd
from geopy.geocoders import Nominatim
import reverse_geocoder 
from langdetect import detect, DetectorFactory
import re
import numpy as np
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
not_rel =['id', 'scrape_id', 'last_scraped', 'name','picture_url', 'host_id', 'host_url','host_location', 'license',
'host_name','instant_bookable','neighborhood_overview','neighbourhood_group_cleansed','calendar_updated','host_thumbnail_url','availability_30',
'availability_60', 'availability_90','calendar_last_scraped','listing_url','property_type','bathrooms','host_picture_url','host_listings_count',
'neighbourhood','beds','minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights','minimum_nights_avg_ntm', 
'maximum_nights_avg_ntm','number_of_reviews_ltm','number_of_reviews_l30d','first_review', 'last_review','review_scores_value','calculated_host_listings_count',
'calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms','calculated_host_listings_count_shared_rooms']
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

def lang_clean(des, ha):
    if des == ha and des == 'en': # everything in english
        return 0
    elif des != ha and des == 'en':
        return 1
    elif des != ha and ha == 'en':
        return 2
    else:
        return 3

###############################################################################################

def cl_host_response_time(x):
    if x == 'within an hour': return 0
    if x in ['within a few hours', 'within a day']: return 1
    if x == np.nan: return np.nan
    else: return 2

###############################################################################################

def cl_host_verifications(x):
    x.replace("'",'').replace('[','').replace(']','').replace(' ','').lower().split(',') # let's turn the input into a list
    if len(x) == 2: return 0
    elif len(x)>2 and 'reviews' in x: return 2
    else: return 1

###############################################################################################
def vectorize(df):
    	
    df.host_is_superhost = df.host_is_superhost.apply(lambda x: 1 if x=='t' else 0)
    #df.instant_bookable = df.instant_bookable.apply(lambda x: 1 if x=='t' else 0)
    df.host_has_profile_pic=df.host_has_profile_pic.apply(lambda x: 1 if x=='t' else 0)
    df.has_availability = df.has_availability.apply(lambda x: 0 if x=='t' else 1)
    df.host_identity_verified =	df.host_identity_verified.apply(lambda x: 0 if x=='t' else 1)
    
    df.host_acceptance_rate = df.host_acceptance_rate.apply(lambda x: np.nan if type(x) == float else pd.to_numeric(x[:-1]))
    df.host_response_rate = df.host_response_rate.apply(lambda x: np.nan if type(x) == float else pd.to_numeric(x[:-1]))
    df.host_since = df.host_since.apply(lambda x: np.nan if x==np.nan else 2022-int(re.findall('\d{4}',x)[0]))
    #df.bathrooms_text = df.bathrooms_text(bath_clean)
    df['host_response_time'] = df.host_response_time.apply(cl_host_response_time)
    df['host_verifications'] = df.host_verifications.apply(cl_host_verifications)
    
    
    
    df['lang_des']=detect_lan(df, 'description')
    df['lang_host']=detect_lan(df, 'host_about')
    df['lang_var'] =df.apply(lambda x: lang_clean(x.lang_des,x.lang_host), axis=1)
    df.drop(columns=['host_about','description','lang_des','lang_host'], inplace=True)

    df[[i.lower().replace(' ','_') for i in df.room_type.unique()]] = pd.get_dummies(df.room_type)
    df.drop(columns=['room_type'], inplace=True)
    
    return df


###############################################################################################

###############################################################################################
###############################################################################################