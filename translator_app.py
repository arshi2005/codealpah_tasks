import streamlit as st
from googletrans import Translator

translator = Translator()

st.title("Language Translation Tool")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Telugu": "te"
}

source_lang = st.selectbox("Source Language", languages.keys())
target_lang = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    if text.strip():
        result = translator.translate(
            text,
            src=languages[source_lang],
            dest=languages[target_lang]
        )
        st.success("Translated Text")
        st.write(result.text)
    else:
        st.warning("Please enter some text to translate.")
