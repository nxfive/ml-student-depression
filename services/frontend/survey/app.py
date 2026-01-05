import streamlit as st
from questions import ENG, PL


if "language_chosen" not in st.session_state:
    st.session_state.language_chosen = False
if "language" not in st.session_state:
    st.session_state.language = "PL"
if "index" not in st.session_state:
    st.session_state.index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

button_label = "Dalej" if st.session_state.language == "PL" else "Next"

if not st.session_state.language_chosen:
    st.write("Wybierz język ankiety / Select the survey language:")
    st.session_state.language = st.radio(
        "Język / Language:",
        ["PL", "EN"],
        index=0 if st.session_state.language == "PL" else 1,
    )

    def choose_language():
        st.session_state.language_chosen = True

    st.button(button_label, on_click=choose_language)

else:
    questions_dict = PL if st.session_state.language == "PL" else ENG
    questions_keys = list(questions_dict.keys())
    current_index = st.session_state.index

    def next_question():
        key = f"input_{st.session_state.index}"
        st.session_state.answers[questions_keys[st.session_state.index]] = (
            st.session_state.get(key, "")
        )
        st.session_state.index += 1

    if current_index < len(questions_keys):
        key = f"input_{current_index}"
        if key not in st.session_state:
            st.session_state[key] = ""
        st.text_input(questions_dict[questions_keys[current_index]], key=key)
        st.button(button_label, on_click=next_question)

    else:
        success_resp = (
            "Thank you for filling out the survey!"
            if st.session_state.language == "ENG"
            else "Dziękujemy za wypełnienie ankiety!"
        )
        qustions_resp = (
            "Your questions:"
            if st.session_state.language == "ENG"
            else "Twoje odpowiedzi:"
        )
        st.success(success_resp)
        st.write(qustions_resp, st.session_state.answers)
