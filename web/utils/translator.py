import googletrans
from googletrans import Translator
import json
import csv
import pandas as pd
import time

def clean_data(df):
    allowed_status = ["Active","Retired","Deceased"]
    df['status'] = np.where((df.status == 'active'),'Active',df.status)
    df['status'] = np.where((df.status == 'retired'),'Retired',df.status)
    df['status'] = np.where((df.status == 'deceased'),'Deceased',df.status)
    df.loc[~df["status"].isin(allowed_status), "status"] = None
    df['status'] = df['status'].fillna("")
    df['nationality'] = df['nationality'].fillna("")
    df['selection'] = df['selection'].fillna("")
    df['occupation'] = df['occupation'].fillna("")
    df['summary'] = df['summary'].fillna("")
    return df
def translate():
    df = pd.read_csv('./astronauts.csv')
    df = clean_data(df)
    translator = Translator()
    translator.raise_Exception = True
    cols_to_trans = ['name','status','nationality','selection','occupation','summary']
    for col in cols_to_trans:
        temp = []
        print(col)
        for i in df[col]:
            translated = translator.translate(i, dest='sinhala').text
            temp.append(translated)
            time.sleep(1)
        df[col] = temp
    return df

    
