import streamlit as st
import base64

def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

def initializeButtons(n_rows, n_cols):
    if 'button_states' not in st.session_state:
        st.session_state.button_states = {f"btn_{i}": False for i in range(n_rows*n_cols)}

def click_button(button_key):
    """Callback function to update the button state."""
    # Toggle the state of the clicked button
    st.session_state.button_states[button_key] = not st.session_state.button_states[button_key]

def buttonGrid(n_rows, n_cols, df):
    words = df.shape[0]
    count_word = 0
    dfArray = df.to_numpy()
    for i in range(n_rows):
        cols = st.columns(n_cols)
        for j in range(n_cols):
            button_key = f"btn_{count_word}"
            with cols[j]:
                # Change button label/appearance based on state (optional)
                if st.session_state.button_states[button_key]:
                    autoplay_audio("assets/click.mp3")
                    label = f"{dfArray[count_word][1]}"
                else:
                    label = f"{dfArray[count_word][0]}"

                #label = f"{dfArray[count_word][1]}" if st.session_state.button_states[button_key] \
                #    else f"{dfArray[count_word][0]}"
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
