import streamlit as st
import pandas as pd

st.title("Nine Hole Golf Score Multiple Linear Regression Model Visualization")
gir=st.number_input("Number of Greens in Regulation:",min_value=0,max_value=9)
putts=st.number_input("Number of Putts",min_value=0)
INTERCEPT=33.5541
GIR=-1.2112
PUTTS=.7590
score=INTERCEPT+(PUTTS*putts)+(gir*GIR)
rounded=round(score)
st.metric("**Projected Nine Hole Golf Score:**",rounded)