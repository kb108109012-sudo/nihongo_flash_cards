import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("assets/verb_masu.csv", delimiter=",")

st.title(f"Verb {df.columns[0]} and て Form")
st.write("")
st.divider()

st.header("Rules:")
st.write("Group 1: 2 syllable and い line")
st.write("Group 1: (い、ち、り) - って　(に、び、み) - んで　(き) - いて　(ぎ) - いで　(し) - して")
st.write("Group 2: 1 syllable and え line")
st.write("Group 2: + て")
st.write("Group 3: きます、します")
st.write("Group 3: + て")

st.divider()

st.write("Group 1 looking, but are in group 2 (exceptions):")
st.write("おきます　かり　おり　あび　でき　たり")

st.divider()

st.write("")
st.write("Lesson 4")

# Lesson4
st.dataframe(
    df.iloc[1:7],
    hide_index=True,)

st.write("Lesson 5")
# Lesson5
st.dataframe(
    df.iloc[8:11],
    hide_index=True,)
st.write("Lesson 6")
# Lesson6
st.dataframe(
    df.iloc[12:23],
    hide_index=True,)
st.write("Lesson 7")
# Lesson7
st.dataframe(
    df.iloc[24:33],
    hide_index=True,)

st.write("Lesson 9")
# Lesson9
st.dataframe(
    df.iloc[34:36],
    hide_index=True,)

st.write("Lesson 10")
# Lesson10
st.dataframe(
    df.iloc[37:39],
    hide_index=True,)

st.write("Lesson 11")
# Lesson11
st.dataframe(
    df.iloc[40:46],
    hide_index=True,)

st.write("Lesson 13")
# Lesson13
st.dataframe(
    df.iloc[47:57],
    hide_index=True,)

st.write("Lesson 14")
# Lesson14
st.dataframe(
    df.iloc[58:79],
    hide_index=True,)

st.write("Lesson 15")
# Lesson15
st.dataframe(
    df.iloc[80:88],
    hide_index=True,)

st.write("Lesson 16")
# Lesson16
st.dataframe(
    df.iloc[89:103],
    hide_index=True,)

st.write("Lesson 17")
# Lesson17
st.dataframe(
    df.iloc[104:118],
    hide_index=True,)