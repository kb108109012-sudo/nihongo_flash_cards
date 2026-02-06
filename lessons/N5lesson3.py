###### Import packages
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

## to change the size of the button
st.markdown(
    """
<h1 style='text-align: center;'>みんなのにほんご Lesson 3 Vocabulary</h1>
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
df = pd.read_csv("assets/lessonN53.csv", delimiter=",")
japanese_words = df['Japanese'].to_numpy()
english_words = df['English'].to_numpy()

st.divider()

n_rows = 6
n_cols = 7

if 'button_states' not in st.session_state:
    st.session_state.button_states = {f"btn_{i}": False for i in range(n_rows*n_cols)}

def click_button(button_key):
    """Callback function to update the button state."""
    # Toggle the state of the clicked button
    st.session_state.button_states[button_key] = not st.session_state.button_states[button_key]

dfArray = df.to_numpy()

# display the buttons
# buttons in a grid structure


words = df.shape[0]
count_word = 0
for i in range(n_rows):
    cols = st.columns(n_cols)
    for j in range(n_cols):
        button_key = f"btn_{count_word}"
        with cols[j]:
            # Change button label/appearance based on state (optional)
            label = f"{dfArray[i*n_cols+j][1]}" if st.session_state.button_states[button_key] \
                else f"{dfArray[i*n_cols+j][0]}"
            st.button(
                label,
                key=button_key,
                on_click=click_button,
                args=(button_key,),
                use_container_width=True
            )
        count_word = count_word + 1
        if count_word == words:
            break
#st.write("Current button states:", st.session_state.button_states)
        

