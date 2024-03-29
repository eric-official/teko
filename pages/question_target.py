import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 4
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


chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader(f"What is the reason for filing the case?")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'More detailed information about your case is helping us to better support you.'
                '</div>', unsafe_allow_html=True)

    question_target = st.selectbox(label="Your information", options=("Repayment of the rental deposit", "Settlement of the incidental rental costs"), label_visibility="hidden").strip()

    if question_target == "Repayment of the rental deposit":
        st.warning("Please note that you can usually get your deposit back at the earliest 6 months after handing over "
                "the rental property.")
        
    elif question_target == "Settlement of the incidental rental costs":
        st.warning("Please note that you must give the landlord a period of 12 months after the end of the billing period "
                "until he needs to provide you with the utility bill.")
else:
    st.subheader(f"Was ist der Grund Ihrer Klage?")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Detaillierte Informationen zu Ihrem Fall helfen uns, Sie zielgenau zu unterstützen.'
                '</div>', unsafe_allow_html=True)

    question_target = st.selectbox(label="Your information", options=("Rückzahlung Mietkaution", "Abrechnung der Nebenkosten"), label_visibility="hidden").strip()

    if question_target == "Rückzahlung Mietkaution":
        st.warning("Bitte beachten Sie, dass Sie Ihre Kaution in der Regel frühestens 6 Monate nach Übergabe des Mietobjekts gerichtlich einfordern können.")
        
    elif question_target == "Abrechnung der Nebenkosten":
        st.warning("Bitte beachten Sie, dass Sie dem Vermieter eine Frist von 12 Monaten nach Ende des Abrechnungszeitraums einräumen müssen,"+
                   " bis er Ihnen die Nebenkostenabrechnung vorlegen muss.")


if st.session_state.current_lang == "English":
    next_question = st.button("Next question")

    if next_question:
        st.session_state.question_target = question_target
        switch_page("question_amount2")
else:
    next_question = st.button("Nächste Frage")

    if next_question:
        st.session_state.question_target = question_target
        switch_page("question_amount2")
