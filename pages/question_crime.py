import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


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


# Content: Question
chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader("To which area of law is your case assigned?")
else:
    st.subheader("Zu welchem Rechtsgebiet ist Ihr Fall zugehörig?")
st.progress((1.0 / 7) * current_step)
if st.session_state.current_lang == "English":
    st.markdown('<div style="text-align: justify;">'
                'TEKO is currently only able to provide support in tenancy law. For other issues, finding a court by '
                'yourself might even not be possible. In the context of a criminal proceeding, a court cannot be selected '
                'by a citizen. Please refer to your subpoena for the appropriate court of a criminal proceeding.'
                '</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align: justify;">'
                'TEKO kann derzeit nur im Mietrecht unterstützen. Bei anderen Angelegenheiten ist es möglicherweise '
                'gar nicht möglich, selbst ein Gericht zu finden. Im Rahmen eines Strafverfahrens kann ein Bürger '
                'kein Gericht wählen. Das zuständige Gericht eines Strafverfahrens entnehmen Sie bitte Ihrer Vorladung.'
                '</div>', unsafe_allow_html=True)

if st.session_state.current_lang == "English":
    question_crime = st.selectbox(label="", options=("Tenancy Law", "Criminal Proceeding", "Other"))
    next_question = st.button("Next Question")
else:
    question_crime = st.selectbox(label="", options=("Mietrecht", "Strafrecht", "Sonstiges"))
    next_question = st.button("Nächste Frage")


if next_question and question_crime in ["Tenancy Law", "Mietrecht"]:
    st.session_state.question_crime = question_crime
    switch_page("question_subject")
elif next_question and question_crime not in ["Tenancy Law", "Mietrecht"]:
    st.error("TEKO is currently only able to provide support in tenancy law!")
