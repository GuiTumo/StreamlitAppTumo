#Streamlit app

import streamlit as st
import pandas as pd
import numpy as np

st.title('Health Form')

score = 0
bar = st.progress(score)

coluna1 = []
coluna2 = []



st.write('At what time do you usually go to bed? ')

option1 = st.selectbox('Time:', ['-----','19:00 - 24:00','24:00 - 3:00','3:00 - 8:00'])

if option1 == "19:00 - 24:00":
    score+=25
    coluna1.append(25)
    coluna2.append(1)
    bar.progress(score)
elif option1 == '24:00 - 3:00':
    score+=12
    coluna1.append(12)
    coluna2.append(1)
    bar.progress(score)
elif option1 == '3:00 - 8:00':
    score+=6
    coluna1.append(6)
    coluna2.append(1)
    bar.progress(score)

st.write('Do you ussualy have breakfast? ')

option2 = st.selectbox('', ['-----','Yes','No'])

if option2 == "Yes":
    score+=25
    coluna1.append(25)
    coluna2.append(2)
    bar.progress(score)
elif option2 == 'No':
    score+=10
    coluna1.append(10)
    coluna2.append(2)
    bar.progress(score)

st.write('Do you have an Active Lifestyle or an Sedentary Lifestyle? ')

option3 = st.selectbox('', ['-----','Active Lifestyle','Sedentary Lifestyle'])

if option3 == "Active Lifestyle":
    score+=25
    coluna1.append(25)
    coluna2.append(3)
    bar.progress(score)
elif option3 == 'Sedentary Lifestyle':
    coluna1.append(5)
    coluna2.append(3)
    score+=5
    bar.progress(score)


st.write('Do you smoke? ')

option4 = st.selectbox(' ',['-----','Yes','No'])

if option4 == "Yes":
    coluna1.append(-10)
    score-=10
    bar.progress(score)
    coluna2.append(3)
    st.warning("Don't smoke")
elif option4 == 'No':
    coluna1.append(25)
    score+=25 
    coluna2.append(3)
    bar.progress(score)
    st.balloons()

if score >= 75 <=100:
    st.write('Tens good habits :))))))) ')
    st.image('happyemoji.jpg',use_column_width=True)
elif score >=50 <=74:
    st.write('Podia ser melhor :))))))) ')
    st.image('notbademoji.webp',use_column_width=True)
elif score >=0 <=49:
    st.warning('Devias começar a tratar mais de ti :) ')
    st.image('sademoji.png',use_column_width=True)

df = pd.DataFrame({
    'Score': coluna1,
    'Questions': coluna2
})

st.write('Score bar chart:')

st.bar_chart(df)

