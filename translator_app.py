import streamlit as st
from deep_translator import GoogleTranslator

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
        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text")
        st.write(translated_text)
    else:
        st.warning("Please enter some text.")
