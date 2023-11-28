#Import Packages
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np

#Data import
dat=pd.read_csv("MLB Data new.csv")
dat=dat.sort_values(by='Player',ascending=True)#Sort By Player Name

#Image Variable For Import
pic=Image.open('MLBi1.JPEG')

#Initial Title and Header
st.title('Scoreboard Science November Issue')
st.header('MLB Postseason Expected Runs Model Project')
st.divider()

#User Input
playerchoice=st.selectbox('Select a player from the dropdown below to see how they performed in the postseason against our model:',dat['Player'])

#Subset Data Based on User Input
playerdata=dat[dat['Player']== playerchoice]

#Display Data
col1, col2, col3 = st.columns(3)
col1.metric("Expected Runs Per Game", playerdata['Expected R/G (Based on Regular Season)'])
col2.metric("Actual Postseason Runs Per Game",playerdata['Actual R/G Postseason'])
col3.metric("Runs Per Game Variance", playerdata['R/G Variance '])
st.divider()

#Display Data Frame
st.header('Utilize our data below to sort values as you wish by clicking on the column names')
st.dataframe(dat)
st.image(pic,width=300)


