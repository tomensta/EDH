#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:15:10 2022

@author: tom
"""

import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

folder = r"/home/tom/Documents/EDH/Dataset/eco2mix-metropoles-tr/"
file = r"Rennes.json"

filepath = Path(folder + file)

with open(filepath) as f:
   jdata = json.load(f)


FIELDS_VALUES =     [
    'nature',
    'code_insee_epci',
    'date',
    'consommation',
    'heures',
    'date_heure',
    'libelle_metropole'
                    ]


conso_global = []
time = []


def moyenne_journaliere(dic_my, releve, day):

    try:
        dic_my[str(day)] = dic_my[str(day)] + releve["consommation"] 
    except KeyError:
        dic_my[str(day)] = releve["consommation"]
    
    return dic_my

plt.figure(figsize = (40,10))        

for m in range(1,13):
    
    dic_month = {}

    for dic_j in jdata:
        try:
            releve = dic_j["fields"] 
            ymd = releve["date"].split("-")
            ymd_trial = ['2020',"%02d" % m]
            if ymd[0:2] == ymd_trial:
                dic_month = moyenne_journaliere(dic_month, releve, ymd[-1])
        except KeyError: 
            print(dic_j["fields"]["date"].split("-")[1:])
    
    plt.scatter(list(dic_month.keys()), list(dic_month.values()), label = str(m))
plt.legend()
plt.show()

#%% Panda dataframe

df = pd.read_json(filepath)
    