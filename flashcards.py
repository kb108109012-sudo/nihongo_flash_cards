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
N5Lesson6 = st.Page(
    page="lessons/N5lesson6.py",
    title="Lesson 6",
    icon=":material/book:"
)
N5Lesson7 = st.Page(
    page="lessons/N5lesson7.py",
    title="Lesson 7",
    icon=":material/book:"
)
N5Lesson8 = st.Page(
    page="lessons/N5lesson8.py",
    title="Lesson 8",
    icon=":material/book:"
)
N5Lesson9 = st.Page(
    page="lessons/N5lesson9.py",
    title="Lesson 9",
    icon=":material/book:"
)


# navigation
pg = st.navigation(
    {
        "Info": [about_page],
        "N5" : [N5Lesson1, N5Lesson2, N5Lesson3, N5Lesson4, 
                N5Lesson5, N5Lesson6, N5Lesson7, N5Lesson8, 
                N5Lesson9],
    }
)


# Shared on all pages
st.logo("assets/icon.png")
st.sidebar.text("Made by キールタナ")


# run
pg.run()