import streamlit as st
from model_utils import preprocess_tokenize, generate_summary, model1, tokenizer1, model2, tokenizer2

st.title("Hindi News Headline Generation")

# Input text
input_text = st.text_area("Enter Hindi News Article for Headline Generation:")

if st.button("Summarize"):
    if input_text:
        preprocessed_text = preprocess_tokenize(input_text)
        BARTsummary = generate_summary(preprocessed_text, model1, tokenizer1)
        T5summary = generate_summary(preprocessed_text, model2, tokenizer2)
        st.subheader("IndicBART Summary:")
        st.write(BARTsummary)
        st.subheader("mT5 Summary:")
        st.write(T5summary)
    else:
        st.write("Please enter some text to summarize.")
