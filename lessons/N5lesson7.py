###### Import packages
import pandas as pd
import streamlit as st
from common.common import *

st.set_page_config(layout="wide")

## to change the size of the button
st.markdown(
    """
<h1 style='text-align: center;'>みんなのにほんご Lesson 7 Vocabulary</h1>
<style>
button {
    height: auto;
    padding-top: 50px !important;
    padding-bottom: 50px !important;
}
</style>

""",
    unsafe_allow_html=True,
)

#### Read vocab list
df = pd.read_csv("assets/lessonN57.csv", delimiter=",")
st.divider()

n_rows = 8
n_cols = 7

# initialize button state in st.session_state
initializeButtons(n_rows, n_cols)

# display the buttons
# buttons in a grid structure
buttonGrid(n_rows, n_cols, df)
        

