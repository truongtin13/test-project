import numpy as np
import pandas as pd
import streamlit as st
import re

def df_change():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  dfmid = df.copy()
  COLS = dfmid.columns.values.tolist().copy()
  
  for i in range(3,16): 
    dfmid[COLS[i]].fillna(0, inplace=True)
  
  dfmid[COLS[16]].fillna('N', inplace=True)
  
  def gen(row):
    if row[COLS[1]] == 'M':
      return 'Nam'
    else:
      return 'Nữ'
  dfmid['Gen'] = dfmid.apply(gen, axis=1)
  
  def grade(row):
    for i in range(10,13):
      if row[COLS[2]][:2] == str(i):
        return 'Lớp ' + str(i)
  dfmid['Grade'] = dfmid.apply(grade, axis=1)
  
  subjects = [['Anh','CA'],
             ['Hoá','CH'],
             ['Lý', 'CL'],
             ['Sinh','CS'],
             ['Toán','CT'],
             ['Tin','CTIN'],
             ['Trung - Nhật','CTRN'],
             ['Văn', 'CV'],
             ['Tích hợp / Song ngữ', 'TH','SN'],
             ['Lớp thường', 'A', 'B'],
             ['Sử - Địa', 'CSD']]
  def subject(row):
    r = ''.join(re.findall('\D', row[COLS[2]]))
    for i in subjects:
      if len(i) == 2:
        if r == i[1]:
          return i[0]
      else:
        if r == i[1] or r == i[2]:
          return i[0]
  dfmid['Subject'] = dfmid.apply(subject, axis=1)
  
  def classroom(row):
    return 'A' + row[COLS[3]][:3]
  dfmid['Classroom'] = dfmid.apply(classroom, axis=1)
  
  def partofday(row):
    if row[COLS[3]][-1] == 'C':
      return 'Chiều'
    else:
      return 'Sáng'
  dfmid['Part of day'] = dfmid.apply(partofday, axis=1)
  
  def homework(row):
    return np.round(np.mean(row[COLS[4:9]+COLS[10:13]]),1)
  dfmid['Homework'] = dfmid.apply(homework, axis=1)
  
  def failorpass(row):
    if row['GPA'] >= 6.0:
      return 'Đậu'
    else:
      return 'Rớt'
  dfmid['Fail or Pass'] = dfmid.apply(failorpass, axis=1)
  
  return dfmid
  
df_change()
