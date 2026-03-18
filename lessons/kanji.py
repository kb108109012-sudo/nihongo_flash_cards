###### Import packages
import pandas as pd
import streamlit as st
from common.common import *

st.set_page_config(layout="wide")

## to change the size of the button
st.markdown(
    """
<h1 style='text-align: center;'>かんじ</h1>
<style>
button {
    height: auto;
    padding-top: 80px !important;
    padding-bottom: 80px !important;
}
</style>

""",
    unsafe_allow_html=True,
)

#### Read vocab list
df = pd.read_csv("assets/kanji.csv", delimiter=",")
st.divider()

n_rows = 2
n_cols = 5

# initialize button state in st.session_state
initializeButtons(n_rows, n_cols)

# display the buttons
# buttons in a grid structure
buttonGrid(n_rows, n_cols, df)
