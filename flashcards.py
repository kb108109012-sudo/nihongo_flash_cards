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
N5Lesson10 = st.Page(
    page="lessons/N5lesson10.py",
    title="Lesson 10",
    icon=":material/book:"
)
N5Lesson11 = st.Page(
    page="lessons/N5lesson11.py",
    title="Lesson 11",
    icon=":material/book:"
)
N5Lesson12 = st.Page(
    page="lessons/N5lesson12.py",
    title="Lesson 12",
    icon=":material/book:"
)
N5Lesson13 = st.Page(
    page="lessons/N5lesson13.py",
    title="Lesson 13",
    icon=":material/book:"
)
N5Lesson14 = st.Page(
    page="lessons/N5lesson14.py",
    title="Lesson 14",
    icon=":material/book:"
)
N5Lesson15 = st.Page(
    page="lessons/N5lesson15.py",
    title="Lesson 15",
    icon=":material/book:"
)

Verb = st.Page(
    page="lessons/verbs.py",
    title="Verb",
    icon=":material/book:"
)
kanji = st.Page(
    page="lessons/kanji.py",
    title="Kanji",
    icon=":material/book:"
)

# navigation
pg = st.navigation(
    {
        "Info": [about_page],
        "Kanji": [kanji],
        "Forms" : [Verb],
        "N5" : [N5Lesson1, N5Lesson2, N5Lesson3, N5Lesson4, 
                N5Lesson5, N5Lesson6, N5Lesson7, N5Lesson8, 
                N5Lesson9, N5Lesson10, N5Lesson11, N5Lesson12,
                N5Lesson13, N5Lesson14, N5Lesson15],
    }
)


# Shared on all pages
st.logo("assets/icon.png")
st.sidebar.text("Made by キールタナ")
st.sidebar.image("assets/psyduck.png",width=150)


# run
pg.run()
