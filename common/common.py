import streamlit as st

def click_button(button_key):
    """Callback function to update the button state."""
    # Toggle the state of the clicked button
    st.session_state.button_states[button_key] = not st.session_state.button_states[button_key]