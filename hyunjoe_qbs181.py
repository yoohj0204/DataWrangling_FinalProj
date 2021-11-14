# -*- coding: utf-8 -*-
"""Hyunjoe_QBS181.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vx78_0h8-CUrLA2siXb_RxMuH8c016qh
"""

#import
import os
import pandas as pd
import numpy as np
import re
import io

#connecting drive/path
from google.colab import files
from google.colab import drive
#uploaded = files.upload()
drive.mount("/content/gdrive/", force_remount=True)
path='/content/drive/My Drive/'

#read 2020 data
data20=pd.read_csv('gdrive/My Drive/QBS181/2020-child-and-adult-health-care-quality-measures.csv')
data20.head

#read 2019 data
data19=pd.read_csv('gdrive/My Drive/QBS181/2019-child-and-adult-health-care-quality-measures-quality.afrw-yks2.csv')
data19.head

#checking for any NA value
data20.isnull().values.any()

#checking where the value is: 3346 missing values in Notes column - does not affect the analysis
data20.isnull().sum()

#checking for any NA value
data19.isnull().values.any()

#checking where the value is: 3017 and 42 missing values in Notes and Rate column
data19.isnull().sum()

#3450-3387=63, so dropped rows of 63 Non reported state rate 
data20.rename(columns={'State Rate': 'StateRate'}, inplace=True)
data20=data20[~data20.StateRate.str.contains("NR")]
data20

data20_trim = data20[['State', 'Reporting Program', 'Measure Type', 'StateRate']]
data20_trim.head()
#trimmed 2020 data - only necessary columns for calculations

#3450-3387=63, so dropped rows of 63 Non reported state rate 
data19.rename(columns={'State Rate': 'StateRate'}, inplace=True)
data19=data19[~data19.StateRate.str.contains("NR")]
data19

data19_trim = data19[['State', 'Reporting Program', 'Measure Type', 'StateRate']]
data19_trim.head()
#trimmed 2019 data - only necessary columns for calculations

#extract adult core set data (2020)
data20_trim_a = data20_trim[data20_trim['Reporting Program'].str.contains('Adult Core Set')]
data20_trim_adult = data20_trim_a[data20_trim_a['Measure Type'].str.contains('Higher')]

data20_trim_adult

#extract child core set data (2020)
#data20_trim_child=data20_trim[data20_trim['Reporting Program'].str.contains('Child Core Set')]
#print(data20_trim_child)

data20_trim_c = data20_trim[data20_trim['Reporting Program'].str.contains('Child Core Set')]
data20_trim_child = data20_trim_a[data20_trim_a['Measure Type'].str.contains('Higher')]

data20_trim_child

#extract adult core set data (2019)
#data19_trim_adult=data19_trim[data19_trim['Reporting Program'].str.contains('Adult Core Set')]
#print(data19_trim_adult)

data19_trim_a = data19_trim[data19_trim['Reporting Program'].str.contains('Adult Core Set')]
data19_trim_adult = data19_trim_a[data19_trim_a['Measure Type'].str.contains('Higher')]

data19_trim_adult

#extract child core set data (2019)
#data19_trim_child=data19_trim[data19_trim['Reporting Program'].str.contains('Child Core Set')]
#print(data19_trim_child)

data19_trim_c = data19_trim[data19_trim['Reporting Program'].str.contains('Child Core Set')]
data19_trim_child = data19_trim_a[data19_trim_a['Measure Type'].str.contains('Higher')]

data19_trim_child

data20_trim_adult=data20_trim_adult.sort_values(by=['StateRate'])
data20_trim_adult

data_a_rank=data20_trim_adult.copy()
#data_a_rank['rank']=data20_trim_adult.groupby('StateRate').rank()

data_a_rank.sort_values("StateRate", inplace = True)
  
# creating a rank column and passing the returned rank
data_a_rank["Rank"] = data_a_rank["StateRate"].rank()
data_a_rank.sort_values("Rank", inplace = True)

data_a_rank.groupby("Rank")

data_a_rank

#Count the number of occurrences of each state in top 10% for 2020 adult data
data_a_rank_10 = data_a_rank.head(177)
data_a_rank_10
data_a_rank_10['State'].value_counts()

data_c_rank=data20_trim_child.copy()
#data_a_rank['rank']=data20_trim_adult.groupby('StateRate').rank()

data_c_rank.sort_values("StateRate", inplace = True)
  
# creating a rank column and passing the returned rank
data_c_rank["Rank"] = data_c_rank["StateRate"].rank()
data_c_rank.sort_values("Rank", inplace = True)

data_c_rank.groupby("Rank")

data_c_rank

#Count the number of occurrences of each state in top 10% for 2020 children data
data_c_rank_10 = data_c_rank.head(163)
data_c_rank_10
data_c_rank_10['State'].value_counts()

data_a_rank_19=data19_trim_adult.copy()
#data_a_rank['rank']=data20_trim_adult.groupby('StateRate').rank()

data_a_rank_19.sort_values("StateRate", inplace = True)
  
# creating a rank column and passing the returned rank
data_a_rank_19["Rank"] = data_a_rank_19["StateRate"].rank()
data_a_rank_19.sort_values("Rank", inplace = True)

data_a_rank_19.groupby("Rank")

data_a_rank_19

#Count the number of occurrences of each state in top 10% for 2020 adult data
data_a_rank_19_10 = data_a_rank_19.head(142)
data_a_rank_19_10
data_a_rank_19_10['State'].value_counts()

data_c_rank_19=data19_trim_child.copy()
#data_a_rank['rank']=data20_trim_adult.groupby('StateRate').rank()

data_c_rank_19.sort_values("StateRate", inplace = True)
  
# creating a rank column and passing the returned rank
data_c_rank_19["Rank"] = data_c_rank_19["StateRate"].rank()
data_c_rank_19.sort_values("Rank", inplace = True)

data_c_rank_19.groupby("Rank")

data_c_rank_19

#Count the number of occurrences of each state in top 10% for 2019 children data
data_c_rank_19_10 = data_c_rank_19.head(162)
data_c_rank_19_10
data_c_rank_19_10['State'].value_counts()