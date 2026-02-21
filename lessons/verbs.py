import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("assets/verb_masu.csv", delimiter=",")

st.title(f"Verb {df.columns[0]}")
st.write("")
st.divider()
st.write("")
st.write("")
st.write("Lesson 4")

# Lesson4
st.dataframe(
    df.iloc[2:7],
    hide_index=True,)

st.write("Lesson 5")
# Lesson5
st.dataframe(
    df.iloc[9:11],
    hide_index=True,)
st.write("Lesson 6")
# Lesson6
st.dataframe(
    df.iloc[13:23],
    hide_index=True,)
st.write("Lesson 7")
# Lesson7
st.dataframe(
    df.iloc[26:33],
    hide_index=True,)