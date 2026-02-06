import streamlit as st

st.markdown(
    """
<h1 style='text-align: center;'>Flashcards for みんなのにほんご</h1>
""",
    unsafe_allow_html=True,
)

st.divider()

st.markdown(
    """
<p style='text-align: center;'>Please pick the lesson you would like to revise.</p>
""",
    unsafe_allow_html=True,
)
left_co, cent_co,last_co = st.columns([0.9, 5, 0.2])
with cent_co:
    st.image("assets/bookcover.png", width=500)