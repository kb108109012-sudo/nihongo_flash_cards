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

N5Lesson2 = st.Page(
    page="lessons/N5lesson2.py",
    title="Lesson 2",
    icon=":material/book:"
)
N5Lesson3 = st.Page(
    page="lessons/N5lesson3.py",
    title="Lesson 3",
    icon=":material/book:"
)
N5Lesson4 = st.Page(
    page="lessons/N5lesson4.py",
    title="Lesson 4",
    icon=":material/book:"
)
N5Lesson5 = st.Page(
    page="lessons/N5lesson5.py",
    title="Lesson 5",
    icon=":material/book:"
)

# navigation
pg = st.navigation(
    {
        "Info": [about_page],
        "N5" : [N5Lesson1, N5Lesson2, N5Lesson3, N5Lesson4, N5Lesson5],
    }
)


# Shared on all pages
st.logo("assets/icon.png")
st.sidebar.text("Made by キルタナ")


# run
pg.run()