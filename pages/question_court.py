import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
import re
from pages.custom_components import *
from src.google_maps import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 1
if st.session_state.current_lang == "English":
    st.session_state.current_page = "Find Court"
    st.session_state.current_index = 3
else:
    st.session_state.current_page = "Gericht Finden"
    st.session_state.current_index = 3



# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()

court_decision = st.session_state.question_court
lines = court_decision.split('\n')
court_decision = lines[0]
court_decision = court_decision.replace(',', '')

court_location = get_address(court_decision)
court_location = court_location.replace(', ', ',\n')
court_location = court_location.replace(',\nDeutschland', '')
court_location = court_location.replace(',\nGermany', '') 


chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader(f"The Court Finder identified {court_decision} as the appropriate court.")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Please confirm the court selection or enter the details of another court.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader(f"Der Gerichtsfinder hat das {court_decision} als das zuständige Gericht identifiziert.")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Bitte bestätigen Sie die Gerichtsselektion oder fügen Sie die Anschrift des passenden Gerichts ein.'
                '</div>', unsafe_allow_html=True)

question_court_address = st.text_area(label="Appropriate Court", value=court_decision+',\n'+court_location, 
                                      height=200, max_chars=150, label_visibility="hidden").strip()


if st.session_state.current_lang == "English":
    next_question = st.button("Next question")
else:
    next_question = st.button("Nächste Frage")

if next_question:
    st.session_state.question_court = question_court_address
    switch_page("question_plaintiff")
