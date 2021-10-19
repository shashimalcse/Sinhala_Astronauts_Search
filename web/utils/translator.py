import googletrans
from googletrans import Translator
import json
import csv
import pandas as pd
import time


def translate():
    df = pd.read_csv('./astronauts.csv')
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

    
