import streamlit as st
import base64


# Page setup

about_page = st.Page(
    page="views/about_page.py",
    title="Welcome",
    icon=":material/auto_stories:",
    default=True,
)

N5Lesson1 = st.Page(
    page="lessons/N5lesson1.py",
    title="Lesson 1",
    icon=":material/book:"
)

# navigation
pg = st.navigation(
    {
        "Info": [about_page],
        "N5" : [N5Lesson1]
    }
)


# Shared on all pages
st.logo("assets/icon.png")
st.sidebar.text("Made by キルタナ")


# run
pg.run()