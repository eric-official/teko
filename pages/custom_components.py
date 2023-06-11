import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras import card
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu


def show_navbar():
    col1, col2, col3 = st.columns([0.10, 0.05, 0.85])
    with col1:
        st.header("TEKO")
    with col2:
        st.header("|")
    with col3:
        st.header("Unlocking Justice. Made Easy.")

    navbar_style = {
        "nav-link-selected": {"background-color": "black"}
    }
    navbar = option_menu(None, ["Home", "About Us", "FAQ", "Find Court"],
                         icons=['house', 'people', "question-circle", "book"], menu_icon="cast", default_index=0,
                         orientation="horizontal", styles=navbar_style)


def get_local_pages():
    pages = ["home", "question_crime", "question_subject", "question_amount", "question_appeal", "question_city",
            "survey_results", "custom_components", "about_us", "faq"]
    return pages


def components_spacer():
    st.text("")
    st.text("")


def chapter_spacer():
    st.text("")
    st.text("")
    st.text("")
    st.text("")