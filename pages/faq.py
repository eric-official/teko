import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras import card
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu
from pages.custom_components import get_local_pages, show_navbar, chapter_spacer, components_spacer


# Set config
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[0])
st.session_state.current_page = "FAQ"
st.session_state.current_index = 2

# Create Navbar
show_navbar()


# Title
if st.session_state.current_lang == "English":
    st.title("Frequently Asked Questions")
    components_spacer()
    st.subheader("Questions on the app")

    expander = st.expander(label="What is the app about?")
    expander.write("TEKO assists you in finding the right court for your legal case.")
    expander.write("Our user-friendly question-answer format will navigate you through the process of finding the "
                   "correct court for your case.")
    expander = st.expander(label="How accurate is our app?")
    expander.write("Our decision tree algorithm has been carefully developed and is based on extensive research and "
                   "analysis of court decisions.")
    expander.write("Although the algorithm is very accurate, individual factors in your "
                   "case may affect the results. It is always advisable to do additional research or consult with an "
                   "attorney to ensure you have the most up-to-date information.")
    expander = st.expander(label="Why should you use TEKO?")
    expander.write("Time-savings: Instead of spending hours searching for the right court information, TEKO quickly "
                   "provides you with the necessary details.")
    expander.write("Error avoidance: Our Decision Tree algorithm is based on thorough legal research and can help you "
                   "avoid selecting the wrong court.")
    expander.write("User-friendliness: Our app guides you through the procedure in simple steps, so that even legal "
                   "novices can easily find the right way to the court.")
    expander = st.expander(label="Can the Court Finder be used for all types of legal disputes?")
    expander.write("Our Court Finder is currently designed to assist you in tenancy law. We are working on widening our "
                   "service to a wide range of legal disputes from civil lawsuits to criminal cases, family law matters, "
                   "and administrative issues.")
    expander.write("However, please note that the Court Finder is not a substitute for legal advice, and it is recommended"
                   "that you consult a lawyer to discuss your particular situation.")

    components_spacer()
    st.subheader("Questions on the document area")
    expander = st.expander(label="What happens after I find the right court using the Court Finder?")
    expander.write("Once you have found the right court for your case, you have the option to proceed to our Create "
                   "Document section. After you have entered your data and the necessary information about your case, "
                   "we will provide you with a printable document that you can use to pursue your case in court or "
                   "consult a lawyer to discuss further legal steps.")
    expander = st.expander(label="I don’t know how to write a complaint and what to include. How can you help me with that?")
    expander.write("We understand that writing a complaint can be challenging, especially if you're unsure about what to "
                   "include. Our Court Finder is here to assist you in this process. Here's how we can help:")
    expander.write("   - We provide step-by-step guidance, templates, and examples to help you understand the structure "
                   "and content of a complaint.")
    expander.write("   - TEKO is built on a comprehensive legal knowledgebase. This means that the information and "
                   "guidance provided align with legal standards and best practices. You can rely on our system to help "
                   "you draft a complaint that meets legal requirements.")
    expander.write("   - In addition to the guidance provided within the Court Finder, we are planning to offer access to "
                   "supplementary resources in our next version of the application. These may include links to legal "
                   "resources, articles, or guides that can further assist you in understanding how to write a complaint "
                   "effectively.")
    expander.write("Please keep in mind that while our Court Finder can provide valuable guidance, it is not a substitute "
                   "for legal advice. If you have complex legal concerns or need personalized assistance, we recommend "
                   "consulting with an attorney who can provide you with tailored advice and review your complaint.")

    components_spacer()
    st.subheader("Questions on data security")
    expander = st.expander(label="What happens to my data?")
    expander.write("The security of your data is our top priority. We strictly comply with the European General Data "
                   "Protection Regulation (GDPR).")
    expander.write("The only purpose we use your data is to help you find the right court "
                   "for your case. We keep your information confidential and do not share it with third parties unless "
                   "we are required to do so by law or have your consent.")
    expander = st.expander(label="How long do you retain my data?")
    expander.write("We retain your data for as long as necessary to fulfill the intended purpose of assisting you in "
                   "finding the right court. If you wish to have your data deleted, you can contact our support team, "
                   "and we will promptly handle your request, subject to any legal obligations.")
    expander = st.expander(label="On which devices can I use TEKO?")
    expander.write("TEKO is currently accessible via a web application. We are working to expand the use of the app to "
                   "many devices. Our vision is that you can switch between devices as your data is synchronized in your "
                   "account.")

    components_spacer()
    st.subheader("You have further questions?")
    st.markdown('<div style="text-align: justify;">'
                'Send us an e-mail to: support@teko.com'
                '</div>', unsafe_allow_html=True)

else:

    st.title("Frequently Asked Questions")
    components_spacer()
    st.subheader("Fragen über die App")

    expander = st.expander(label="Worum geht es in dieser App?")
    expander.write("TEKO hilft dir beim Finden des zuständigen Gerichts für deine Klage.")
    expander.write("Unser benutzerfreundliches Frage-Antwort-Format navigiert dich durch den Prozess um das richtige "
                   "Gericht für deine Klage zu finden.")
    expander = st.expander(label="Wie genau ist eure App?")
    expander.write("Unser Entscheidungsbaum-Algorithmus wurde sorgfältig entwickelt und basiert auf umfangreichen "
                   "Recherchen und Analysen von Gerichtsentscheidungen.")
    expander.write("Obwohl der Algorithmus sehr genau ist, können in Ihrem Fall individuelle Faktoren die Ergebnisse "
                   "beeinflussen. Es ist immer ratsam, zusätzliche Nachforschungen anzustellen oder einen Anwalt zu "
                   "konsultieren, um sicherzustellen, dass Sie über die korrekten Informationen verfügen.")
    expander = st.expander(label="Warum sollte ich TEKO benutzen?")
    expander.write("Zeitersparnis: Anstatt stundenlang nach den richtigen Gerichtsinformationen zu suchen, liefert "
                   "Ihnen TEKO schnell die notwendigen Details.")
    expander.write("Fehlervermeidung: Unser Entscheidungsbaum-Algorithmus basiert auf gründlicher juristischer "
                   "Recherche und kann Ihnen dabei helfen, die Wahl des falschen Gerichts zu vermeiden.")
    expander.write("Unsere App führt Sie in einfachen Schritten durch das Verfahren, sodass auch Rechtseinsteiger "
                   "problemlos den richtigen Weg zum Gericht finden.")
    expander = st.expander(label="Kann der Gerichtsfinder für alle Arten von Klagen verwendet werden?")
    expander.write(
        "Unser Court Finder soll Sie aktuell im Mietrecht unterstützen. Wir arbeiten daran, unseren Service auf ein "
        "breites Spektrum von Rechtsstreitigkeiten auszuweiten, von Zivilklagen über Strafsachen bis hin zu "
        "Familienrechtsangelegenheiten und Verwaltungsangelegenheiten.")
    expander.write(
        "Unser Court Finder soll Sie aktuell im Mietrecht unterstützen. Wir arbeiten daran, unseren Service auf ein "
        "breites Spektrum von Rechtsstreitigkeiten auszuweiten, von Zivilklagen über Strafsachen bis hin zu "
        "Familienrechtsangelegenheiten und Verwaltungsangelegenheiten.")
    
    components_spacer()
    st.subheader("Fragen zur Dokumentenerstellung")
    
    expander = st.expander(label="Was passiert nachdem ich das zuständige Gericht mit dem Gerichtsfinder gefunden habe?")
    expander.write("Sobald Sie das richtige Gericht für Ihren Fall gefunden haben, haben Sie die Möglichkeit, "
                   "zu unserem Abschnitt Dokument erstellen zu gehen. Nachdem Sie Ihre Daten und die erforderlichen "
                   "Informationen zu Ihrem Fall eingegeben haben, stellen wir Ihnen ein ausdruckbares Dokument zur Verfügung, "
                   "das Sie verwenden können, um Ihren Fall vor Gericht zu verfolgen oder einen Anwalt zu konsultieren, "
                   "um weitere rechtliche Schritte zu besprechen.")
    
    expander = st.expander(label="Ich weiß nicht, wie ich eine Klage formulieren soll und was sie enthalten soll. "
                           "Wie können Sie mir dabei helfen?")
    expander.write("Wir wissen, dass das Verfassen einer Klage eine Herausforderung sein kann, vor allem, "
                   "wenn Sie sich nicht sicher sind, was Sie schreiben sollen. Unser Gerichtsfinder unterstützt Sie "
                   "bei diesem Prozess. Hier erfahren Sie, wie wir helfen können:")
    expander.write("   - Wir bieten schrittweise Anleitungen, Vorlagen und Beispiele, die Ihnen helfen, den Aufbau "
                   "und Inhalt einer Klage zu verstehen.")
    expander.write("   - TEKO stützt sich auf eine umfassende juristische Wissensdatenbank. Das bedeutet, "
                   "dass die bereitgestellten Informationen und Anleitungen mit den rechtlichen Standards "
                   "und bewährten Verfahren übereinstimmen. Sie können sich darauf verlassen, dass unser System Ihnen hilft, "
                   "eine Klage zu verfassen, die den rechtlichen Anforderungen entspricht.")
    expander.write("   - Zusätzlich zu den im Court Finder enthaltenen Anleitungen planen wir, in der nächsten Version "
                   "der Anwendung Zugang zu zusätzlichen Ressourcen zu bieten. Dazu können Links zu Rechtsquellen, Artikeln "
                   "oder Leitfäden gehören, die Ihnen helfen können, eine Klage effektiv zu verfassen.")
    expander.write("Bitte bedenken Sie, dass unser Gerichtsfinder zwar wertvolle Hinweise geben kann, aber kein Ersatz "
                   "für eine Rechtsberatung ist. Wenn Sie komplexe rechtliche Fragen haben oder persönliche Unterstützung "
                   "benötigen, empfehlen wir Ihnen, einen Anwalt zu konsultieren, der Sie individuell beraten und Ihre Klage prüfen kann.")

    components_spacer()
    st.subheader("Fragen zur Datensicherheit")

    expander = st.expander(label="Was passiert mit meinen Daten?")
    expander.write("Die Sicherheit Ihrer Daten hat für uns oberste Priorität. Wir halten uns streng an die "
                   "Europäische Datenschutzgrundverordnung (GDPR).")
    expander.write("Der einzige Zweck, zu dem wir Ihre Daten verwenden, ist, Ihnen zu helfen, das richtige Gericht für "
                   "Ihren Fall zu finden. Wir behandeln Ihre Daten vertraulich und geben sie nicht an Dritte weiter, "
                   "es sei denn, wir sind gesetzlich dazu verpflichtet oder haben Ihre Zustimmung.")
    expander = st.expander(label="Wie lang speichern Sie meine Daten?")
    expander.write("Wir speichern Ihre Daten so lange, wie es für die Erfüllung des Zwecks, Sie bei der Suche nach dem "
                   "richtigen Gericht zu unterstützen, erforderlich ist. Wenn Sie wünschen, dass Ihre Daten gelöscht werden, "
                   "können Sie sich an unser Support-Team wenden, und wir werden Ihren Antrag vorbehaltlich rechtlicher "
                   "Verpflichtungen umgehend bearbeiten.")
    expander = st.expander(label="Auf welchen Geräten kann ich TEKO verwenden?")
    expander.write("TEKO ist derzeit über eine Webanwendung zugänglich. Wir arbeiten daran, die Nutzung der App auf viele "
                   "Geräte auszuweiten. Unsere Vision ist, dass Sie zwischen den Geräten wechseln können, während Ihre Daten "
                   "in Ihrem Konto synchronisiert werden.")
    
    components_spacer()
    st.subheader("Haben Sie weitere Fragen?")
    st.markdown('<div style="text-align: justify;">'
                'Senden Sie uns eine E-mail an: support@teko.com'
                '</div>', unsafe_allow_html=True)


    
    

    





